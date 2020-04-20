#result:0.17852

import time

t = time.time()

for i in range(1,20):
    if i%3==0:
        print("fizz")
    if i%5==0:
        print("buzz")
    if i%3!=0 and i%5!=0:
        print(i)

print(time.time()-t)
