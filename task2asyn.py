import asyncio
import time
import aiohttp
import json
async def download_file(index: int):
    url = f"https://xkcd.com/{index}/info.0.json"
#     print(f"Begin downloading {url}")
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            content = await response.read()
#             print(f"Finished downloading {url}")
            return content


async def write_to_file(content: bytes):
    filename = "data.json"
    with open(filename, "ab") as file:
#         print("Begin writing")
        file.write(content)
#         print("Finished writing")


async def combining(index: int):
    content = await download_file(index)
    await write_to_file(content)


async def main():
    tasks = []
    for i in range(1,201):
        tasks.append(combining(i))
    await asyncio.gather(*tasks)


s = time.time()
asyncio.run(main())
time_taken = time.time() - s
# with open("data.json",'r') as file:
#     print(file)
print(f"Execution time: {time_taken:0.2f} seconds.")


