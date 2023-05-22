import asyncio
import time
def print_now():
    print(time.time()) 
    
async def keep_printing(name: str=" "):
    while True:
        print(name,end=" ")
        print_now()
        await asyncio.sleep(0.5)

#await x means do not proceed with this coro until x is completed
async def main():
    await keep_printing("first")
    await keep_printing("second")
    await keep_printing("third")
    
#to run non sequentially we use gather

async def main2():
    await asyncio.gather(
    keep_printing("first"),
    keep_printing("second"),
    keep_printing("third")
    )
asyncio.run(main())
asyncio.run(main2())