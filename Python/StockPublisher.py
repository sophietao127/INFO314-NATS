from pynats import NATSClient
import sys

"""
connect to the NATS server and spin up three "stock markets":
"""
def main(natsurl):
    with NATSClient(url=natsurl) as nc:
        nc.connect()
        nc.publish(subject="subject", payload=bytes("hello world", "UTF-8"));
        print("Exiting main...")

natsurl = "nats://localhost:4222"
print("Starting Python message producer....")
main(natsurl)
