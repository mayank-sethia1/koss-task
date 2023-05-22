import asyncio
import time
loop=asyncio.get_event_loop()
start = time.time()
def print_now():
    print(time.time()-start)
def trampoline(name: str=" ")    :
    print(name,end="")
    print_now()
    loop.call_later(0.5,trampoline,name)
    
def hog():
    sum=0
    for i in range (10000):
        for j in range(10000):
            sum+=j
    return sum  
loop.call_soon(trampoline)
loop.call_later(12,loop.stop)
loop.call_later(6,hog)
loop.run_forever()