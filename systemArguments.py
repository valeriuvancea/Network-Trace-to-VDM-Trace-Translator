import sys
import json


def readSystemArguments():
    ipToListenTo = sys.argv[1]
    argumentsToSaveFileName = sys.argv[2]
    argumentsToSaveFile = open(argumentsToSaveFileName, "r")
    argumentsToSave = json.loads(argumentsToSaveFile.read())
    argumentsToSaveFile.close()

    return ipToListenTo, argumentsToSave
