import sys
import re
import operator
import glob

class SpeechSet(object):
    def __init__(self,directoryPath):
        self.wordUsage = {}
        filelist = glob.glob(directoryPath+"/*.txt")
        for filename in filelist:
            self.parseFile(filename)
    def parseFile(self, filename):
        file = open(filename)
        for line in file:
            for word in line.split():
                cleanedWord = re.sub(r"[.,\"!?]",'',word).lower()
                self.wordUsage[cleanedWord] = 1

if __name__ == "__main__":
    if(len(sys.argv) == 2):
        set = SpeechSet(sys.argv[1])
        print set.wordUsage
    else:
        print "Error:  Did not give a filename"