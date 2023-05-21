from pynats import NATSClient
import xml.etree.ElementTree as ET
import time
import StockBroker
import threading

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
        self.threshold = {}

        self.symbols_num = self.getSymbols()  #{'MSFT': '500', 'AMZN': '500', 'GOOG': '500'}
        # print(self.symbols_num)
        self.market_price = None     # for a specific symbol while runing the for loop below

        self.getThreshold()
        # with NATSClient(url=self.natsurl) as nc:
        #     nc.connect()
        #     print("Check the StockPublisher:")

        #     for symbol in self.symbols_num.keys():
        #         nc.subscribe(subject=symbol, callback=self.callback)

        #     nc.wait()

        # input("Press Enter to terminate")

    def callback(self, msg):
        print("Received a message with subject: " + msg.subject)
        content = msg.payload.decode()
        xml_data = content

        myroot = ET.fromstring(xml_data)   # parse xml file
        symbol = myroot[0][0].text
        price = myroot[0][2].text
        print(symbol, price)
        self.market_price = price

        # check the strategy - call checkTreshold()

    def getSymbols(self):
        # open portfolio.xml to get all symbols - return the list
        symbols = {}
        filename = self.portfolio
        tree = ET.parse(filename)
        root = tree.getroot()
        # print(root.tag)
        for child in root:
            symbol, num = child.attrib['symbol'], child.text
            symbols[symbol] = num
        return symbols

    def getThreshold(self):
        # filename = self.strategy
        tree = ET.parse("strategy-Mary.xml")
        root = tree.getroot()

        for children in root:
            for child in children:
                print(child.tag, child.text)

            # symbol, num = child.attrib['symbol'], child.text




    def checkThreshold(self):
        pass

    def updatePortfolio(self):
        filename = self.portfolio
        # read and update the file

    def workWithBroker(self, req = None):
        """
        Received a request on 'test-subject:
        The request is: <order><buy symbol='MSFT' amount='40' /></order>
        reply firslt!!
        """
        req = b"<order><buy symbol='MSFT' amount='40' /></order>"
        broker = self.broker

        def worker(name):
            broker.worker(name)

        # run thread to call the StockBroker
        t = threading.Thread(target=worker, args=(self.name,))
        t.start()

        time.sleep(1)

        with NATSClient(self.natsurl) as client:
        # payload likes a "request"
            resp = client.request(self.name, payload=req)
            reply = resp.payload.decode()
            print(reply)

        t.join()


if __name__ == "__main__":
    broker_alex =StockBroker.Broker("Alex")
    client_mary = StockerBrokerClient("Mary", broker_alex)
    # client_mary.workWithBroker();