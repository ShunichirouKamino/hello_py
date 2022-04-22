import tqdm as td
import time


def main():
    print("Hello! Progress!")
    for i in td(range(10)):
        time.sleep(1)
