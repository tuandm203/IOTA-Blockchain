import os

from dotenv import load_dotenv

import json
from datetime import datetime


from iota_sdk import MintNftParams, Wallet, utf8_to_hex

load_dotenv()

# In this example we will mint an nft

wallet = Wallet(os.environ['WALLET_DB_PATH'])

if 'STRONGHOLD_PASSWORD' not in os.environ:
    raise Exception(".env STRONGHOLD_PASSWORD is undefined, see .env.example")

wallet.set_stronghold_password(os.environ["STRONGHOLD_PASSWORD"])

account = wallet.get_account(os.environ['USER_NAME'])

# Sync account with the node
response = account.sync()

# Get current timestamp
current_time = datetime.now().isoformat()

# Sensor data
sensor_data = {
    "device_name": "sensor_device_1",
    "timestamp": current_time,
    "light": 250
}

json_data = json.dumps(sensor_data)


outputs = [MintNftParams(
    immutableMetadata=utf8_to_hex(json_data),
)]

transaction = account.mint_nfts(outputs)
print(f'Block sent: {os.environ["EXPLORER_URL"]}/block/{transaction.blockId}')