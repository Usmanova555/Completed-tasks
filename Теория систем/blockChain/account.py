import datetime
import hashlib
import json
import rsa
from uuid import uuid4


class Account:
    def __init__(self):
        self.private_key = ""
        self.public_key = ""

    def generate_keys(self):
        public_key, private_key = rsa.newkeys(1024)
        self.private_key = private_key
        self.public_key = public_key

        # with open("public.pem","wb") as f:
        #     f.write(public_key.save_pkcs1("PEM"))
        #
        # with open("private.pem","wb") as f:
        #     f.write(private_key.save_pkcs1("PEM"))
        return public_key, private_key

    def create_transaction(self ,data):
        transaction_id = str(uuid4()).replace('-' ,'')
        timestamp = str(datetime)

        transaction = {}
        transaction['transaction_id'] = transaction_id
        transaction['timestamp'] = timestamp
        transaction['data'] = data

        return transaction

    def get_signature(self ,transaction ,private):
        encoded_transaction = json.dumps(transaction ,sort_keys=True).encode()
        signature = rsa.sign(encoded_transaction ,private ,"SHA-256")

        return signature
