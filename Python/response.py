import nats
import asyncio

async def main():
  nc = await nats.connect("nats://localhost:4222")

  try:
    response = await nc.request("help", b'help me', timeout=0.5)

    print("Received response: {message}".format(
          message=response.data.decode()))
  except TimeoutError:
    print("Request timed out")

if __name__ == '__main__':
    asyncio.run(main())