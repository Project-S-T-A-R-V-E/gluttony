import random
import asyncio

theValue = 0

async def update_value():
    global theValue
    while True:
        theValue = random.randint(1, 100)
        await asyncio.sleep(5)


update_value()
async def print_value():
    global theValue
    while True:
        print(f"Updated value: {theValue}")
        await asyncio.sleep(.2)

# Run both coroutines concurrently
async def main():
    await asyncio.gather(update_value(), print_value())

asyncio.run(main())