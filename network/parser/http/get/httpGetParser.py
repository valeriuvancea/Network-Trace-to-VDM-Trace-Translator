from network.parser.baseParser import BaseParser


class HTTPGetParser(BaseParser):
    def parseToImplement(self):
        # Request packet
        if self.packetStringContet[:4] == "'GET":
            self.requestPacketDataExtractor.writeDataIntoVDMTraceFromPacket(
                self.packet, self.packetStringContet)
        # Response packet
        elif "Content-Type: application/json" in self.packetStringContet:
            self.responsePacketDataExtractor.writeDataIntoVDMTraceFromPacket(
                self.packet, self.packetStringContet)
