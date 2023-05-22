import asyncio
import time
def print_now():
    print(time.time()) 

async def keep_printing(name: str=" "):
    while True:
        print(name,end=" ")
        print_now()
        await asyncio.sleep(0.5)
#manually stopping raises long tracback so wraping it up in a async main function
async def async_main():
    try:
        await asyncio.wait_for(keep_printing("hey"),10)
    except :
        print("times up")   
asyncio.run(async_main())