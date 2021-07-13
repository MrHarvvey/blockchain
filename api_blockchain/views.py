from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Operation
import uuid

@api_view(['POST'])
def transfer_normal(request):
    if request.method == 'POST':
        input_json = request.data
        src_account = input_json.get("src_account")
        des_account = input_json.get("des_account")
        amount = input_json.get("amount")
        transaction_uuid = uuid.uuid4().hex
        new_transaction = Operation(src_account=src_account, des_account=des_account, amount=amount,
                                    transaction_id=transaction_uuid)
        new_transaction.save()

        data_response = {
            "streets": input_json
        }
    return Response(data_response, status=status.HTTP_200_OK)

@api_view(['POST'])
def transaction_history(request):
    if request.method == 'POST':
        input_json = request.json

        data_response = {
            "streets": input_json
        }
    return Response(data_response, status=status.HTTP_200_OK)
