import speechSet
import speech
import sys
import math
import glob
import huffmanCoding
import time
import numpy
import matplotlib
import operator

def determineWordUsage(startingWordUsage,totalSpeeches):
    wordUsage = startingWordUsage.copy()
    for n in range(totalSpeeches):
        #print listRecentFilenames[n]
        nthMostRecentSpeech = speech.Speech(listRecentFilenames[n],wordUsage)
        #print nthMostRecentSpeech.printStatistics()
        wordUsage= nthMostRecentSpeech.wordUsage
    return wordUsage

if(__name__ == "__main__"):
    if(len(sys.argv) >= 3):
        print "finding speech set"
        set = speechSet.SpeechSet(sys.argv[1])
        reverse = False
        if(len(sys.argv) == 4):
            reverse = True
        print "finding all filenames"
        if(reverse):#note that reversing the list puts it in chronological non-reverse
            listRecentFilenames = sorted(glob.glob(set.directoryPath+"/"+set.fileType),reverse = False)
        else:
            listRecentFilenames = sorted(glob.glob(set.directoryPath+"/"+set.fileType),reverse = True)
        print "finding word usage"
        wordUsage = determineWordUsage(set.wordUsage,int(sys.argv[2]))
        #print sorted(wordUsage.iteritems(),key = operator.itemgetter(1))
        print "start finding coding tree "+str(time.clock())
        tree = huffmanCoding.huffmanCodingTree(wordUsage)
        #print "bit the "+ str(tree.bitsNeededDictionary["the"])
        #print "bit a " + str(tree.bitsNeededDictionary["a"])
        #print "bit for " + str(tree.bitsNeededDictionary["for"])
        print "completed finding coding tree "+str(time.clock())
        file = None
        fileForWordCount = open("WordCount.txt","w+")
        if(reverse):
            file = open(sys.argv[2]+"LeastRecentSpeech.txt","w+")
        else:
            file = open(sys.argv[2]+"MostRecentSpeech.txt","w+")
        print "starting compression ratio, "+str(time.clock())
        for filename in listRecentFilenames:
            nthMostRecentSpeech = speech.Speech(filename,wordUsage)
            file.write(filename+" "+str(set.compressionRatio(wordUsage,nthMostRecentSpeech.wordUsage,tree = tree))+'\n')
            fileForWordCount.write(filename+" "+str(nthMostRecentSpeech.wordCount)+'\n')
        print "completed compression ratio, "+str(time.clock())
            #print "    " + str(set.compressionRatio(wordUsage,nthMostRecentSpeech.wordUsage,tree = tree))
    else:
        print "error, did not give name for directory"