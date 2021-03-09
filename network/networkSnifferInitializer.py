from network.networkSniffer import NetworkSniffer
from network.packetDataExtractor.http.get.httpGetRequestPacketDataExtractorWithExtraData import HTTPGetRequestPacketDataExtractorWithExtraData
from network.packetDataExtractor.http.get.httpGetResponsePacketDataExtractor import HTTPGetResponsePacketDataExtractor
from network.parser.http.get.httpGetParser import HTTPGetParser


class NetworkSnifferInitializer:
    def __init__(self, ipToListenTo):
        self.httpGetRequestPacketDataExtractor = HTTPGetRequestPacketDataExtractorWithExtraData()
        self.HTTPGetResponsePacketDataExtractor = HTTPGetResponsePacketDataExtractor()
        self.httpGetParser = HTTPGetParser(
            self.httpGetRequestPacketDataExtractor, self.HTTPGetResponsePacketDataExtractor)
        self.networkSniffer = NetworkSniffer(ipToListenTo, self.httpGetParser)
