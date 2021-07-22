from celery import shared_task
from .utils.database_blockchain import BlockchainVerify
import time


@shared_task
def run_function():
    while True:
        verify_records = BlockchainVerify()
        time.sleep(10)


@shared_task
def run_function2():
    while True:
        print("jest super")
        time.sleep(10)