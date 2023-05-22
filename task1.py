import asyncio
import time
import aiohttp
async def get_response(el):
    async with aiohttp.ClientSession() as session:
            async with session.get("https://reqres.in/api/users?page{el}") as response:              
                response_= await response.text()
                

async def main():
    obj1 = get_response(1)
    obj2 = get_response(2)
    obj3 = get_response(3)

    start = time.time()

    await asyncio.gather(obj1, obj2, obj3)

    time_taken = time.time() - start
    print('Time Taken in asynchronously {0}'.format(time_taken))
    obj4 = get_response(1)
    obj5 = get_response(2)
    obj6 = get_response(3)
    start = time.time()

    await obj4
    await obj5
    await obj6

    time_taken = time.time() - start
    print('Time Taken in synchronously {0}'.format(time_taken))

asyncio.run(main())