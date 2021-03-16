from network.parser.baseParser import BaseParser
from network.packet import Packet


class HTTPGetParser(BaseParser):
    def __init__(self, requestPacketDataExtractor, responsePacketDataExtractor):
        super().__init__()
        self.packets = []
        self.requestPacketDataExtractor = requestPacketDataExtractor
        self.responsePacketDataExtractor = responsePacketDataExtractor

    def parseToImplement(self):
        packet = self.packet
        stringContent = self.packetStringContet
        fullStringPacket = str(packet)
        if fullStringPacket.find('GET'):
            if 'IP' in packet and packet['IP'].len == 1500:
                packetIdToExpect = packet['IP'].id + 1
                try:
                    foundPacket = next(x for x in self.packets if x .packetIdToExpect ==
                                       packet['IP'].id)
                    foundPacket.stringContent += stringContent[1:-1]
                    foundPacket.packetIdToExpect = packetIdToExpect
                    self.packets[self.packets.index(foundPacket)] = foundPacket
                except:
                    foundPacket = Packet(packetIdToExpect, stringContent[:-1])
                    self.packets.append(foundPacket)
                if "\\r\\n\\r\\n\'" in stringContent:
                    self.writeAttributesIntoTheVDMTrace(foundPacket.stringContent)
            else:
                try:
                    foundPacket = next(
                        x for x in self.packets if x .packetIdToExpect == packet['IP'].id)
                    foundPacket.stringContent += stringContent[1:-1]
                    self.packets.remove(foundPacket)
                    self.writeAttributesIntoTheVDMTrace(foundPacket.stringContent)
                except:
                    self.writeAttributesIntoTheVDMTrace(stringContent)
        

    def writeAttributesIntoTheVDMTrace(self, packetStringContet):
        # Request packet
        if packetStringContet[:4] == "'GET":
            self.requestPacketDataExtractor.writeDataIntoVDMTraceFromPacket(
                self.packet, packetStringContet)
        # Response packet
        elif "Content-Type: application/json" in packetStringContet:
            self.responsePacketDataExtractor.writeDataIntoVDMTraceFromPacket(
                self.packet, packetStringContet)
