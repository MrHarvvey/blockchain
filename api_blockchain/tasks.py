from celery import shared_task
from .utils.database_blockchain import BlockchainVerify
import time


@shared_task
def run_function():
    while True:
        build_block = BlockchainVerify()
        time.sleep(20)
        return "baza zaktulizowana"

