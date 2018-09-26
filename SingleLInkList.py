class Node:
    def __init__(self,value=None):
        self.value = value
        self.nextNode = None

class SLinkList:

    def __init__(self):
        self.headNode = Node()
        self.noOfItems=0 #increments when item are adden and decrement when removed

    def insertAtEnd(self,value):
        newNode= Node(value)
        self.noOfItems += 1
        #check if list is empty
        if self.headNode.nextNode == None:
            self.headNode.nextNode = newNode
        else:
            counterNode = self.headNode.nextNode
            while counterNode.nextNode != None:
                counterNode = counterNode.nextNode
            counterNode.nextNode = newNode

    def insertAtStart(self,value):
        newNode= Node(value)
        self.noOfItems+=1
        if self.headNode.nextNode == None:
            self.headNode.nextNode = newNode
        else:
            tempNode = self.headNode.nextNode
            self.headNode.nextNode = newNode
            newNode.nextNode = tempNode

    #insert at the mid of list according to key
    def insertAtKey(self,value,key):
        count =0
        #insertAtStart is key =<0
        if(key <=  0):
            self.insertAtStart(value)
        #insert at end if key > noOfitems
        elif key > (self.noOfItems-1):
            self.insertAtEnd(value)
        else:
            counterNode = self.headNode.nextNode
            while count< key-1:
                counterNode = counterNode.nextNode
                count +=1

            leftNode= counterNode
            rightNode = counterNode.nextNode
            newNode = Node(value)
            leftNode.nextNode = newNode
            newNode.nextNode = rightNode







    def printList(self):
        counterNode = self.headNode

        while counterNode.nextNode != None:
            counterNode = counterNode.nextNode
            print(counterNode.value)


lis = SLinkList()
lis.insertAtStart(1)
lis.insertAtEnd(2)
lis.insertAtEnd(3)
lis.insertAtEnd(5)
lis.insertAtEnd(6)
lis.printList()
print("inser fisr")
lis.insertAtStart(600)
lis.printList()

lis.insertAtKey(4,1)
print("afeter insertd at key")
lis.printList()