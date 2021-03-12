from network.packetDataExtractor.http.get.httpGetRequestPacketDataExtractor import HTTPGetRequestPacketDataExtractor
from network.networkSniffer import NetworkSniffer
from globalConfiguration import GlobalConfiguration

class MockupHTTPGetRequestPacketDataExtractor(HTTPGetRequestPacketDataExtractor):
    def addAdditionalParametersToData(self):
        keyVaultIp = GlobalConfiguration.dictionary["keyVaultIp"]
        self.data["isForKeyVault"] = True if self.destination == keyVaultIp else False
        self.data["isBetweenControllers"] = True if self.destination != keyVaultIp and self.source != keyVaultIp else False
