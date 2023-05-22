import time
import asyncio

def print_now():
    print(time.time())
async def print3():
   for i in range (3):
       print_now()
       await asyncio.sleep(0.1)
coro1 = print3()
coro2 = print3()
print(type(print3))
print(type(coro1))

#asyncio.run(print3)

#this will raise an error as coroutines are awaitable but func are not
asyncio.run(coro1)
asyncio.run(coro2)
asyncio.run(coro1)  
# coro could only be use once 