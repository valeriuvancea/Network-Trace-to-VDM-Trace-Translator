from scapy.layers.inet import UDP
from network.packetDataExtractor.basePacketDataExtractor import BasePacketDataExtractor
import json

class JsonPacketDataExtractor(BasePacketDataExtractor):
    def getDataFromPacket(self):
        try:
            if len(self.packetStringContent) != 0 and self.packet.haslayer(UDP):
                self.data = json.loads(self.packetStringContent[1:-1])
                self.data["isForKeyVault"] = True
        except:
            pass


