from network.parser.baseParser import BaseParser


class JsonParser(BaseParser):
    def __init__(self, packetDataExtractor):
        super().__init__()
        self.packets = []
        self.packetDataExtractor = packetDataExtractor

    def parseToImplement(self):
        if  len(self.packetStringContet) != 0 and self.packet.payload.dst == '255.255.255.255':
            self.packetDataExtractor.writeDataIntoVDMTraceFromPacket(
                    self.packet, self.packetStringContet)