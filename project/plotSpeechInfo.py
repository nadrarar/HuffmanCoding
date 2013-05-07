import numpy
import matplotlib
import sys
import glob

def parseFile(file):
    fileDictionary = {}
    return fileDictionary

def createPlot(dictionary):
    print dictionary

if(__name__ == "__main__"):
    if(len(sys.argv) == 2):
        informationFile = open(sys.argv[1])
        createPlot(parseFile(informationFile))
    elif(len(sys.argv) == 3):
        if(sys.argv[1] == '-f'):
            informationFile = open(sys.argv[1])
            createPlot(parseFile(informationFile))
        elif(sys.argv[1] == '-d'):
            listOfInformationFiles = glob.glob(sys.argv[2]+"*RecentSpeech.txt")
            print listOfInformationFiles
            for f in listOfInformationFiles:
                createPlot(parseFile(f))
        else:
            print "error, if using file, use -f filename, if using directory, use -d pathOfDirectory"
    elif(len(sys.argv) == 1):
        listOfInformationFiles = glob.glob("./*RecentSpeech.txt")
        print listOfInformationFiles
        for f in listOfInformationFiles:
            createPlot(parseFile(f))
    else:
        print "error, given wrong argument"