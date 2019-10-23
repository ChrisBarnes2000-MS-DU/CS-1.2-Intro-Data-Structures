import random
import sys

class rearrange():
    params = sys.argv[1:]
    
    for val in range(len(params)-1,0, -1):
        j = random.randint(0, val+1)
        params[val], params[j] = params[j], params[val]

    print(params)
