import systemArguments
import networkSniffer
import vdmTrace

ipToListenTo, argumentsToSave = systemArguments.readSystemArguments()
vdmTrace.vdmTraceFileInit(argumentsToSave)
networkSniffer.networkSnifferInit(ipToListenTo)
