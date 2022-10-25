import json
import datetime
import random
import string
import time
import os
import sys
import httpx

cooldown = int(os.environ.get('SEC_CD', 20))
referrer = os.environ.get('WARP_ID')


def generate_string(string_length):
    try:
        letters = string.ascii_letters + string.digits
        return ''.join(random.choice(letters) for i in range(string_length))
    except Exception as error:
        sys.stdout.write(error)


def generate_digit(string_length):
    try:
        digit = string.digits
        return ''.join((random.choice(digit) for i in range(string_length)))
    except Exception as error:
        sys.stdout.write(error)


url = f'https://api.cloudflareclient.com/v0a{generate_digit(3)}/reg'


def run():
    try:
        install_id = generate_string(22)
        body = {
            "key": "{}=".format(generate_string(43)),
            "install_id": install_id,
            "fcm_token": "{}:APA91b{}".format(install_id, generate_string(134)),
            "referrer": referrer,
            "warp_enabled": False,
            "tos": datetime.datetime.now().isoformat()[:-5] + "-05:00",
            "type": "Android",
            "locale": "en_US"
        }
        data = json.dumps(body).encode('utf8')
        headers = {
            'Content-Type': 'application/json; charset=UTF-8',
            'Host': 'api.cloudflareclient.com',
            'Connection': 'Keep-Alive',
            'Accept-Encoding': 'gzip',
            'User-Agent': 'okhttp/3.12.1'
        }
        req = httpx.post(url, headers=headers, data=data)
        status_code = req.status_code
        return status_code
    except Exception as error:
        return error


added = 0
failed = 0

while True:
    os.system('cls' if os.name == 'nt' else 'clear')

    result = run()

    if result == 200:
        added += 1
        cooldown = int(os.environ.get('SEC_CD', 20))
    elif result == 429:
        failed += 1
        cooldown = 30
    else:
        failed += 1

    current_date = datetime.date.today()
    current_time = time.strftime("%H:%M:%S", time.localtime())

    sys.stdout.write("Start: ------------------" + "\n")
    sys.stdout.write(f"UTC: {current_date} {current_time}" + "\n")
    sys.stdout.write(f"Referrer: {referrer}" + "\n")
    sys.stdout.write(f"Result: {result}" + "\n")
    sys.stdout.write(f"Total: {added}GB Added, {failed}GB Failed" + "\n")

    sys.stdout.write(f"Cooldown: {cooldown} seconds" + "\n")
    sys.stdout.write("End: ------------------" + "\n")
    sys.stdout.flush()

    time.sleep(cooldown)
