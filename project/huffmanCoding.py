import sys
import speechSet
import operator
import math
import re
import Queue
import copy
class treeNode(object):
    
    def __init__(self, left = None,right = None, data = None, code = None):
        self.left = left
        self.right = right
        self.data = data
        self.code = code
        self.bits = None
class huffmanCodingTree(object):

    def printCodingTree(self,node,level = 0):
        if(node != None):
            for x in range(level):
                sys.stdout.write(" ")
            stringCode = bin(node.code<<self.maxBits-node.bits).zfill(self.maxBits)
            stringCode = re.sub('0b','',stringCode).zfill(self.maxBits)
            print str(level)+' '+str(node.data)+' '+stringCode
            self.printCodingTree(level = level+1,node = node.right)
            self.printCodingTree(level = level+1,node = node.left)

    def __init__(self,dict):
        dictionaryList = sorted(dict.iteritems(),key = operator.itemgetter(1),reverse=True)
        #nodesList = []
        nodesList = Queue.PriorityQueue()
        for i in dictionaryList:
            node = treeNode(data = i)
            nodesList.put(tuple([node.data[1],node]))
        #used to debug
        """
        print "iteration for tree"
        nodesListCopy = Queue.PriorityQueue()
        for n in range(nodesList.qsize()):
            qn = nodesList.get()
            print "  "+str(qn[1].data)
            nodesListCopy.put(qn)
        nodesList = nodesListCopy
        """
        while nodesList.qsize()>1:
            smallNode0 = nodesList.get()[1]
            smallNode1 = nodesList.get()[1]
            node = treeNode(left = smallNode1,right = smallNode0)
            node.data = [None,int(smallNode0.data[1])+int(smallNode1.data[1])]
            #just add and then resort.  not sure how fast python can sort almost sorted list
            #but it's probably slower than the other version
            nodesList.put(tuple([node.data[1],node]))
            #faster than doing a sort for every iteration
            """addNode = False
            for m in range(len(nodesList)-1,-1,-1):
                if(nodesList[m].data[1] >= node.data[1]):
                    nodesList.insert(m+1,node)
                    addNode = True
                    break
            if(addNode==False):
                nodesList.insert(0,node)
            """
            #used for debugging
            """print "trees"
            nodesListCopy = Queue.PriorityQueue()
            for n in range(nodesList.qsize()):
                qn = nodesList.get()
                print "  "+str(qn[1].data)
                nodesListCopy.put(qn)
            nodesList = nodesListCopy
            """
        self.root = nodesList.get()[1]
        self.maxBits = 0
        self.findMaxBits(self.root)
        #print "maxbits:"+str(self.maxBits)
        self.treeCoding(self.root)
        self.bitsNeededDictionary = {}
        self.findBitsNeededDictionary(self.root)
    def findMaxBits(self,node,level = 0):
        if(node):
            if(self.maxBits < level):
                self.maxBits = level
            self.findMaxBits(node.left,level = level+1)
            self.findMaxBits(node.right,level = level+1)
    def treeCoding(self,node,parentCode = None,level = 0,isRight = False):
        if(node != None):
            #print level
            if(parentCode == None):
                node.code = 0
                node.bits = 0
            else:
                node.code = parentCode*2
                if(isRight):
                    node.code+=1
                node.bits = level
            self.treeCoding(level = level+1,node = node.right,isRight = True,parentCode = node.code)
            self.treeCoding(level = level+1,node = node.left,parentCode = node.code)
    def findNode(self, word):
        return self.findNodeImp(word = word,node = self.root)
    def findNodeImp(self, word, node):
        if(node):
            if(node.data[0] == word):
                return node
            else:
                left = self.findNodeImp(word,node = node.left)
                if(left):
                    return left
                right = self.findNodeImp(word,node = node.right)
                return right
        else:
            return None
    def bitsNeededForCoding(self,word):
        return bitsNeededDictionary[word]
    def findBitsNeededDictionary(self,node):
        if(node):
            if(node.data[0]):
                self.bitsNeededDictionary[node.data[0]] = node.bits
            else:
                if(node.left):
                    self.findBitsNeededDictionary(node.left)
                if(node.right):
                    self.findBitsNeededDictionary(node.right)


if(__name__ == "__main__"):
    
    if(len(sys.argv) == 2):
        set = speechSet.SpeechSet(sys.argv[1])
        tree = huffmanCodingTree(set.wordUsage)
    else:
        print "error, requires directory"