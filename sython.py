import os
import json
import requests
import subprocess
A = '\033[1;34m'#ازرق
X = '\033[1;33m' #اصفر

filename = 'sython.json'

try:
    with open(filename, 'r') as f:
        data = json.load(f)
        api_id = data['api_id']
        api_hash = data['api_hash']
        bot_token = data['bot_token']
        DEVLOO = data['DEVLOO']
        MAX_ACCOUNTS = data['MAX_ACCOUNTS']
        id_bot = bot_token.split(':')[0]  # Extract id_bot from bot_token

        # Send a GET request to the Telegram API
        response = requests.get(f'https://api.telegram.org/bot{bot_token}/getme')
        response_data = response.json()

        # Extract bot_username from the response
        user_bot = response_data['result']['username']
except FileNotFoundError:
    api_id = 15687161
    print('  ')
    api_hash = 'b9e6c423ac5fa8727de33967c3c6b2a6'
    print('  ')
    bot_token = "7877982888:AAHQyyDpPsyko3DA5KvYSIFH62Xz2Ka-7uw"
    print('  ')
    DEVLOO = "6620607756"
    print('  ')
    MAX_ACCOUNTS = "50"
    print('  ')
    id_bot = bot_token.split(':')[0]  # Extract id_bot from bot_token
    print('  ')

    # Send a GET request to the Telegram API
    response = requests.get(f'https://api.telegram.org/bot{bot_token}/getme')
    response_data = response.json()

    # Extract bot_username from the response
    user_bot = response_data['result']['username']
    
    print('  ')
    
    data = {
        'api_id': api_id,
        'api_hash': api_hash,
        'bot_token': bot_token,
        'DEVLOO': DEVLOO,
        'MAX_ACCOUNTS': MAX_ACCOUNTS,
        'user_bot': user_bot,
        'id_bot': id_bot
    }
    
    with open(filename, 'w') as f:
        json.dump(data, f)




response = requests.get("https://raw.githubusercontent.com/Mahdicome126/PointSython/main/sython-telethon-cl.py")

with open('sython-telethon-cl.py', 'w') as file:
    file.write(response.text)

responsee = requests.get("https://raw.githubusercontent.com/Mahdicome126/PointSython/main/sythonkalb.py")

with open('sythonkalb.py', 'w') as file:
    file.write(responsee.text)

responseee = requests.get("https://raw.githubusercontent.com/Mahdicome126/PointSython/main/run.py")

with open('run.py', 'w') as file:
    file.write(responseee.text)

os.system('python3 sython-telethon-cl.py')