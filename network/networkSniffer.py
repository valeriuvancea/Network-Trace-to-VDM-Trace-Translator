from scapy.all import *


class NetworkSniffer:
    def __init__(self, ipToListenTo, httpGetParser):
        self.httpGetParser = httpGetParser
        sniff(filter="host " + ipToListenTo + " or dst " +
              ipToListenTo, prn=self.checkPackets)

    def checkPackets(self, packet):
        stringPacket = str(packet)
        if stringPacket.find('GET'):
            self.httpGetParser.parse(packet)
