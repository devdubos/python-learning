import asyncio

async def main():
    print("Hello...")
    await asyncio.sleep(2)
    print("...World!")

asyncio.run(main())


import time
async def download_file(file_id, delay):
    print(f"{file_id} started downloading.")
    await asyncio.sleep(delay)
    print(f"{file_id} downloaded!")
    return f"Data from {file_id}"

async def main2():
    start_time = time.time()
    
    results = await asyncio.gather(
        download_file("File 1", 2),
        download_file("File 2", 2),
        download_file("File 3", 2)
    )
    
    print("Results:", results)
    print(f"Total time taken: {time.time() - start_time:.2f} seconds.")

asyncio.run(main2())


async def heavy_calculation():
    print("Background calculation started...")
    await asyncio.sleep(3)
    print("Background calculation finished!")

async def main3():
    task = asyncio.create_task(heavy_calculation())
    
    print("Main code: Performing a quick operation.")
    await asyncio.sleep(1)
    print("Main code: Quick operation finished.")
    
    await task

asyncio.run(main3())