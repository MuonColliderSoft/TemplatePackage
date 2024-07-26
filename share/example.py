from Gaudi.Configuration import *

from Configurables import LcioEvent, EventDataSvc, MarlinProcessorWrapper
from k4MarlinWrapper.parseConstants import *
algList = []
evtsvc = EventDataSvc()


CONSTANTS = {
}

parseConstants(CONSTANTS)

read = LcioEvent()
read.OutputLevel = WARNING
read.Files = ["input_file.slcio"]
algList.append(read)

MyAIDAProcessor = MarlinProcessorWrapper("MyAIDAProcessor")
MyAIDAProcessor.OutputLevel = WARNING 
MyAIDAProcessor.ProcessorType = "AIDAProcessor" 
MyAIDAProcessor.Parameters = {
                              "Compress": ["1"],
                              "FileName": ["histograms"],
                              "FileType": ["root"]
                              }

MyProcessor = MarlinProcessorWrapper("MyProcessor")
MyProcessor.OutputLevel = WARNING 
MyProcessor.ProcessorType = "TemplateProcessor" 
MyProcessor.Parameters = {
                          "InputCollectionName": ["MCParticle"],
                          "MinPt": ["2"],
                          "OutputCollectionName": ["OutMCParticle"]
                          }

algList.append(MyAIDAProcessor)
algList.append(MyProcessor)

from Configurables import ApplicationMgr
ApplicationMgr( TopAlg = algList,
                EvtSel = 'NONE',
                EvtMax   = 10,
                ExtSvc = [evtsvc],
                OutputLevel=WARNING
              )
