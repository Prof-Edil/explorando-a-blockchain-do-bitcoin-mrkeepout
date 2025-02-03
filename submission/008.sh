# Which public key signed input 0 in this tx:
#   `e5969add849689854ac7f28e45628b89f7454b83e9699e551ce14b6f90c86163`
TXID="e5969add849689854ac7f28e45628b89f7454b83e9699e551ce14b6f90c86163"
DECODED_TX=$(bitcoin-cli getrawtransaction $TXID true)
REDEEM_SCRIPT=$(echo "$DECODED_TX" | jq -r '.vin[0].txinwitness[2]')
PUBKEY=$(echo "$REDEEM_SCRIPT" | grep -oE "02[0-9a-f]{64}|03[0-9a-f]{64}" | head -n 1)
echo "$PUBKEY"
