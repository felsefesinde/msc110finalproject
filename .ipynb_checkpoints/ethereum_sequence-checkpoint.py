import web3
import random

def generate_eth_sequence():    
    RPC_URL = "https://eth.meowrpc.com"

    w3 = web3.Web3(web3.Web3.HTTPProvider(RPC_URL))
    data = w3.eth.get_block("latest")
    transactions = data["transactions"]

    random_num = random.sample(range(len(transactions) + 1) , 2)
    sequence = ""

    for num in random_num:
        sequence += transactions[num].hex()[2:]


    return sequence
