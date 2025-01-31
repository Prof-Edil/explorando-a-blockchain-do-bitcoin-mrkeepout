# Using descriptors, compute the taproot address at index 100 derived from this extended public key:
#   `xpub6Cx5tvq6nACSLJdra1A6WjqTo1SgeUZRFqsX5ysEtVBMwhCCRa4kfgFqaT2o1kwL3esB1PsYr3CUdfRZYfLHJunNWUABKftK2NjHUtzDms2`
#!/bin/bash
# Descritor 
descriptor="tr(xpub6Cx5tvq6nACSLJdra1A6WjqTo1SgeUZRFqsX5ysEtVBMwhCCRa4kfgFqaT2o1kwL3esB1PsYr3CUdfRZYfLHJunNWUABKftK2NjHUtzDms2/100/*)"

# Obtaining descriptor checksum
descriptor_info=$(bitcoin-cli getdescriptorinfo "$descriptor")
corrected_descriptor=$(echo $descriptor_info | jq -r '.descriptor')

# Deriva o endereço Taproot no índice 100 usando o descritor corrigido
bitcoin-cli deriveaddresses "$corrected_descriptor" "[100,100]"
