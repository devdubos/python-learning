import asyncio


async def fetch_data():
    print("Start request")
    await asyncio.sleep(2)
    print("Request complete")

    return 45



async def main():
    print(fetch_data())
    print(await fetch_data())

asyncio.run(main())

