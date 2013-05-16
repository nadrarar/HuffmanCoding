import numpy
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import sys
import glob
import re
import operator
def parseFileName(filename):
    fileNumber = re.findall("\d+",filename)
    fileMostLeast = re.findall("Most|Least",filename)
    if(fileNumber):
        if(fileMostLeast):
            return str(fileNumber[0]+" "+fileMostLeast[0]+" Recent")
        else:
            print "error in parsing Most and Least speech"
            return "NO NAME"
    else:
        print "error when parsing number of speeches"
        return "NO NAME"
    #return re.sub("[:num]"
def parseFile(filename):
    f = open(filename)
    fileDictionary = {}
    for l in f:
        fileDictionary[str(re.sub("../speeches/",'',l.split()[0]))] = float(l.split()[1])
    return fileDictionary

def createPlot(dictionary,pdf,plotName = "No Name"):
    plotName = parseFileName(plotName)
    listOfDictionary = sorted(dictionary.iteritems(), key = operator.itemgetter(0))
    yearsList = []
    numbersList = []
    for e in listOfDictionary:
        yearsList.append(float(re.sub(".txt","",re.sub("_","",e[0])))/100000000.0)
        numbersList.append(e[1])
    plot = plt.subplot(111)
    plot.plot(yearsList,numbersList,label = plotName)
    #plot.ylabel('compression ratio')
    #plot.xlabel('year')
    plot.legend(loc='upper center',bbox_to_anchor=(0.5,1.05),ncol=3,fancybox=True,shadow=True)
    pdf.savefig()
    #pdf.savefig(fig)
def pdfMostRecentSpeeches():
    listOfInformationFiles = glob.glob("./*MostRecentSpeech.txt")
    fig = plt.figure(figsize = (8.27, 8.27),dpi = 100)
    
    for f in listOfInformationFiles:
        pdf = PdfPages('mostRecentSpeeches.pdf')
        createPlot(parseFile(f),pdf,f)
        pdf.close()
def pdfLeastRecentSpeeches():
    fig = plt.figure(figsize = (8.27, 8.27),dpi = 100)
    listOfInformationFiles = glob.glob("./*LeastRecentSpeech.txt")
    for f in listOfInformationFiles:
        parseFileName(f)
        pdf = PdfPages('leastRecentSpeeches.pdf')
        createPlot(parseFile(f),pdf,f)
        pdf.close()
def pdf1MostRecentSpeeches():
    fig = plt.figure(figsize = (8.27, 8.27),dpi = 100)
    listOfInformationFiles = glob.glob("./1MostRecentSpeech.txt")
    for f in listOfInformationFiles:
        pdf = PdfPages('1MostRecentSpeeches.pdf')
        createPlot(parseFile(f),pdf,f)
        pdf.close()
def pdf626MostRecentSpeeches():
    fig = plt.figure(figsize = (8.27, 8.27),dpi = 100)
    listOfInformationFiles = glob.glob("./626MostRecentSpeech.txt")
    for f in listOfInformationFiles:
        pdf = PdfPages('626MostRecentSpeeches.pdf')
        createPlot(parseFile(f),pdf,f)
        pdf.close()
def pdfAllSpeeches():
    fig = plt.figure(figsize = (8.27, 8.27),dpi = 100)
    listOfInformationFiles = glob.glob("./*RecentSpeech.txt")
    for f in listOfInformationFiles:
        pdf = PdfPages('allSpeeches.pdf')
        createPlot(parseFile(f),pdf,f)
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
        speechRatio = parseFile("./626MostRecentSpeech.txt")
        ratioBottomToTop = sorted(speechRatio.iteritems(),key = operator.itemgetter(1))
        print "best ratio speeches:"
        for x in range(10):
            print " "+str(ratioBottomToTop[x])
        print "worst ratio speeches:"
        for x in range(len(ratioBottomToTop)-1,len(ratioBottomToTop)-11,-1):
            print " "+str(ratioBottomToTop[x])
        pdf1MostRecentSpeeches()
        pdfMostRecentSpeeches()
        pdf626MostRecentSpeeches()
        pdfLeastRecentSpeeches()
        pdfAllSpeeches()
    else:
        print "error, given wrong argument"