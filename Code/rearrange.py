import random
import sys

class Rearrange():
    def __init__(self, params):
        for val in range(len(params) - 1, 0, -1):
            j = random.randint(0, val + 1)
            #print(val, j , params)
            params[val], params[j] = params[j], params[val]

        print(params)

if __name__ == "__main__":
    params = sys.argv[1:]
    Rearrange(params)