import bittensor as bt

wallet = bt.wallet(name = 'Miner', )
wallet.create_new_coldkey()
print (wallet)
"Wallet (default, default, ~/.bittensor/wallets/)"
