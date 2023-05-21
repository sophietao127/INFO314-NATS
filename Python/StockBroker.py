from pynats import NATSClient
# StockBrokers are uniquely named (give each StockBroker a name constructor parameter that is used to identify this StockBroker everywhere in the system), and clients choose which StockBroker they use. When the client wishes
# they will send "buy" messages that look like the following:
class Broker:
    def __init__(self, name) -> None:
        self.name = name
        self.clients = {}
        self.natsurl = "nats://localhost:4222"

        # with NATSClient(self.natsurl) as server:
        #     # keep waiting new customer
        #     pass

    def getName(self):
        return self.name

    def worker(self, name):
        with NATSClient(self.natsurl) as server:

            def callback(msg):
                print(f"Received a request on Customer'{msg.subject}:")
                print(f"The request is: {msg.payload.decode()}")
                server.publish(msg.reply, payload=b"reply firslt!!")

            server.subscribe(
                name, callback=callback, queue="test-queue", max_messages=2
            )
            server.wait(count=1)