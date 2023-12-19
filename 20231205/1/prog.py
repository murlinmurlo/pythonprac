import asyncio

event = asyncio.Event()

async def writer(order, delay):
    i = 0
    while True:
        await asyncio.sleep(delay)
        await order.put(f'{i}_{delay}')
        if event.is_set():
            break
        i += 1


async def stacker(order, stack):
    while True:
        await asyncio.sleep(0)
        item = await order.get()
        await stack.put(item)
        if event.is_set():
            break


async def reader(stack, num, delay):
    while num:
        await asyncio.sleep(delay)
        while not stack:
            await asyncio.sleep(0)
        val = await stack.get()
        print(val)
        num -= 1
    event.set()


async def main():
    d1, d2, d3, num = eval(input())
    order = asyncio.Queue()
    stack = asyncio.LifoQueue()
    await asyncio.gather(
        writer(order, d1),
        writer(order, d2),
        stacker(order, stack),
        reader(stack, num, d3)
    )


asyncio.run(main())
