import speech
import speechSet
import tempfile
import unittest
import os
import huffmanCoding
import operator

class Testing(unittest.TestCase):
    #setUp------------------------------------------
    def filesSetUp(self):
        self.file0 = self.fileSetUp("""
        test file writing writing test test file file file complete
        """)
        self.speech0 = speech.Speech(self.file0.name)
        self.file0Usage = {'writing':2,'complete':1,'test':3,'file':4}
        #file1
        self.file1 = self.fileSetUp("""
        second test
        has a few more words
        test writing "writing" test "test has  more complete"
        """)
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
        self.speechSet = speechSet.SpeechSet(tempfile.gettempdir(),"tmp*")

    def setUp(self):
        self.filesSetUp()
        self.directorySetUp()
        self.file0Frequency= {'second':1,'has':1,'a':1,'few':1,'more':1,'words':1,'writing':3,
                               'complete':2,'test':4,'file':5}
        self.file1Frequency= {'second':2,'has':3,'a':2,'few':2,'more':3,'words':2,'writing':3,
                               'complete':2,'test':5,'file':1}
 
    #tests----------------------------------------
    def testWordUsage0(self):
        self.assertEqual(self.speech0.wordUsage,self.file0Usage)
    def testWordUsage1(self):
        self.assertEqual(self.speech1.wordUsage,self.file1Usage)
    def testSpeechSet(self):
        self.assertEqual(self.speechSet.wordUsage,self.speechSetUsage)
    def testWordFrequency0(self):
        testSpeech = speech.Speech(self.file0.name,self.speechSet.wordUsage)
        self.assertEqual(testSpeech.wordUsage,self.file0Frequency)
    def testWordFrequency1(self):
        testSpeech = speech.Speech(self.file1.name,self.speechSet.wordUsage)
        self.assertEqual(testSpeech.wordUsage,self.file1Frequency)
    def testCodingTree(self):
        testCoding = huffmanCoding.huffmanCodingTree(self.file1Frequency)
        testCoding.printCodingTree(testCoding.root)
        self.assertEqual(testCoding.root.data[0],None)
        self.assertEqual(testCoding.root.right.right.data[0],"test")
        self.assertEqual(testCoding.root.left.left.right.left.data[0],"second")
    def testCodingBits(self):
        testCoding = huffmanCoding.huffmanCodingTree(self.file1Frequency)
        self.assertEqual(testCoding.maxBits,4)
    def testCodingCode(self):
        testCoding = huffmanCoding.huffmanCodingTree(self.file1Frequency)
        self.assertEqual(testCoding.findNode("complete").bits,4)
        self.assertEqual(testCoding.findNode("more").bits,3)
        self.assertEqual(testCoding.findNode("has").bits,3)
        self.assertEqual(testCoding.findNode("test").bits,2)
        self.assertEqual(testCoding.findNode("second").bits,4)
        self.assertEqual(testCoding.root.code,0)
    def testCodingFindNode(self):
        testCoding = huffmanCoding.huffmanCodingTree(self.file1Frequency)
        self.assertEqual(testCoding.findNode("has").data[0],"has")
        self.assertEqual(testCoding.findNode("words").data[0],"words")
        self.assertEqual(testCoding.findNode("file").data[0],"file")
    def testCompressionRatio0(self):
        speech0 = speech.Speech(self.file0.name,self.speechSet.wordUsage)
        speech1 = speech.Speech(self.file1.name,self.speechSet.wordUsage)
        testCoding = huffmanCoding.huffmanCodingTree(self.file0Frequency)
        cRatio = self.speechSet.compressionRatio(speech0,speech1,testCoding)
        self.assertEqual(cRatio,53/60.0)
    def testCompressionRatio1(self):
        speech0 = speech.Speech(self.file0.name,self.speechSet.wordUsage)
        speech1 = speech.Speech(self.file1.name,self.speechSet.wordUsage)
        testCoding = huffmanCoding.huffmanCodingTree(self.file1Frequency)
        cRatio = self.speechSet.compressionRatio(speech1,speech0,testCoding)
        self.assertEqual(cRatio,32/40.0)
    def testCompressionRatioWordUsage(self):
        speech0 = speech.Speech(self.file0.name,self.speechSet.wordUsage)
        speech1 = speech.Speech(self.file1.name,self.speechSet.wordUsage)
        cRatio = self.speechSet.compressionRatio(speech1.wordUsage,speech0.wordUsage)
        self.assertEqual(cRatio,32/40.0)
    def testBitsNeededDictionary0(self):
        testCoding = huffmanCoding.huffmanCodingTree(self.file0Frequency)
        #testCoding.printCodingTree(testCoding.root)
        self.assertEqual(testCoding.bitsNeededDictionary['test'],3)
        self.assertEqual(testCoding.bitsNeededDictionary['more'],4)
        self.assertEqual(testCoding.bitsNeededDictionary['words'],4)
        self.assertEqual(testCoding.bitsNeededDictionary['writing'],3)
    def testBitsNeededDictionary1(self):
        testCoding = huffmanCoding.huffmanCodingTree(self.file1Frequency)
        #testCoding.printCodingTree(testCoding.root)
        self.assertEqual(testCoding.bitsNeededDictionary['more'],3)
        self.assertEqual(testCoding.bitsNeededDictionary['words'],4)
        self.assertEqual(testCoding.bitsNeededDictionary['writing'],3)
        self.assertEqual(testCoding.bitsNeededDictionary['test'],2)
    #def testCompressionRatioSet0(self):
    #    testCoding = huffmanCoding.huffmanCodingTree(self.file0And1Frequency)
    #    self.assertEqual(

if __name__ == "__main__":
    unittest.main()