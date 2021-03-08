from network.packetDataExtractor.basePacketDataExtractor import BasePacketDataExtractor
import json


class HTTPGetResponsePacketDataExtractor(BasePacketDataExtractor):
    def getDataFromPacket(self):
        packetLines = self.packetStringContent.split(r"\r\n")
        lastPacketLine = packetLines[-1]
        # The response JSON data is on the last line of the HTTP packet and it has an extra "/" character at the end. The following line removes it and loads the JSON
        self.data = json.loads(lastPacketLine[0:-1])
