import asyncio
import time
import aiohttp
import requests
import json
start = time.time()
def downloading(i):
    # print(i)
    url = "https://xkcd.com/{index}/info.0.json"
    url = url.format(index=i)
    content_ = requests.get(url) 
    data = content_.content
    return data
def writing(content):
    filename= "data.json"
    with open(filename,'ab') as file:
        file.write(content)

def combining(i):
    content = downloading(i)
    writing(content)
    
if __name__=="__main__":
    for i in range(1, 201):
        combining(i)
    # with open("data2.json","r") as file:
    #     data = file.read()
    #     print(data)
    time_takenn= time.time()-start
    print("time = ",time_takenn)
