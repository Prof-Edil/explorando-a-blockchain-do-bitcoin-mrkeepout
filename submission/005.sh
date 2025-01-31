# Create a 1-of-4 P2SH multisig address from the public keys in the four inputs of this tx:
#   `37d966a263350fe747f1c606b159987545844a493dd38d84b070027a895c4517`
#!/bin/bash
txid="37d966a263350fe747f1c606b159987545844a493dd38d84b070027a895c4517"
tx=$(bitcoin-cli getrawtransaction $txid 1)
keys=$(echo $tx | jq -r '.vin[].txinwitness | select(.) | .[1]')
keys_array=$(echo "$keys" | jq -s -R 'split("\n")[:-1]')
bitcoin-cli createmultisig 1 "$keys_array"
