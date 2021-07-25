from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import *
import uuid
from api_blockchain.tasks import run_function


#run_function.apply_async()


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

        transaction = Operation.objects.get(transaction_id=transaction_uuid)
        if transaction.transaction_id == transaction_uuid:
            data_response = {
                "src_account": src_account,
                "des_account": des_account,
                "amount": amount,
                "transaction_uuid": transaction_uuid,
                "date": new_transaction.date_transaction
            }
        else:
            data_response = {
                'error': "something went wrong"
            }
    return Response(data_response, status=status.HTTP_200_OK)


@api_view(['POST'])
def transaction_history(request):
    if request.method == 'POST':
        input_json = request.data
        num_trans = input_json.get("num_trans")
        if num_trans:
            all_transactions = Blockchain.objects.all()[:int(num_trans)]
            data_response = {}
            for ix, item in enumerate(all_transactions):
                data_response[f'transaction_{ix + 1}'] = item.transaction
        else:
            all_transactions = Blockchain.objects.all()
            data_response = {}
            for ix, item in enumerate(all_transactions):
                data_response[f'transaction_{ix + 1}'] = item.transaction
        return Response(data_response, status=status.HTTP_200_OK)


