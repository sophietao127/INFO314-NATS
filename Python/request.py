from pynats import NATSClient
from pynats import NATSInvalidResponse
import threading
import time

def test_request(nats_plain_url):
    def worker(name):
        with NATSClient(nats_plain_url) as server:

            def callback(msg):
                print(f"Received a request on '{msg.subject}:")
                print(f"The request is: {msg.payload.decode()}")
                server.publish(msg.reply, payload=b"reply firslt!!")

            server.subscribe(
                subject=name, callback=callback, queue="test-queue", max_messages=2
            )
            server.wait(count=1)
            # client.wait()

    t = threading.Thread(target=worker, args=("test-subject",))
    t.start()

    time.sleep(1)

    with NATSClient(nats_plain_url) as client:
        # payload likes a "request"
        resp = client.request("test-subject", payload=b"Request-payload1")
        reply = resp.payload.decode()
        print(reply)

        # resp = client.request("test-subject", payload=b"Request-payload2")
        # print(resp)

    t.join()

if __name__ == '__main__':
    natsurl = "nats://localhost:4222"
    test_request(natsurl)