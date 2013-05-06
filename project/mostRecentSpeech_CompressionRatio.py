import speechSet
import speech
import sys
import math
import glob
import huffmanCoding
if(__name__ == "__main__"):
    if(len(sys.argv) == 2):
        set = speechSet.SpeechSet(sys.argv[1])
        listRecentFilenames = sorted(glob.glob(set.directoryPath+"/"+set.fileType),reverse = True)
        mostRecentFilename = listRecentFilenames[0]#sorted(glob.glob(set.directoryPath+"/"+set.fileType),reverse = True)[0]
        wordUsage = set.wordUsage
        for n in range(100):
            #print listRecentFilenames[n]
            nthMostRecentSpeech = speech.Speech(listRecentFilenames[n],wordUsage)
            #print nthMostRecentSpeech.printStatistics()
            wordUsage = nthMostRecentSpeech.wordUsage
        tree = huffmanCoding.huffmanCodingTree(wordUsage)
        for filename in listRecentFilenames:
            nthMostRecentSpeech = speech.Speech(filename,wordUsage)
            print filename
            print "    " + str(set.compressionRatio(wordUsage,nthMostRecentSpeech.wordUsage,tree = tree))
    else:
        print "error, did not give name for directory"