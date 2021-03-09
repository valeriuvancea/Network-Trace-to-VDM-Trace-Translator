from network.packetDataExtractor.http.get.httpGetRequestPacketDataExtractor import HTTPGetRequestPacketDataExtractor
from network.networkSniffer import NetworkSniffer

class HTTPGetRequestPacketDataExtractorWithExtraData(HTTPGetRequestPacketDataExtractor):
    def addAdditionalParametersToData(self):
        self.data["isForKeyVault"] = True if self.destination == NetworkSniffer.ipToListenTo else False
        self.data["isBetweenControllers"] = True if self.destination != NetworkSniffer.ipToListenTo and self.source != NetworkSniffer.ipToListenTo else False
