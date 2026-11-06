import asyncio
import time


# async def toast():
#     print("Toast put in toaster")
#     await asyncio.sleep(2)
#     print("Toast is ready!")


# async def soup():
#     print("Soup put on stove")
#     await asyncio.sleep(5)
#     print("Soup is cooked!")


# async def main():
#     await asyncio.gather(toast(), soup())


# if __name__ == "__main__":
#     start_time = time.time()

#     asyncio.run(main())

#     end_time = time.time()
#     print(f"\nTotal cooking time: {end_time - start_time:.2f} seconds")



async def download_image(img_id, download_time):
    print(f"Started downloading image {img_id}")
    await asyncio.sleep(download_time)
    print(f"Image {img_id} downloaded successfully!")

async def main():
    await asyncio.gather(
        download_image(1, 3),
        download_image(2, 1),
        download_image(3, 4)
    )

if __name__ == "__main__":
    start = time.time()
    asyncio.run(main())
    print(f"Total time: {time.time() - start:.2f} seconds")