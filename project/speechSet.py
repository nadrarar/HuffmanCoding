import sys
import re
import operator
import glob
import speech
import huffmanCoding
import math

ignoredWords = ['to','of','in','for','on','with','at','by','from','the','and','a','that','as','an']

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
    def compressionRatio(self,encodingWordUsage, compressionUsage,tree = None):
        # the first two arguments can either be speeches or dictionaries with words and frequencies
        if(isinstance(encodingWordUsage,speech.Speech)):
           encodingWordUsage = encodingWordUsage.wordUsage
        if(isinstance(compressionUsage,speech.Speech)):
           compressionUsage = compressionUsage.wordUsage
        #tree can be provided, to help performance, otherwise make a tree
        if(tree == None):
            tree = huffmanCoding.huffmanCodingTree(encodingWordUsage)
        wordCount = 0 
        bitsInHuffmanCoding = 0
        #note, don't use the additive smoothing for finding ratio
        for entry in compressionUsage.iteritems():
            #bits needed dictionary has the number of bits that each node of tree would encode.  This could
            #be found using tree.findNode(), but looking things up in the tree took a long time, relative
            #to the number of times that it has to be done.
            bitsInHuffmanCoding += (entry[1]-1)*tree.bitsNeededDictionary[entry[0]]
            wordCount += entry[1] - 1
        bitsInBlockCoding = wordCount*int(math.ceil(math.log(len(compressionUsage),2)))
        #for debugging
        #print "huffmanCoding = "+str(bitsInHuffmanCoding)+" blockCoding: "+str(bitsInBlockCoding)
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