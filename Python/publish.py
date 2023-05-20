from pynats import NATSClient
import sys

def main(natsurl):
    with NATSClient(url=natsurl) as nc:
        nc.connect()

        # Publish a message
        nc.publish(subject="info314", payload=bytes("hello world1", "UTF-8"));
        nc.publish(subject="info314", payload=bytes("hello world2", "UTF-8"));
        print("Exiting main...")

natsurl = "nats://localhost:4222"
print("Starting Python message producer....")
main(natsurl)