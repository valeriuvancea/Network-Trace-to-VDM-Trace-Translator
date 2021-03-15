import sys
import json
from globalConfiguration import GlobalConfiguration


def readSystemArguments():
    configurationFileName = sys.argv[1]
    configurationFile = open(configurationFileName, "r")
    configurationFileJson = json.loads(configurationFile.read())
    configurationFile.close()
    GlobalConfiguration.scapyFilter = configurationFileJson["scapyFilter"]
    GlobalConfiguration.dictionary = configurationFileJson["globalDictionary"]
    GlobalConfiguration.argumentsToSave = configurationFileJson["argumentsToSave"]