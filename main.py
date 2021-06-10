#import hashlib to use sha256 encrption
import hashlib

#bacis block chain class, which needs the previous hash and the transaction list
class PyroCoinBlock:
    def __init__(self, previousBlockHash, listTransactions):
        self.previousBlockHash = previousBlockHash
        self.listTransactions = listTransactions

        #making the data that is the list of transactions joined with the previous hash
        self.blockData = "-".join(listTransactions) + "-" + previousBlockHash
        #using sha256 to encode the blockdata
        self.blockHash = hashlib.sha256(self.blockData.encode()).hexdigest()

#--Lists of transactions if anything chages here it'll changes the hashes 
t1 = "Bob sends 3.001 PC to Jack"
t2 = "Jack sends 3.69 PC to Someone"
t3 = "Anna sends 609 PC to Brad"
t4 = "Josh sends 4.21 PC to Chad"
t5 = "Nikki sends 6.77 PC to Rat"
t6 = "Popo sends 9.754 PC to Kami"

#inital block which all other blocks are essentially connected to, with the previous blockHash just being a random string
initBlock = PyroCoinBlock("Initial String", [t1, t2])
print(initBlock.blockData)
print(initBlock.blockHash)

#2nd block
secondBlock = PyroCoinBlock(initBlock.blockHash, [t3, t4])
print(secondBlock.blockData)
print(secondBlock.blockHash)

#3rd block 
thirdBlcok = PyroCoinBlock(secondBlock.blockHash, [t5, t6])
print(thirdBlcok.blockData)
print(thirdBlcok.blockHash)
