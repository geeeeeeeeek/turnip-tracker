import requests
import time
from datetime import datetime

ISLAND_URL = 'http://api.turnip.exchange/islands'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Safari/605.1.15'}
COOKIES = {
    '__cfduid': 'db1eb4357d63476a501dfd1f76aabb4801586213874',
    '_ga_ccuid_v2': 'QZ4CfTwZ5%2B5MIB4UTteY1Q%3D%3D%3A%3Atqrs%2FxGGlTJqOpWSIpLP779obLM2vPSA%2BLvLa0eZwuAK%2BD7aNVO9Aq2lTDojX8daeV%2FBY%2BXYKJPbb03dwo7h%2BPpx%2Bn79l2UlBLki4JLCwVudGcwtnMBqf1n7AlqlVITbvR7b90s43WDj%2F8%2F5o95cTOOPGyiY7NmB%2Feqd41OMT%2FDgMbLq3ElXgct26V47Wup7VkbXR25colMIpB%2Bmh%2FjBJs2%2BFvU1bmeB07Uv4AcBpv%2BVfzIwDPpd6jf48TcF4GvpKKgeZMiUzyGezMYuQKsX2TjIpASDgOyQqvssxyJyc%2BP3anaYIsB6cV0iCvjFxy%2BChN3Gbfftn0hvfKb7dAZjRdP54Thex3SPsBdYitrEGG6f4drVUqWFRo8RryI2q7hM8F2LG3BCptmcdMd5y6nUqkJZteIvYTdo0rLkmdJGkwhKwTlmfn%2BDxf1fz9wf07DD9MZbN2bc4crHJvzoCuFOM5t2K4Ic1ZtPcmrQqGc5kVgOogBMKp9u5m7VrPWoh5sJHqaI7b8h0K2LZGf7mGXws0qZ%2BrFV8m0WQWC0sluyvefwdLm9faZ6JLyhtCWy05Cq6QegJ%2FbLokH84pyhSfU1sXwv78s1BeOhMaOzO0CUg5PhawFfvegd4fS%2BGx%2FEKtY%2FUbFTC69DAa4og3%2Fk13h4uRr95mNhGPTGVPEhqP0BsWljKvZjGlWQ9w3HC2K9Mu8v',
    'adbe_omni_usr': '840c1450-a7b4-5285-90bf-a0c5afec6b91',
}

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
    data = requests.get(ISLAND_URL, headers=HEADERS, cookies=COOKIES).json()
    if (data['success'] == False):
        print('[{time}] Request failed.'.format(time=now))
    else:
        find_new_islands(data['islands'])
    time.sleep(180)
