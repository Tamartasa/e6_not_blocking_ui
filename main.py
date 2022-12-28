import time
from concurrent.futures import ThreadPoolExecutor
import requests


def counter(counter: float):

    print(f"{round(counter, 1)} seconds left")
    with ThreadPoolExecutor() as executor:
        futures = []
        while round(counter, 1) > 0.1:
            counter = round(counter, 1) - 0.1
            time.sleep(0.1)
            if round(counter, 1) == int(counter):
                executor.submit(get_quote)
            print(f"{round(counter, 1)} seconds left")
    print('Done!')

def get_quote():
    response = requests.get("https://api.kanye.rest")
    if response.status_code < 400:
        print(response.json()['quote'])
    else:
        raise Exception(f"Received response code {response.status_code}")

counter(2.5)



