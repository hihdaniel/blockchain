# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 05:11:45 2021

@author: dan
"""
import json
from datetime import datetime,timezone
import secrets


#custom_blockchain = [Sender_Timeline, Receiver_Timeline, Used_Block_Names, All_Block_Names, Block_Resolution_Time, Block_Validators_Accepting_The_Most_Recent_Block,]
#Block = [Block_Name, Block_Creation_Time, List_Of_Transactions_Included_In_Block, Coin_Validator]

#Coin_Validator not in use yet
#----------------------------------------start
#1st if*prompt user to initiate a transaction, asks how much, asks to whom. 2nd if*sets the utc time variable if successful
Sender = secrets.choice(range(1000000000,9999999999))
initiate_transaction_question = int(input('press 1 to initiate a transaction.'))
initiate_transaction = ()
Transaction_Creation_Time = ()
Amount_Of_Coins_Being_Sent = float(input('how much will you send? min 0.000000000000000001'))
Recipient = (input('enter the wallet address of recipient'))

if initiate_transaction_question == 1:
    initiate_transaction = (True),
    Amount_Of_Coins_Being_Sent
    Transaction_Creation_Time = datetime.now(timezone.utc)
#    print(Transaction_Creation_Time)
else:
    print('transaction not initiated.')
#-----------------------------------end
#########################################
transaction = [Sender, Recipient, Amount_Of_Coins_Being_Sent, Transaction_Creation_Time]
#########################################
#-----------------------------------start


initiate_transaction_question
print(transaction)
