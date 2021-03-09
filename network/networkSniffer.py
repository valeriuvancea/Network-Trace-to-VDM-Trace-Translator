from scapy.all import *


class NetworkSniffer:
    ipToListenTo = "127.0.0.1"
    def __init__(self, ipToListenTo, httpGetParser):
        NetworkSniffer.ipToListenTo = ipToListenTo
        self.httpGetParser = httpGetParser
        sniff(filter="host " + ipToListenTo + " or dst " +
              ipToListenTo, prn=self.checkPackets)

    def checkPackets(self, packet):
        stringPacket = str(packet)
        if stringPacket.find('GET'):
            self.httpGetParser.parse(packet)
