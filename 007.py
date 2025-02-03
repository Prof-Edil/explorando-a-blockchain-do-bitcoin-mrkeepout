import requests

block_height = 123321
url = f"https://blockchain.info/block-height/{block_height}?format=json"
response = requests.get(url)
data = response.json()

# Acesse as transações do bloco
transactions = data['blocks'][0]['tx']

# Itere sobre as transações para encontrar o output não gasto
for tx in transactions:
    for output in tx['out']:
        if 'spent' not in output or not output['spent']:
            print(f"Endereço não gasto: {output['addr']}")