from tqdm import tqdm
import numpy as np
import time


def main():
    print("Hello! Progress!")
    x = np.array([1, 2, 3])
    print(x)

    for i in tqdm(range(10)):
        time.sleep(1)
