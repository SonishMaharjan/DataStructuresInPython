class Node:
    def __init__(self,value =None):
        self.prev = None
        self.item = value
        self.next = None

class DLinkList:
    def __init__(self):
        self.head = Node()
        self.noOfItem = 0

    def insertAtEnd(self,value):
        counterNode = self.head
        node = Node(value)
        while counterNode.next != None:
            counterNode = counterNode.next

        counterNode.next = node
        node.prev = counterNode

        self.noOfItem = self.noOfItem +1

    def insertAtFront(self,value):
        node = Node(value)
        node.prev = self.head
        temp = self.head.next
        self.head.next = node
        node.next = temp
        temp.prev = node
        self.noOfItem = self.noOfItem +1

    def insertAtIndex(self,value,index):
        if index <=0:
            self.insertAtFront(value)
            return
        if index > self.noOfItem-1:
            self.insertAtEnd(value)
            return

        counterNode = self.head.next
        counter = 0
        while counter < index-1:
            counter = counter+1
            counterNode = counterNode.next

        node= Node(value)
        node.prev = counterNode
        node.next = counterNode.next
        counterNode.next = node


    def traverserFront(self):
        itemList =[]
        counterNode = self.head
        while counterNode.next != None:
            counterNode = counterNode.next
            itemList.append(counterNode.item)
        return itemList

    def traverseBack(self):
        counterNode = self.head
        counter = 0
        itemList = []
        while counter<self.noOfItem:

            counterNode = counterNode.next
            counter =1+counter


        while counterNode.prev != None:
            itemList.append(counterNode.item)
            counterNode = counterNode.prev

        return  itemList


dList = DLinkList()
dList.insertAtEnd(3)
dList.insertAtEnd(34)
dList.insertAtFront(233)
dList.insertAtFront(369)
dList.insertAtEnd(3434)

print(dList.traverserFront())
#print(dList.traverseBack())
dList.insertAtIndex(300,5)
print(dList.traverserFront())
print(dList.traverseBack())
print("no of iten:",dList.noOfItem)



