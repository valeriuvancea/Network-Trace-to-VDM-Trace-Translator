from vdm.vdmTrace import addParametersToVDMTrace


class BasePacketDataExtractor:
    def __init__(self):
        self.source = ""
        self.destination = ""
        self.packet = None
        self.packetStringContent = ""
        self.data = {}

    def printPacket(self):
        print("Source: " + self.source)
        print("Dest: " + self.destination)
        print("Data: ")
        print(self.data)
        print()

    def addAdditionalParametersToData(self):
        pass

    def getDataFromPacket(self):
        pass

    def writeDataIntoVDMTraceFromPacket(self, packet, packetStringContent):
        self.packet = packet
        self.packetStringContent = packetStringContent
        self.source = packet.payload.src
        self.destination = packet.payload.dst
        self.getDataFromPacket()
        self.printPacket()
        self.addAdditionalParametersToData()
        addParametersToVDMTrace(self.data)
