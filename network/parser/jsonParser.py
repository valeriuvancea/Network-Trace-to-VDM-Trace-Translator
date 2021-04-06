from network.parser.baseParser import BaseParser


class JsonParser(BaseParser):
    def __init__(self, packetDataExtractor):
        super().__init__()
        self.packets = []
        self.packetDataExtractor = packetDataExtractor

    def parseToImplement(self):
        self.packetDataExtractor.writeDataIntoVDMTraceFromPacket(
                self.packet, self.packetStringContet)