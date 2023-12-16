import datetime
import hashlib
import json
import rsa
from account import Account
import requests
from arbitary import Arbitary
from collections import namedtuple


index = 0

class MasondoCoin:
    global block

    def __init__(self,previous_block_hash,transaction_list):
        global index
        #self.chain = []


        self.previous_block_hash = previous_block_hash
        self.position = index
        self.nonce = 0
        self.timestamp = str(datetime)
        self.arbitary_signature = ""
        self.transaction_list = transaction_list
        self.block_data = "-".join(transaction_list) + "-" + previous_block_hash
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()

        mining = False

        if(self.position != 0):
            if(self.isValid()):
                # while mining is False:
                #     self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()
                #     if self.block_hash[:1] == '0':
                #         mining = True
                #     else:
                #         self.nonce += 1
                #         self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()

                block.add(self)
            else:
                print(" Block is Invalid ")
        else:
            block.add(self)




        index = index + 1

    def get_signature(self):
        payload = {'digest': self.block_hash}
        arbitary = Arbitary('http://89.108.115.118/ts',payload)
        #return arbitary.request
        zama = arbitary.request.json()
        self.timestamp = zama["timeStampToken"]["ts"]
        self.arbitary_signature = zama["timeStampToken"]['signature']

        print(zama)


    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
            sort_keys=True, indent=4)

    def isValid(self):
        if(block.chain[self.position - 1].block_hash == self.previous_block_hash):
            return True
        else:
            print(block.chain[self.position - 1].block_hash + " >> ")
            print(self.previous_block_hash)
            return False
    def add_transaction_to_pool(self,transaction,public_key,signature):
        encoded_transaction = json.dumps(transaction, sort_keys=True).encode()
        isvalid = rsa.verify(encoded_transaction,signature,public_key)
        if isvalid == "SHA-256":
            self.transaction_list.append(transaction)
            return True
        else:
            return False






class SignedChain:
    def __init__(self):
        self.chain = []

    def add(self,block):
        self.chain.append(block)
    def isValid(self):
        valid = True

        for i in range(len(self.chain)-1):
            if(self.chain[i].block_hash != self.chain[i+1].previous_block_hash and valid):
                valid = False

        return valid
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
            sort_keys=True, indent=4)

    def save(self):
        sl = self.toJSON()
        with open('blockChain.json', 'w') as f:
            json.dump(sl, f)






t1 = "Masondo sends 2.3 MC to David"
t2 = "David sends 5.3 MC to Masondo"
t3 = "Jobe sends 7 MC to Sbu"
t4 = "Sbu sends 1 MC to Menzi"
t5 = "Menzi sends 0.3 MC to William"
block = SignedChain()


initial_block = MasondoCoin("Initialising",[t1,t2])
first_block = MasondoCoin(initial_block.block_hash,[t3,t4])
second_block = MasondoCoin(first_block.block_hash,[t4,t5])
fake_block = MasondoCoin("Zamokuhle",["Fake Stuff","just fake Man"])

##print(first_block.block_data)
#print(block.chain[1].block_data)
print(first_block.isValid())
print(block.isValid())
block.save()
first_block.get_signature()
#print(block.toJSON())


