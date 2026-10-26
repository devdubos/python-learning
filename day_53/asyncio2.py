import asyncio
import time


async def fetch_data():
    print("Start fetching data...")
    await asyncio.sleep(2)
    print("Data fetched successfully!")
    return {"status": "success", "data": "some_data"}

async def main():
    result = await fetch_data()
    print(f"Result in main: {result}")

asyncio.run(main())




async def download_file(file_name, duration):
    print(f"Started downloading {file_name}...")
    await asyncio.sleep(duration)
    print(f"Finished downloading {file_name}.")

async def main():
    start_time = time.time()
    
    await download_file("video.mp4", 2)
    await download_file("image.jpg", 1)
    
    end_time = time.time()
    print(f"Total execution time: {end_time - start_time:.2f} seconds")

asyncio.run(main())



async def download_file(file_name, duration):
    print(f"Started downloading {file_name}...")
    await asyncio.sleep(duration)
    print(f"Finished downloading {file_name}.")
    return f"{file_name} data"

async def main():
    start_time = time.time()
    
    results = await asyncio.gather(
        download_file("video.mp4", 2),
        download_file("image.jpg", 1)
    )
    
    end_time = time.time()
    print(f"Downloaded contents: {results}")
    print(f"Total execution time: {end_time - start_time:.2f} seconds")

asyncio.run(main())





async def send_email(user_email):
    print(f"Sending email alert to {user_email}...")
    await asyncio.sleep(3)
    print(f"Email sent to {user_email}!")

async def main():
    print("Main process started.")
    
    email_task = asyncio.create_task(send_email("user@example.com"))
    
    print("Doing other heavy work in main...")
    await asyncio.sleep(1)
    print("Main process finished its immediate work.")
    
    await email_task

asyncio.run(main())