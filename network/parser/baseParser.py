class BaseParser:
    lastPacketContent = ""

    def __init__(self, requestPacketDataExtractor, responsePacketDataExtractor):
        self.packet = None
        self.packetStringContet = ""
        self.requestPacketDataExtractor = requestPacketDataExtractor
        self.responsePacketDataExtractor = responsePacketDataExtractor

    def parse(self, packet, defragmentedPacketStringContent):
        self.packet = packet
        self.packetStringContet = defragmentedPacketStringContent
        if BaseParser.lastPacketContent != self.packetStringContet:
            self.parseToImplement()
        BaseParser.lastPacketContent = self.packetStringContet

    def parseToImplement(self):
        pass
