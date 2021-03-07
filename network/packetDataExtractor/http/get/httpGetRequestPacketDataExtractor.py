from network.packetDataExtractor.basePacketDataExtractor import BasePacketDataExtractor
import urllib.parse as urlparse
from urllib.parse import parse_qs


class HTTPGetRequestPacketDataExtractor(BasePacketDataExtractor):
    def getDataFromPacket(self):
        packetLines = self.packetStringContent.split(r"\r\n")
        firstPacketLine = packetLines[0]
        # The request parameters are on the first line of the packet between the HTTP request method and the HTTP protocol version. This three information are separated by space
        queryRequest = firstPacketLine.split(" ")[1]
        requestParameters = urlparse.parse_qs(urlparse.urlparse(
            queryRequest).query)
        # The HTTP standard specifies that each query parameter should be a list.
        # One can use parameters like this:
        # localhost/?test=asd&test=qwe
        # Which in python will be translated as {'test': ['asd', 'qwe']}.
        # Even if the parameter is only mentioned once, python will still parse it as a list with one element
        self.data = self.getListOfRequestParameters(requestParameters)

    def getListOfRequestParameters(self, requestParameters):
        listOfRequestParameters = {}
        for key in requestParameters:
            listOfRequestParameters[key] = requestParameters[key][0]
        return listOfRequestParameters
