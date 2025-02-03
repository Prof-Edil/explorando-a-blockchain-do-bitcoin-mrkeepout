import subprocess
import json

def bitcoin_cli(command, args=[]):
    args = [str(arg) for arg in args]
    result = subprocess.run(
        ["bitcoin-cli", command] + args,
        capture_output=True,
        text=True
    )
    if result.returncode != 0:
        raise Exception(f"Error at bitcoin-cli: {result.stderr.strip()}")
    try:
        return json.loads(result.stdout)
    except json.JSONDecodeError:
        return result.stdout.strip()

try:
    # ------ STEP 1: Obtaining data from 256,128 ------
    hash_bloco_256128 = bitcoin_cli("getblockhash", [256128])
    bloco_256128 = bitcoin_cli("getblock", [hash_bloco_256128, 2])  # verbosity=2 para transações completas
    
    # Extracting TXID from coinbase (first transaction)
    tx_coinbase = bloco_256128["tx"][0]["txid"]
    output_alvo = f"{tx_coinbase}:0"  # Format TXID:VOUT

    # ------ STEP 2: Analyse block 257,343 ------
    hash_bloco_257343 = bitcoin_cli("getblockhash", [257343])
    bloco_257343 = bitcoin_cli("getblock", [hash_bloco_257343, 2])  # verbosity=2
    
    # ------ STEP 3: Search the spend  ------
    resposta = None
    for tx in bloco_257343["tx"]:
        for vin in tx["vin"]:
            if "txid" in vin and "vout" in vin:
                vin_ref = f"{vin['txid']}:{vin['vout']}"
                if vin_ref == output_alvo:
                    resposta = tx["txid"]
                    break
        if resposta:
            break

    # ------ RETURN ------
    if resposta:
        print(f"{resposta}")
    else:
        print("Any transaction was found.")

except Exception as e:
    print(f"\nERROR: {str(e)}")