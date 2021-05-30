class BaseParser:
    def __init__(self):
        self.packet = None
        self.packetStringContet = ""
        self.lastPacketContent = ""

    def parse(self, packet):
        self.packet = packet
        self.packetStringContet = packet.sprintf("{Raw:%Raw.load%}")
        if self.lastPacketContent != self.packetStringContet:
            self.parseToImplement()
        self.lastPacketContent = self.packetStringContet

    def parseToImplement(self):
        pass
