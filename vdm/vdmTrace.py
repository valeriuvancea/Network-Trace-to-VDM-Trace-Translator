import atexit
import json

isFirstParameterAdded = False
vdmTraceFile = None
argumentsToSaveInTrace = []


def vdmTraceFileInit(argumentsToSave):
    global vdmTraceFile
    global argumentsToSaveInTrace
    vdmTraceFile = open("trace.txt", "w")
    vdmTraceFile.write("[")
    atexit.register(exit_handler)
    argumentsToSaveInTrace = argumentsToSave


def addParametersToVDMTrace(parameters):
    global isFirstParameterAdded
    global vdmTraceFile
    global argumentsToSaveInTrace
    # If the parameters have at least one requested argument
    if list(set(map(lambda argument: argument["name"], argumentsToSaveInTrace)) & set(parameters.keys())):
        if isFirstParameterAdded:
            vdmTraceFile.write(",")
        else:
            isFirstParameterAdded = True
        vdmTraceFile.write("mk_(")
        isFirstArgumentAdded = False
        for argument in argumentsToSaveInTrace:
            if argument["name"] in parameters.keys():
                if isFirstArgumentAdded:
                    vdmTraceFile.write(",")
                else:
                    isFirstArgumentAdded = True

                if argument["type"] == "OBJECT":
                    vdmTraceFile.write(json.dumps(
                        parameters[argument["name"]]).replace(": ", "|->"))
                elif argument["type"] == "BOOLEAN":
                    vdmTraceFile.write(
                        "true" if parameters[argument["name"]] else "false")
                elif argument["type"] == "NUMBER":
                    vdmTraceFile.write(str(
                        parameters[argument["name"]]))
                else:
                    vdmTraceFile.write(json.dumps(
                        parameters[argument["name"]]))

        vdmTraceFile.write(")")


def exit_handler():
    # When CTRL+C is pressed, the program will finish writing into the VDM trace file and then it will exit
    global vdmTraceFile
    vdmTraceFile.write("]")
    vdmTraceFile.close()
    print('Application closed! Saving VDM trace!')
