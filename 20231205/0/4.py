import asyncio

async def main(*args):
    res = await asyncio.gather(*(squarer(arg) for arg in args))
    res = await asyncio.gather(*(doubler(arg) for arg in args))
    print(*res)

async def squarer(x):
    return x*x

async def doubler(x):
    return x+x



#asyncio.run(main(*args))

