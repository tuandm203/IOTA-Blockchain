import os

from dotenv import load_dotenv

from iota_sdk import Wallet

# This example requests funds from the faucet

load_dotenv()

FAUCET_URL = os.environ.get(
    'FAUCET_URL',
    os.environ['FAUCET_URL'])

wallet = Wallet(os.environ['WALLET_DB_PATH'])

account = wallet.get_account(os.environ['USER_NAME'])

address = account.addresses()[0].address
print(address)

response = wallet.get_client().request_funds_from_faucet(FAUCET_URL, address=address)
print(response)