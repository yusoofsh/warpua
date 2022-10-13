import httpx
import json
import datetime
import random
import string
import time
import os
import sys

referrer = (os.environ.get('WARP_ID'))

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
      "tos": datetime.datetime.now().isoformat()[:-3] + "+02:00",
      "type": "Android",
      "locale": "es_ES"
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

g = 0
b = 0

while True:
  os.system('cls' if os.name == 'nt' else 'clear')

  result = run()

  if result == 200:
    g += 1
  else:
    b += 1

  sys.stdout.write("" + "\n")
  sys.stdout.write(f"Referrer: {referrer}" + "\n")
  sys.stdout.write(f"Result: {result}" + "\n")
  sys.stdout.write(f"Total: {g}GB Added, {b}GB Failed" + "\n")

  sys.stdout.write(f"Cooldown: 10 seconds" + "\n")
  time.sleep(10)

  sys.stdout.flush()
