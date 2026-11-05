import asyncio
import time


async def toast():
    print("Toast put in toaster")
    await asyncio.sleep(2)
    print("Toast is ready!")


async def soup():
    print("Soup put on stove")
    await asyncio.sleep(5)
    print("Soup is cooked!")


async def main():
    await asyncio.gather(toast(), soup())


if __name__ == "__main__":
    start_time = time.time()

    asyncio.run(main())

    end_time = time.time()
    print(f"\nTotal cooking time: {end_time - start_time:.2f} seconds")