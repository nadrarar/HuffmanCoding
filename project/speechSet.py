import sys
import re
import operator
import glob
import speech
import huffmanCoding
import math
class SpeechSet(object):
    def __init__(self,directoryPath,fileType="*.txt"):
        self.directoryPath = directoryPath
        self.fileType = fileType
        self.wordUsage = {}
        filelist = glob.glob(directoryPath+"/"+fileType)
        for filename in filelist:
            self.parseFile(filename)
    def parseFile(self, filename):
        file = open(filename)
        for line in file:
            for word in line.split():
                cleanedWord = re.sub(r"[.,\"!?]",'',word).lower()
                self.wordUsage[cleanedWord] = 1
    def compressionRatio(self,speechWithCoding, speechThatIsCompared,tree = None):
        wordInstanceCode = speechWithCoding
        wordInstanceCompare = speechThatIsCompared
        if(isinstance(speechWithCoding,speech.Speech)):
           wordInstanceCode = speechWithCoding.wordUsage
        if(isinstance(speechThatIsCompared,speech.Speech)):
           wordInstanceCompare = speechThatIsCompared.wordUsage
        if(tree == None):
            tree = huffmanCoding.huffmanCodingTree(wordInstanceCode)
        bitsInBlockCoding = int(math.ceil(math.log(wordInstanceCompare.__len__(),2)))*wordInstanceCompare.__len__()
        bitsInHuffmanCoding = 0
        for entry in wordInstanceCompare.iteritems():
            bitsInHuffmanCoding += int(tree.findNode(entry[0]).bits)
            #print entry[0]+", "+str(bitsInHuffmanCoding)+", "+str(bitsInBlockCoding)
        if(bitsInBlockCoding > 0):
            return float(bitsInHuffmanCoding)/float(bitsInBlockCoding)
        else:
            return 0
if __name__ == "__main__":
    if(len(sys.argv) == 2):
        set = SpeechSet(sys.argv[1])
        print set.wordUsage
    elif(len(sys.argv) == 3):
        if(sys.argv[1]=='-w'):
            set = SpeechSet(sys.argv[2])
            wordUsage = open("sourceSymbols.txt",'w+')
            wordUsage.write(str(set.wordUsage))
        elif(sys.argv[1] == '-s'):
            set = SpeechSet(sys.argv[2])
            mostRecentFilename = sorted(glob.glob(set.directoryPath+"/"+set.fileType),reverse = True)[0]
            print mostRecentFilename
            speech0 = speech.Speech(mostRecentFilename,set.wordUsage)
            speech0.printStatistics()
            print len(speech0.wordUsage)
        else:
            print "Error:  Usage is -s 'directoryPath' or -w 'directoryPath'"
    else:
        print "Error:  Did not give a filename"