import asyncio
import time



# async def fetch_data(seconds):
#     print(f"Start request on {seconds}")
#     await asyncio.sleep(seconds)
#     print(f"request complete on {seconds}")
  
# async def main():
#     start = time.perf_counter()
#     task1 = asyncio.create_task(fetch_data(2))
#     task2 = asyncio.create_task(fetch_data(4))
#     task3 = asyncio.create_task(fetch_data(3))
#     await task1
#     await task2
#     await task3

#     print(time.perf_counter() - start) 
    

# asyncio.run(main())


# async def fetch_data(seconds): 
#     print(f"Start request on {seconds}")
#     await asyncio.sleep(seconds)
#     print(f"request complete on {seconds}")
  
# async def main():
#     start = time.perf_counter()

#     await asyncio.gather(fetch_data(2),fetch_data(3),fetch_data(4))

#     print(time.perf_counter() - start) 
    

# asyncio.run(main())


# async def fetch_data(seconds):
#     print(f"Start request on {seconds}")
#     await asyncio.to_thread(time.sleep, seconds)
#     print(f"request complete on {seconds}")
  
# async def main():
#     start = time.perf_counter()

#     await asyncio.gather(fetch_data(2),fetch_data(3),fetch_data(4))

#     print(time.perf_counter() - start) 
    

# asyncio.run(main())


import random
import aiofiles


# async def create_request_start(city, count):
#     print("Start request: complete")
#     await asyncio.sleep(random.uniform(1, 10))
#     print(f"Mettadata taken:in {city} have {count} stuffs")

# async def main():

#     async with aiofiles.open('day_62/stocks.txt','r', encoding = 'utf-8') as file:
#         task = []
#         async for line in file:
#             data = line.strip().split(',')
#             if len(data)<2:
#                 continue
#             city = data[0]
#             count = int(data[1])
#             coroutine = create_request_start(city,count)
#             task.append(coroutine)
#     await asyncio.gather(*task)
    

# asyncio.run(main())

async def user_coroutine(name, email,):
    print("Request status: complete")
    print(f"User's mettadata:Name:{name}, email:{email}")


async def telelgram_coroutine(name, nick_tg):
    print("Request status: complete")
    print(f"User's mettadata telegram:Name:{name}, tg. nick:{nick_tg}") 

async def incapsulation_coroutine(name, email, nick_tg):
    user_time = random.uniform(1,5)
    await asyncio.sleep(user_time)
    await user_coroutine(name,email)
    await telelgram_coroutine(name,nick_tg)
    

async def main():
    async with aiofiles.open("day_62/users.txt",'r', encoding="utf-8") as file:
        task = []
        async for line in file:    
            data = line.strip().split(',')
            if len(data) < 3:
                continue
            name = data[0]
            email = data[1]
            nick_tg = data[2]
            coroutine = (incapsulation_coroutine(name,email,nick_tg))
            task.append(coroutine)
        await asyncio.gather(*task)



asyncio.run(main())

