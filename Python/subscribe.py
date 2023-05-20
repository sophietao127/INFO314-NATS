from pynats import NATSClient
import sys

# Subscribe
def callback(msg):
    print("Received a message with subject: " + msg.subject)
    content = msg.payload.decode()
    print(content)
    # print(f"Received a message with subject {msg.subject}: {msg}")

def main(natsurl):
    with NATSClient(url=natsurl) as nc:
        nc.connect()
        print("connected")

        nc.subscribe(subject="*", callback=callback)

        # nc.wait(count=2)  # wait for 1 message
        nc.wait()

    input("Press Enter to terminate")


natsurl = "nats://localhost:4222"
print("Starting Python message producer....")
main(natsurl)