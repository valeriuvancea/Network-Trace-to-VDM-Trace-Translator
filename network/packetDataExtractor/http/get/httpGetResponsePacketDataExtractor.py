from network.packetDataExtractor.basePacketDataExtractor import BasePacketDataExtractor
import json


class HTTPGetResponsePacketDataExtractor(BasePacketDataExtractor):
    def getDataFromPacket(self):
        packetLines = self.packetStringContent.split(r"\r\n")
        lastPacketLine = packetLines[-1].replace('\\n', '')
        # The response JSON data is on the last line of the HTTP packet and it has an extra "/" character at the end. The following line removes it and loads the JSON
        try:
            self.data = json.loads(lastPacketLine)
        except:
            pass
