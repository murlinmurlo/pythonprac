import asyncio

async def snd():
    print("snd: generated evsnd")
    await asyncio.sleep(1)
    return "evsnd"

async def mid1():
    event = await snd()
    print("mid1: received", event)
    print("mid1: generated evmid1")
    await asyncio.sleep(1)
    return "evmid1"

async def mid2():
    event = await snd()
    print("mid2: received", event)
    print("mid2: generated evmid2")
    await asyncio.sleep(1)
    return "evmid2"

async def rcv():
    event1 = await mid1()
    event2 = await mid2()
    print("rcv: received", event1, "and", event2)

asyncio.run(rcv())
