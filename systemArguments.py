
import sys


def readSystemArguments():
    ipToListenTo = sys.argv[1]
    numberOfArgumentsToSave = sys.argv[2]
    argumentsToSave = []

    for i in range(int(numberOfArgumentsToSave)):
        argumentsToSave.append(sys.argv[3 + i])

    return ipToListenTo, argumentsToSave
