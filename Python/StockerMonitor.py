from pynats import NATSClient
import sys

"""
Previously: Subscribe.py
Receive message from StockPublisher through NATS Server

Run commands Line: "MSFT", "AMZN", "BLIZ"

look which markets they are belongs to
"""
# sys.argv[0] is StockerMonitor.py
print("the two input variables are: ", sys.argv[1], sys.argv[2])



class StockMonitor:
    def __init__(self) -> None:
        """
        get the input of the market name.
        """
        pass

    # creat and write the price log file for each symbols
    # with each line consisting of
    # 1. the timestamp a message is received
    # 2. the adjustment for that message
    # 3. the current price of the stock after adjustment.
    def priceLogs(symbols):
        pass

    def callback(self, msg):
        print("Received a message with subject: " + msg.subject)

    def main(self, natsurl):
        with NATSClient(url=natsurl) as nc:
            nc.connect()

            nc.subscribe(subject="market.*.*", callback=self.callback)

            nc.wait(count = 1)

        input("Press Enter to terminate")


natsurl = "nats://localhost:4222"
print("Starting Python message producer....")
# # call the StockerMonitor class
# # main(natsurl)
# # may be we don't need to build a class for stockmonitor
