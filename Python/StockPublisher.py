from pynats import NATSClient
import sys
from StockMarket import StockMarket
import threading

"""
connect to the NATS server and spin up three "stock markets":
publish message from StockMarket

"""
def publish(symbol, adjustment, price):
    print("PUBLISH: " + str(symbol) + " " + str(adjustment) + " " + str(price))


def main(natsurl):
    # get the input url

    print("Starting stock publisher....")
    sm1 = StockMarket(publish, ["AMZN", "GOOG", "MSFT"])
    sm2 = StockMarket(publish, ["GE", "GMC", "FORD"])
    threading.Thread(target=sm1.run).start()
    threading.Thread(target=sm2.run).start()
    print("Press Ctrl-C to terminate")

    with NATSClient(url=natsurl) as nc:
        nc.connect()
        nc.publish(subject="subject", payload=bytes("hello world", "UTF-8"));
        print("Exiting main...")

natsurl = "nats://localhost:4222"
print("Starting Python message producer....")
main(natsurl)