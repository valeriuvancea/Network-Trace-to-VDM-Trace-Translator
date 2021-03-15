from scapy.all import *
from globalConfiguration import GlobalConfiguration
from network.packet import Packet


class NetworkSniffer:
    def __init__(self, httpGetParser):
        self.httpGetParser = httpGetParser
        self.packets = []
        sniff(filter=GlobalConfiguration.scapyFilter,
              prn=self.checkPackets)

    def checkPackets(self, packet):
        fullStringPacket = str(packet)
        stringContent = packet.sprintf("{Raw:%Raw.load%}")
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
                    self.httpGetParser.parse(
                        packet, foundPacket.stringContent)
            else:
                try:
                    foundPacket = next(
                        x for x in self.packets if x .packetIdToExpect == packet['IP'].id)
                    foundPacket.stringContent += stringContent[1:-1]
                    self.packets.remove(foundPacket)
                    self.httpGetParser.parse(packet, foundPacket.stringContent)
                except:
                    self.httpGetParser.parse(packet, stringContent)
