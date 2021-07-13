from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import *
import uuid
import hashlib


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

        data_response = {
            "src_account": src_account,
            "des_account": des_account,
            "amount": amount,
            "transaction_uuid": transaction_uuid,
            "date": new_transaction.date_transaction
        }
        new_transaction.save()
        all_transactions = Operation.objects.all()
        if len(all_transactions) == 10:
            record_str = ""
            for operation in all_transactions:
                record_str += f'{operation.id}:{operation.date_transaction}:{operation.src_account}:' \
                              f'{operation.des_account}:{operation.amount};'
                operation.delete()

            new_record = Blockchain(transaction=record_str, prev_transaction=(hashlib.sha256
                                                                              (record_str.encode()).hexdigest()))
            new_record.save()

    return Response(data_response, status=status.HTTP_200_OK)

@api_view(['POST'])
def transaction_history(request):
    if request.method == 'POST':
        input_json = request.json

        data_response = {
            "streets": input_json
        }
    return Response(data_response, status=status.HTTP_200_OK)
