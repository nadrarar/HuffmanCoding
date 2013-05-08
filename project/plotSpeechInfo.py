import numpy
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import sys
import glob
import re
import operator
def parseFile(filename):
    f = open(filename)
    fileDictionary = {}
    for l in f:
        fileDictionary[str(re.sub("../speeches/",'',l.split()[0]))] = float(l.split()[1])
    return fileDictionary

def createPlot(dictionary):
    pdf = PdfPages('speechPlot.pdf')
    listOfDictionary = sorted(dictionary.iteritems(), key = operator.itemgetter(0))
    yearsList = []
    numbersList = []
    for e in listOfDictionary:
        yearsList.append(float(re.sub(".txt","",re.sub("_","",e[0])))/100000000.0)
        numbersList.append(e[1])
    plt.plot(yearsList,numbersList)
    plt.ylabel('compression ratio')
    plt.xlabel('year')
    pdf.savefig()
    pdf.close()

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
            #print listOfInformationFiles
            for f in listOfInformationFiles:
                createPlot(parseFile(f))
        else:
            print "error, if using file, use -f filename, if using directory, use -d pathOfDirectory"
    elif(len(sys.argv) == 1):
        listOfInformationFiles = glob.glob("./*RecentSpeech.txt")
        #print listOfInformationFiles
        for f in listOfInformationFiles:
            createPlot(parseFile(f))
    else:
        print "error, given wrong argument"