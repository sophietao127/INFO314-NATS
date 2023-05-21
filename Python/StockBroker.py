from pynats import NATSClient
import xml.dom.minidom
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

    def parseRequest(self, req):
        # check buy or sell
        plan = "sell" if req[8] == 's' else "buy"

        # parse request
        doc = xml.dom.minidom.parseString(req)
        sym = doc.getElementsByTagName(plan)[0].getAttribute('symbol')
        amount = doc.getElementsByTagName(plan)[0].getAttribute('amount')
        print(plan, sym, amount)

    def worker(self, name):
        with NATSClient(self.natsurl) as server:

            def callback(msg):
                print(f"Received a request on Customer'{msg.subject}:")
                req = msg.payload.decode()
                print(f"The request is: {req}")

                # parse request
                self.parseRequest(req)

                server.publish(msg.reply, payload=b"reply firslt!!")

            server.subscribe(
                name, callback=callback, queue="test-queue", max_messages=2
            )
            server.wait(count=1)