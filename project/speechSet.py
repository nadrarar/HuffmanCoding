import sys
import re
import operator
import glob

class SpeechSet(object):
    def __init__(self,directoryPath,fileType="*.txt"):
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

if __name__ == "__main__":
    if(len(sys.argv) == 2):
        set = SpeechSet(sys.argv[1])
        print set.wordUsage
    elif(len(sys.argv) == 3):
        if(sys.argv[1]=='-w'):
            set = SpeechSet(sys.argv[2])
            wordUsage = open("speechSetWordUsage.txt",'w+')
            wordUsage.write(str(set.wordUsage))
        else:
            print "Error:  Usage is -w 'directoryPath'"
    else:
        print "Error:  Did not give a filename"