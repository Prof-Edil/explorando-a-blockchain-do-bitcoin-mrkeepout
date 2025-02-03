import requests

block_height = 123321
url = f"https://blockchain.info/block-height/{block_height}?format=json"
response = requests.get(url)
data = response.json()

transactions = data['blocks'][0]['tx']

for tx in transactions:
    for output in tx['out']:
        if 'spent' not in output or not output['spent']:
            print(f"{output['addr']}")
