import sys
import re
import operator
import itertools
class Speech(object):
    def __init__(self, filename,wordUsage0=None):
        if(wordUsage0==None):
            wordUsage0 = {}
        self.wordUsage = wordUsage0.copy()
        self.wordCount = 0
        self.parseFileAndCountWordUsage(filename)
    def parseFileAndCountWordUsage(self, filename):
        file = open(filename)
        for line in file:
            for word in line.split():
                self.wordCount += 1
                cleanedWord = re.sub(r"[.,\"!?]",'',word).lower()
                if self.wordUsage.has_key(cleanedWord):
                    self.wordUsage[cleanedWord] = self.wordUsage[cleanedWord]+1
                else:
                    self.wordUsage[cleanedWord] = 1
    def printStatistics(self):
        print "Top 5 words:"
        for word in sorted(self.wordUsage.iteritems(),key = operator.itemgetter(1),reverse=True)[:5]:
            print word
    #def compareWordUsage(self, otherSpeech):
    #    print "compare speeches"

if __name__ == "__main__":
    if(len(sys.argv) == 2):
        newSpeech = Speech(sys.argv[1])
        newSpeech.printStatistics()
    else:
        print "Error:  Did not give a filename"