import speechSet
import speech
import sys
import math
import glob
import huffmanCoding
import time
if(__name__ == "__main__"):
    if(len(sys.argv) == 2):
        print "finding speech set"
        set = speechSet.SpeechSet(sys.argv[1])
        print "finding all filenames"
        listRecentFilenames = sorted(glob.glob(set.directoryPath+"/"+set.fileType),reverse = True)
        mostRecentFilename = listRecentFilenames[0]#sorted(glob.glob(set.directoryPath+"/"+set.fileType),reverse = True)[0]
        wordUsage = set.wordUsage
        print "finding word usage"
        for n in range(1):
            #print listRecentFilenames[n]
            nthMostRecentSpeech = speech.Speech(listRecentFilenames[n],wordUsage)
            #print nthMostRecentSpeech.printStatistics()
            wordUsage = nthMostRecentSpeech.wordUsage
        print "start finding coding tree "+str(time.clock())
        tree = huffmanCoding.huffmanCodingTree(wordUsage)
        print "completed finding coding tree "+str(time.clock())
        #increase speed by making a dictionary that stores the number of bits needed to code
        #every key, and use that for compressionRatio
        print "finding compression ratio"
        for filename in listRecentFilenames:
            nthMostRecentSpeech = speech.Speech(filename,wordUsage)
            print filename
            print "    " + str(set.compressionRatio(wordUsage,nthMostRecentSpeech.wordUsage,tree = tree))
    else:
        print "error, did not give name for directory"