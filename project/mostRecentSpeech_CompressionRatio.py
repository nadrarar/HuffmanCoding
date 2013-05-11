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
    if((len(sys.argv) == 4) or (len(sys.argv) == 5)):
        print "finding speech set"
        set = speechSet.SpeechSet(sys.argv[1])
        
        print "finding all filenames"
        if len(sys.argv) == 5:
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
        print "finding compression ratio"
        file = open(sys.argv[3],"w+")
        for filename in listRecentFilenames:
            nthMostRecentSpeech = speech.Speech(filename,wordUsage)
            file.write(filename+" "+str(set.compressionRatio(wordUsage,nthMostRecentSpeech.wordUsage,tree = tree))+'\n')
            #print "    " + str(set.compressionRatio(wordUsage,nthMostRecentSpeech.wordUsage,tree = tree))
    else:
        print "error, did not give name for directory"