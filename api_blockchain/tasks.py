from celery import shared_task
from .utils.database_blockchain import BlockchainVerify
import time


@shared_task
def run_function():
    build_block = BlockchainVerify()
    return "baza zaktulizowana"

@shared_task
def run_function_1():
    build_block = BlockchainVerify()
    return "baza w drugim watku zaktuliowana"

