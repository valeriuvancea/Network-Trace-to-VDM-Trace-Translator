from network.networkSniffer import NetworkSniffer
from network.packetDataExtractor.http.get.mockupHTTPGetRequestPacketDataExtractor import MockupHTTPGetRequestPacketDataExtractor
from network.packetDataExtractor.http.get.httpGetResponsePacketDataExtractor import HTTPGetResponsePacketDataExtractor
from network.parser.http.get.httpGetParser import HTTPGetParser


class NetworkSnifferInitializer:
    def __init__(self):
        httpGetRequestPacketDataExtractor = MockupHTTPGetRequestPacketDataExtractor()
        httpGetResponsePacketDataExtractor = HTTPGetResponsePacketDataExtractor()
        httpGetParser = HTTPGetParser(
            httpGetRequestPacketDataExtractor, httpGetResponsePacketDataExtractor)
        self.networkSniffer = NetworkSniffer(httpGetParser)
