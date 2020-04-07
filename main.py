import requests
import time
from datetime import datetime

ISLAND_URL = 'http://api.turnip.exchange/islands'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


def is_island_eligible(island):
    queued = island['queued']
    return queued < 50 and island['turnipPrice'] > 400


def find_new_islands(islands):
    now = datetime.now().strftime("%H:%M:%S")
    found_island = False
    for island in islands:
        if is_island_eligible(island):
            print('[{time}] Price: {price}. URL: https://turnip.exchange/island/{code}.'.format(
                time=now, price=island['turnipPrice'], code=island['turnipCode']))
            print('\a')
            found_island = True
    if not found_island:
        print('[{time}] No eligible island found.'.format(time=now))

while True:
    now = datetime.now().strftime("%H:%M:%S")
    data = requests.get(ISLAND_URL, headers=HEADERS).json()
    if (data['success'] == False):
        print('[{time}] Request failed.'.format(time=now))
    else:
        find_new_islands(data['islands'])
    time.sleep(180)
