from pynats import NATSClient
import sys
import xml.etree.ElementTree as ET

def callback(msg):
    print("Received a message with subject: " + msg.subject)
    content = msg.payload.decode()
    print(content)
    # xml_data = content

    # myroot = ET.fromstring(xml_data)
    # timestamp = myroot.attrib['sent']
    # symbol = myroot[0][0].text
    # adjustment = myroot[0][1].text
    # price = myroot[0][2].text

    # print("timestamp: ", timestamp)
    # print(symbol, adjustment, price)

    # # write in a file - create price log for current symbol
    # filename = symbol + '.txt'
    # f = open(filename,"a")
    # f.write("Timestamp: {t}, Adjustment: {a}, Current Price: {p}\r\n".format(t=timestamp, a=adjustment, p=price))
    # f.close()


def connect(natsurl):
    with NATSClient(url=natsurl) as nc:
        nc.connect()
        print("SEC connected")
        nc.subscribe(subject=">", callback=callback)
        nc.wait()

    input("Press Enter to terminate")


if __name__ == "__main__":
    natsurl = "nats://localhost:4222"
    print("Starting SEC Checking...")
    connect(natsurl)