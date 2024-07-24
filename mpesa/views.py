import logging
from django.conf import settings
from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from .models import MpesaRequest, MpesaResponse
from .serializers import MpesaRequestSerializer, MpesaResponseSerializer
import requests
import base64
from datetime import datetime

logger = logging.getLogger(__name__)

class MpesaRequestView(APIView):

    def get(self, request, pk=None):
        if pk:
            mpesa_request = get_object_or_404(MpesaRequest, pk=pk)
            serializer = MpesaRequestSerializer(mpesa_request)
        else:
            mpesa_requests = MpesaRequest.objects.all()
            serializer = MpesaRequestSerializer(mpesa_requests, many=True)
        return Response(serializer.data)

    def post(self, request):
        logger.info('Received POST request with data: %s', request.data)
        serializer = MpesaRequestSerializer(data=request.data)
        if serializer.is_valid():
            mpesa_request = serializer.save()
            response_data = self.initiate_stk_push(mpesa_request)
            if 'errorCode' in response_data:
                return Response({'error': response_data['errorMessage']}, status=status.HTTP_400_BAD_REQUEST)
            mpesa_response = MpesaResponse.objects.create(
                request=mpesa_request,
                merchant_request_id=response_data.get('MerchantRequestID', ''),
                checkout_request_id=response_data.get('CheckoutRequestID', ''),
                response_code=response_data.get('ResponseCode', ''),
                response_description=response_data.get('ResponseDescription', ''),
                customer_message=response_data.get('CustomerMessage', '')
            )
            response_serializer = MpesaResponseSerializer(mpesa_response)
            return Response(response_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        mpesa_request = get_object_or_404(MpesaRequest, pk=pk)
        serializer = MpesaRequestSerializer(mpesa_request, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        mpesa_request = get_object_or_404(MpesaRequest, pk=pk)
        mpesa_request.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def initiate_stk_push(self, mpesa_request):
        access_token = get_access_token()
        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = {
            "Authorization": f"Bearer {access_token}"
        }
        payload = {
            "BusinessShortCode": settings.MPESA_SHORTCODE,
            "Password": generate_password(),
            "Timestamp": datetime.now().strftime('%Y%m%d%H%M%S'),
            "TransactionType": "CustomerPayBillOnline",
            "Amount": float(mpesa_request.amount),  # Convert Decimal to float
            "PartyA": mpesa_request.phone_number,
            "PartyB": settings.MPESA_SHORTCODE,
            "PhoneNumber": mpesa_request.phone_number,
            "CallBackURL": "https://your-callback-url.com/callback",  # Update with your actual callback URL
            "AccountReference": mpesa_request.account_reference,
            "TransactionDesc": mpesa_request.transaction_desc
        }
        response = requests.post(api_url, json=payload, headers=headers)
        logger.info(f"STK Push Response: {response.json()}")
        return response.json()

@api_view(['POST'])
def stk_push(request):
    logger.info(f"Request Data: {request.data}")
    serializer = MpesaRequestSerializer(data=request.data)
    if serializer.is_valid():
        mpesa_request = serializer.save()
        mpesa_view = MpesaRequestView()  # Create an instance to call the method
        response_data = mpesa_view.initiate_stk_push(mpesa_request)
        if 'errorCode' in response_data:
            return Response({'error': response_data['errorMessage']}, status=status.HTTP_400_BAD_REQUEST)
        mpesa_response = MpesaResponse.objects.create(
            request=mpesa_request,
            merchant_request_id=response_data.get('MerchantRequestID', ''),
            checkout_request_id=response_data.get('CheckoutRequestID', ''),
            response_code=response_data.get('ResponseCode', ''),
            response_description=response_data.get('ResponseDescription', ''),
            customer_message=response_data.get('CustomerMessage', '')
        )
        response_serializer = MpesaResponseSerializer(mpesa_response)
        return Response(response_serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def get_access_token():
    consumer_key = settings.MPESA_CONSUMER_KEY
    consumer_secret = settings.MPESA_CONSUMER_SECRET
    api_url = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
    r = requests.get(api_url, auth=requests.auth.HTTPBasicAuth(consumer_key, consumer_secret))
    logger.info(f"Access Token Response: {r.json()}")
    return r.json().get('access_token')

def generate_password():
    shortcode = settings.MPESA_SHORTCODE
    passkey = settings.MPESA_PASSKEY
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    data_to_encode = shortcode + passkey + timestamp
    encoded_string = base64.b64encode(data_to_encode.encode())
    return encoded_string.decode('utf-8')
