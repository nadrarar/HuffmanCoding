import speech
import speechSet
import tempfile
import unittest
import os
class Testing(unittest.TestCase):
    #setUp------------------------------------------
    def filesSetUp(self):
        #file0
        self.file0 = self.fileSetUp("""
        test file writing writing test test file file file complete
        """)
        print os.curdir
        print self.file0.name
        #os.rename("."+self.file0.name,"file0.txt")
        self.speech0 = speech.Speech(self.file0.name)
        self.file0Usage = {'writing':2,'complete':1,'test':3,'file':4}
        #file1
        self.file1 = self.fileSetUp("""
        second test
        has a few more words
        test writing "writing" test "test has  more complete"
        """)
        #os.rename("./"+self.file1.name,"file1.txt")
        self.speech1 = speech.Speech(self.file1.name)
        self.file1Usage = {'second':1,'has':2,'a':1,'few':1,
                           'more':2,'words':1,'writing':2,'complete':1,'test':4}
    def fileSetUp(self,string):
        file = tempfile.NamedTemporaryFile();
        file.write(string)
        file.seek(0)
        return file

    def directorySetUp(self):
        self.speechSetUsage = {'second':1,'has':1,'a':1,'few':1,'more':1,'words':1,'writing':1,
                               'complete':1,'test':1,'file':1}
        self.speechSet = speechSet.SpeechSet(tempfile.gettempdir())

    def setUp(self):
        self.filesSetUp()
        self.directorySetUp()
    
    #tests----------------------------------------
    def testWordUsage0(self):
        self.assertEqual(self.speech0.wordUsage,self.file0Usage,"error, didn't count the words correctly for file 0")
    def testWordUsage1(self):
        self.assertEqual(self.speech1.wordUsage,self.file1Usage,"error, didn't count the words correctly for file 1")
    def testSpeechSet(self):
        self.assertEqual(self.speechSet.wordUsage,self.speechSetUsage)
if __name__ == "__main__":
    unittest.main()