from django.db import models
from django.utils import timezone


class Operation(models.Model):
    date_transaction = models.DateTimeField(default=timezone.now, null=False)
    src_account = models.CharField(max_length=26, null=False)
    des_account = models.CharField(max_length=26, null=False)
    transaction_id = models.TextField(null=False)
    amount = models.DecimalField(max_digits=7, decimal_places=2)
    hash_blockchain = models.TextField(null=True)

    def __str__(self):
        return f'{self.des_account}  {self.src_account}'


class Blockchain(models.Model):
    transaction = models.TextField(null=False)
    prev_hash = models.TextField(null=False)
    hash = models.TextField(null=False)
    random_int = models.FloatField(null=False)
