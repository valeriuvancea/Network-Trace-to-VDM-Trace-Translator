from network.networkSniffer import NetworkSniffer
from network.packetDataExtractor.http.get.mockupHTTPGetRequestPacketDataExtractor import MockupHTTPGetRequestPacketDataExtractor
from network.packetDataExtractor.http.get.httpGetResponsePacketDataExtractor import HTTPGetResponsePacketDataExtractor
from network.packetDataExtractor.jsonPacketDataExtractor import JsonPacketDataExtractor
from network.parser.http.get.httpGetParser import HTTPGetParser
from network.parser.jsonParser import JsonParser


class NetworkSnifferInitializer:
    def __init__(self):
        self.networkSniffer = NetworkSniffer()
        self.addHTTPGetParser()
        self.networkSniffer.startSniffing()

    def addHTTPGetParser(self):
        httpGetRequestPacketDataExtractor = MockupHTTPGetRequestPacketDataExtractor()
        httpGetResponsePacketDataExtractor = HTTPGetResponsePacketDataExtractor()
        httpGetParser = HTTPGetParser(
            httpGetRequestPacketDataExtractor, httpGetResponsePacketDataExtractor)
        self.networkSniffer.addParser(httpGetParser)

        jsonPacketDataExtractor = JsonPacketDataExtractor()
        jsonParser = JsonParser(jsonPacketDataExtractor)
        self.networkSniffer.addParser(jsonParser)