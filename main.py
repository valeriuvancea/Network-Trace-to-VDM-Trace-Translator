from systemArguments import readSystemArguments
from vdm.vdmTrace import vdmTraceFileInit
from network.networkSnifferInitializer import NetworkSnifferInitializer

readSystemArguments()
vdmTraceFileInit()
NetworkSnifferInitializer()
