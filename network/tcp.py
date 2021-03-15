from scapy.all import *

class TLS(Packet):
    [...]

    @classmethod
    def tcp_reassemble(cls, data, metadata):
        length = struct.unpack("!H", data[3:5])[0] + 5
        if len(data) == length:
            return TLS(data)