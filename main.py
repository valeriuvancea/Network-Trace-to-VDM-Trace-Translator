from scapy.all import *
import json
import urllib.parse as urlparse
from urllib.parse import parse_qs
import atexit

ipToListenTo = sys.argv[1]
numberOfArgumentsToRead = sys.argv[2]
argumentsToRead = []
lastPacketContent = ""
vdmTraceFile = open("trace.txt", "w")
vdmTraceFile.write("[")

for i in range(int(numberOfArgumentsToRead)):
    argumentsToRead.append(sys.argv[3 + i])


def checkPackets(packet):
    http_packet = str(packet)
    if http_packet.find('GET'):
        parseHTTPGetPacket(packet)


isFirstParameterAdded = False


def addParametersToVDMTrace(parameters):
    global isFirstParameterAdded
    # If the parameters have at least one requested argument
    if list(set(argumentsToRead) & set(parameters.keys())):
        if isFirstParameterAdded:
            vdmTraceFile.write(",")
        else:
            isFirstParameterAdded = True
        vdmTraceFile.write("mk_(")
        isFirstArgumentAdded = False
        for argumentToRead in argumentsToRead:
            if argumentToRead in parameters.keys():
                if isFirstArgumentAdded:
                    vdmTraceFile.write(",")
                else:
                    isFirstArgumentAdded = True
                vdmTraceFile.write('"' + parameters[argumentToRead] + '"')
        vdmTraceFile.write(")")


def parseHTTPGetPacket(packet):
    global lastPacketContent
    packetContet = packet.sprintf("{Raw:%Raw.load%}")
    # The scapy library sees a packet twice. Once when it leaves the interface and once when it comes bck. We only want to process a packet once
    if lastPacketContent != packetContet:
        packetLines = packetContet.split(r"\r\n")
        # Request packet
        if packetContet[:4] == "'GET":
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
            requestParameters = getListOfRequestParameters(requestParameters)
            print("Source: " + packet.payload.src)
            print("Dest: " + packet.payload.dst)
            print("Data: ")
            print(requestParameters)
            print()
            addParametersToVDMTrace(requestParameters)
        # Response packet
        elif "Content-Type: application/json" in packetContet:
            lastPacketLine = packetLines[-1]
            # The response JSON data is on the last line of the HTTP packet and it has an extra "/" character at the end. The following line removes it and loads the JSON
            responseParameters = json.loads(lastPacketLine[0:-1])
            print("Source: " + packet.payload.src)
            print("Dest: " + packet.payload.dst)
            print("Data: ")
            print(responseParameters)
            print()
            addParametersToVDMTrace(responseParameters)
    lastPacketContent = packetContet


def getListOfRequestParameters(requestParameters):
    listOfRequestParameters = {}
    for key in requestParameters:
        listOfRequestParameters[key] = requestParameters[key][0]
    return listOfRequestParameters


sniff(filter="host " + ipToListenTo + " or dst " + ipToListenTo, prn=checkPackets
      )


def exit_handler():
    # When CTRL+C is pressed, the program will finish writing into the VDM trace file and then it will exit
    vdmTraceFile.write("]")
    vdmTraceFile.close()
    print('Application closed! Saving VDM trace!')


atexit.register(exit_handler)
