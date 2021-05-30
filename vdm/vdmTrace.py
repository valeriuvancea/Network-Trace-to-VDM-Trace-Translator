import atexit
import json
from globalConfiguration import GlobalConfiguration

isFirstParameterAdded = False
vdmTraceFile = None


def vdmTraceFileInit():
    global vdmTraceFile
    vdmTraceFile = open("trace.txt", "w")
    vdmTraceFile.write("[")
    atexit.register(exit_handler)


def addParametersToVDMTrace(parameters):
    global isFirstParameterAdded
    global vdmTraceFile
    # If the parameters have at least one requested argument
    if list(set(map(lambda argument: argument["name"], GlobalConfiguration.argumentsToSave)) & set(parameters.keys())):
        if isFirstParameterAdded:
            vdmTraceFile.write(",")
        else:
            isFirstParameterAdded = True
        vdmTraceFile.write("{")
        isFirstArgumentAdded = False
        for argument in GlobalConfiguration.argumentsToSave:
            if argument["name"] in parameters.keys():
                if isFirstArgumentAdded:
                    vdmTraceFile.write(",")
                else:
                    isFirstArgumentAdded = True

                vdmTraceFile.write('"' + argument["name"] + '"|->')

                if argument["type"] == "OBJECT":
                    vdmTraceFile.write(json.dumps(
                        parameters[argument["name"]]).replace(": ", "|->"))
                elif argument["type"] == "BOOLEAN":
                    vdmTraceFile.write(
                        "true" if parameters[argument["name"]] else "false")
                elif argument["type"] == "NUMBER":
                    vdmTraceFile.write(str(
                        parameters[argument["name"]]))
                elif argument["type"] == "TOKEN":
                    vdmTraceFile.write("mk_token(" + str(
                        parameters[argument["name"]]) +")")
                else:
                    vdmTraceFile.write(json.dumps(
                        parameters[argument["name"]]))

        vdmTraceFile.write("}")


def exit_handler():
    # When CTRL+C is pressed, the program will finish writing into the VDM trace file and then it will exit
    global vdmTraceFile
    vdmTraceFile.write("]")
    vdmTraceFile.close()
    print('Application closed! Saving VDM trace!')
