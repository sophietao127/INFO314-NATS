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

        nc.subscribe(subject="info314", callback=callback)
        nc.publish(subject="info314", payload=bytes("hello world1", "UTF-8"));

        resp = nc.request("info314", payload=b"test-payload")
        msg = resp.sid()
        print(msg)

        nc.wait(count=1)  # wait for 1 message
        # nc.wait()

    input("Press Enter to terminate")


natsurl = "nats://localhost:4222"
print("Starting Python message producer....")
main(natsurl)