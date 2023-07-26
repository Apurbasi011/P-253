# --------------253 Proj----------------
from web3 import Web3
# Import time module here
import time
 

ganache_url = 'http://127.0.0.1:7545'

web3_ganache_connection = Web3(Web3.HTTPProvider(ganache_url))

Alice_account = '0x726942AF234f201a7E8588F5edCf8FBdB946f4a1'
James_account = '0x08425004faB3ab4a6615Ca5199c9E82399aA1A83'
Ryan_account  = '0x916A6E915788F7df8EE316209bFdFBEc412647e5'


nonce1 = web3_ganache_connection.eth.get_transaction_count(Alice_account)

transaction_data1 = {
    'nonce': nonce1,
    'to': James_account,
    'value':web3_ganache_connection.to_wei(10, 'ether'),
    'gas':21000,
    'gasPrice':web3_ganache_connection.to_wei(50,'gwei')
}

private_key1 = '0x2a1bcc5011dc81342e8dc845fd77c6dc921c5de3b6c7b689e3c1353c4b71a7cc'

singed_transaction1 = web3_ganache_connection.eth.account.sign_transaction(transaction_data1,private_key1)
transaction_hash1 = web3_ganache_connection.eth.send_raw_transaction(singed_transaction1.rawTransaction)

print(web3_ganache_connection.to_hex(transaction_hash1))



# -----------------
"Define the print statement and" 
"sleep() function here"
print('Wait for few seconds Transaction is in progress...')
time.sleep(5)
# -----------------



nonce2 = web3_ganache_connection.eth.get_transaction_count(James_account)

transaction_data2 = {
    'nonce': nonce2,
    'to': Ryan_account,
    'value':web3_ganache_connection.to_wei(15, 'ether'),
    'gas':21000,
    'gasPrice':web3_ganache_connection.to_wei(40,'gwei')
}

private_key2 = '0x36ef0376d9d1254d70bdbb9f425d2ff9766d280c1d3b5f7c0b91eb3d40f25248'

singed_transaction2 = web3_ganache_connection.eth.account.sign_transaction(transaction_data2,private_key2)
transaction_hash2 = web3_ganache_connection.eth.send_raw_transaction(singed_transaction2.rawTransaction)

print(web3_ganache_connection.to_hex(transaction_hash2))
