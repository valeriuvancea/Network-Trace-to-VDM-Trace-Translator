from network.networkSniffer import NetworkSniffer
from network.packetDataExtractor.http.get.httpGetRequestPacketDataExtractor import HTTPGetRequestPacketDataExtractor
from network.packetDataExtractor.http.get.HTTPGetResponsePacketDataExtractor import HTTPGetResponsePacketDataExtractor
from network.parser.http.get.httpGetParser import HTTPGetParser


class NetworkSnifferInitializer:
    def __init__(self, ipToListenTo):
        self.httpGetRequestPacketDataExtractor = HTTPGetRequestPacketDataExtractor()
        self.HTTPGetResponsePacketDataExtractor = HTTPGetResponsePacketDataExtractor()
        self.httpGetParser = HTTPGetParser(
            self.httpGetRequestPacketDataExtractor, self.HTTPGetResponsePacketDataExtractor)
        self.networkSniffer = NetworkSniffer(ipToListenTo, self.httpGetParser)
