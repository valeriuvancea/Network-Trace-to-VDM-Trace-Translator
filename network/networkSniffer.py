from scapy.all import *
from globalConfiguration import GlobalConfiguration


class NetworkSniffer:
    def __init__(self):
        self.parsers = []

    def addParser(self, parser):
        self.parsers.append(parser)

    def startSniffing(self):
        sniff(filter=GlobalConfiguration.scapyFilter, prn=self.checkPackets)

    def checkPackets(self, packet):
        for parser in self.parsers:
            parser.parse(packet)
       
