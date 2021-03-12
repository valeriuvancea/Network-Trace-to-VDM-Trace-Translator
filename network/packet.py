class Packet:
    def __init__(self, packetIdToExpect, stringContent):
        self.packetIdToExpect = packetIdToExpect
        self.stringContent = stringContent
