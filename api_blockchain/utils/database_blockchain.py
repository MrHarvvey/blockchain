from ..models import Blockchain, Operation
import hashlib


class BlockchainVerify:

    def __init__(self):
        all_objects = Operation.objects.all().filter(added_blockchain=False)
        while len(all_objects) > 10:
            operations = all_objects[:10]
            record_str = ""
            for operation in operations:
                record_str += f'{operation.id}:{operation.date_transaction}:{operation.src_account}:' \
                              f'{operation.des_account}:{operation.amount};'
                operation.added_blockchain = True
                operation.save()
            previus_record = Blockchain.objects.last()
            prev_hash = previus_record.hash
            random_int = 0
            while True:
                random_int += 1
                hashable_string = record_str + prev_hash + str(random_int)
                my_hash = hashlib.sha256(hashable_string.encode()).hexdigest()
                if my_hash[-5:] == 'aaaaa':
                    break
            new_blockchain = Blockchain(transaction=record_str, prev_hash=prev_hash, random_int=random_int,
                                        hash=my_hash)
            new_blockchain.save()
            all_objects = Operation.objects.all().filter(added_blockchain=False)

