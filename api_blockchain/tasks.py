from celery import shared_task
from .utils.database_blockchain import BlockchainVerify


@shared_task(max_retries=0, ignore_result=True)
def run_function():
    build_block = BlockchainVerify()
    return "baza zaktulizowana"

