import asyncio
from time import strftime

async def late(delay, msg):
    print(f"> Start {msg}")
    await asyncio.sleep(delay)
    print(msg)
    print(msg)

async def main():

    task3 = asyncio.create_task(late(3, "Three"))
    task4 = asyncio.create_task(late(4, "Four"))
    await(task3)
    print(f"> {strftime('%X')}")
    await(task4)
    print(f"> {strftime('%X')}")

asyncio.run(main())

