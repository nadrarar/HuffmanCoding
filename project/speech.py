import sys
import re
import operator

class Speech(object):
    def __init__(self, filename):
        self.wordUsage = {}
        self.parseFileAndCountWordUsage(filename)
    def parseFileAndCountWordUsage(self, filename):
        file = open(filename)
        for line in file:
            for word in line.split():
                cleanedWord = re.sub(r"[.,\"!?]",'',word).lower()
                if self.wordUsage.has_key(cleanedWord):
                    self.wordUsage[cleanedWord] = self.wordUsage[cleanedWord]+1
                else:
                    self.wordUsage[cleanedWord] = 1
    def printStatistics(self):
        print max(self.wordUsage.iteritems(),key = operator.itemgetter(1))[0]
    #def compareWordUsage(self, otherSpeech):
    #    print "compare speeches"

if __name__ == "__main__":
    if(len(sys.argv) == 2):
        newSpeech = Speech(sys.argv[1])
        newSpeech.printStatistics()
    else:
        print "Error:  Did not give a filename"