from network.packetDataExtractor.basePacketDataExtractor import BasePacketDataExtractor
import json

class JsonPacketDataExtractor(BasePacketDataExtractor):
    def getDataFromPacket(self):
        try:
            self.data = json.load(self.packetStringContent)
        except:
            pass


