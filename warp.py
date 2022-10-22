import httpx
import json
import datetime
import random
import string
import time
import os
import sys

cooldown = int(os.environ.get('SEC_CD', 20))
referrer = os.environ.get('WARP_ID')

def genString(stringLength):
  try:
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(stringLength))
  except Exception as error:
    sys.stdout.write(error)

def digitString(stringLength):
  try:
    digit = string.digits
    return ''.join((random.choice(digit) for i in range(stringLength)))
  except Exception as error:
    sys.stdout.write(error)

url = f'https://api.cloudflareclient.com/v0a{digitString(3)}/reg'

def run():
  try:
    install_id = genString(22)
    body = {
      "key": "{}=".format(genString(43)),
      "install_id": install_id,
      "fcm_token": "{}:APA91b{}".format(install_id, genString(134)),
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
    req = httpx.post(url,headers=headers,data=data)
    status_code = req.status_code
    return status_code
  except Exception as error:
    return  error

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

  current_time = time.strftime("%H:%M:%S", time.localtime())

  sys.stdout.write(f"Start: ------------------" + "\n")
  sys.stdout.write(f"Time: {current_time}" + "\n")
  sys.stdout.write(f"Referrer: {referrer}" + "\n")
  sys.stdout.write(f"Result: {result}" + "\n")
  sys.stdout.write(f"Total: {added}GB Added, {failed}GB Failed" + "\n")

  sys.stdout.write(f"Cooldown: {cooldown} seconds" + "\n")
  sys.stdout.write(f"End: ------------------" + "\n")
  sys.stdout.flush()

  time.sleep(cooldown)
