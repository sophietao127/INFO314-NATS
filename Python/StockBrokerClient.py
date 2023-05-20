from pynats import NATSClient
import time
import StockBroker

# each client will have a portfolio of stocks and a "strategy" as to when to buy or sell particular stocks.
# StockBrokers are uniquely named (give each StockBroker a name constructor parameter that is used to identify this StockBroker everywhere in the system), and clients choose which StockBroker they use. When the client wishes
# they will send "buy" messages that look like the following:
# nats: request(), msgpack()


class StockerBrokerClient:
    def __init__(self, name, broker) -> None:
        self.name = name
        self.broker = broker    # an instance of a StockBroker
        self.portfolio = 'portfolio-' + name + '.xml'
        self.strategy = 'strategy-' + name + '.xml'
        self.natsurl = "nats://localhost:4222"

        with NATSClient(url=self.natsurl) as nc:
            nc.connect()
            print("connected")

            # just test 1 symbol
            nc.subscribe(subject="GE", callback=self.callback)

            nc.wait()

        input("Press Enter to terminate")

    def callback(self, msg):
        print("Received a message with subject: " + msg.subject)
        content = msg.payload.decode()
        self.getSymbol()
        # print(content)

    def getSymbol(self):
        # open portfolio.xml to get all symbols - return the list
        symbols = []
        filename = self.portfolio
        # f = open(filename, "r")
        with open(filename) as f:
            lines = f.readlines()
            for line in lines:
                print(line.strip())
            f.close()

        return symbols

    def getBroker(self):
        return self.broker

    def checkThreshold(self):
        pass

    def updatePortfolio(self):
        filename = self.portfolio
        # read and update the file


if __name__ == "__main__":
    # broker_alex =StockBroker("Alex")
    client_mary = StockerBrokerClient("Mary", "broker1")