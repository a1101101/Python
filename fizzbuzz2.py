#https://en.wikipedia.org/wiki/Fizz_buzz
#result:0.16930

import time

t = time.time()

for n in range(1, 20):
    response = ""

    if n % 3 == 0:
        response += "Fizz"
    if n % 5 == 0:
        response += "Buzz"

    print(response or n)

print(time.time()-t)
