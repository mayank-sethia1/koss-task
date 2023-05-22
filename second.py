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
loop.call_soon(trampoline)
loop.call_later(8,loop.stop)
loop.run_forever()