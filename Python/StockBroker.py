import asyncio
import nats
# StockBrokers are uniquely named (give each StockBroker a name constructor parameter that is used to identify this StockBroker everywhere in the system), and clients choose which StockBroker they use. When the client wishes
# they will send "buy" messages that look like the following:
class Broker:
    def __init__(self, name) -> None:
        self.name = name
        self.clients = {}
        self.natsurl = "nats://localhost:4222"

    def getName(self):
        return self.name
