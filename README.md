# Network Sniffer to VDM Trace
This script generates a VDM Trace by sniffing network packets from or to a specific IP address. This script uses scapy for network sniffing.

## How to use
Call the main script with two arguments. The first one is the IP address used for sniffing and the second is a path to the configuration file.
E.g. `python main.py 192.168.0.35 argumentsToSave.json`

## Configuration file
The configuration is a json file where you can specify how to write certain parameters into the VDM trace.
E.g.
```javascript
[
    {
        "name": "a",
        "type": "STRING"
    },
    {
        "name": "b",
        "type": "STRING"
    },
    {
        "name": "c",
        "type": "ARRAY"
    },
    {
        "name": "d",
        "type": "OBJECT"
    },
    {
        "name": "e",
        "type": "BOOLEAN"
    },
    {
        "name": "f",
        "type": "NUMBER"
    }
]
```

### Supported types
- STRING -> is equivalent to `seq of char` in VDM
- NUMBER
- BOOLEAN
- ARRAY -> is equivalent to a `seq` in VDM. The type of the sequence will be inferred from the JSON data format from the packet.
- OBJECT -> is equivalent to a `map` in VDM. The type of the map will be inferred from the JSON data format from the packet. (usually in JSON the key type is a string so a `seq of char` in VDM)

## Parser
The packet parsers supports the following:
- HTTP GET Requests -> this parses the request query parameters
- HTTP GET Response -> this parses the json returned by the server

## Extension
One can extend this script for its own protocols

### Packet data extractor
There following base classes are defined which can be used for extension:
- `BasePacketDataExtractor` -> this is a generic data extractor. You can inherit this class and then implement the `getDataFromPacket` function where you have access to the raw scapy packet and also the packet in string packet and you need to populate the `self.data` python dict. This is where you will need to add the parameters that will be added to the VDM trace.
- `HTTPGetRequestPacketDataExtractor` and `HTTPGetResponsePacketDataExtractor` -> these are generic data extractor for http get packets. The request class extracts its parameters from the request query parameters and the response class extracts tis parameters from the json returned by the server. This classes inherits the `BasePacketDataExtractor` class and can also be inherited from and the the `addAdditionalParametersToData` function can bee implemented to add additional data (e.g. A flag that indicates that the message was from or to the server)

### Network Sniffer
The `NetworkSniffer` class implements a function called `checkPackets` which will be called on every packet sniffed that that was send from or to the specific IP address defined when using the script. This functions only implements functionality for a HTTP GET packet parser, but it can be extended to use any other wanted parser.
