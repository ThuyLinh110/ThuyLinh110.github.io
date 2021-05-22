class Node:
    def __init__(self):
        self.data = None
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = Node()
        self.curNode = self.head
    def insertNodeAtEnd(self, data):
        node = Node()
        node.data = data
        node.next = None
        if self.head.data == None:
            self.head = node
            self.curNode = node
        else:
            self.curNode.next = node
            self.curNode = node
    def insertNodeAtBegin(self,data):
         node = Node()
         node.data = data
         if self.head ==None:
             self.head=node
             self.curNode=node
         else:
             node.next=self.head
             self.head=node 
    def findMiddle(self):
        x_ptr=self.head
        y_ptr=self.head
        while (y_ptr != None and y_ptr.next!=None):
            y_ptr=y_ptr.next.next
            x_ptr=x_ptr.next
        return x_ptr.data
    def removeListAtEnd(self):
        node =self.head
        while(node.next.next != None):
            node=node.next
        node.next=node.next.next
        self.curNode=node
    def printList(self):
        temp = self.head 
        while (temp): 
            print (temp.data,end="->")
            temp = temp.next
        print()   
l = LinkedList()
l.insertNodeAtEnd(1)
l.insertNodeAtEnd(2)
l.insertNodeAtEnd(3)
l.insertNodeAtEnd(4)
l.insertNodeAtEnd(5)
k=int(input("So vi tri dich phai: "))
l.printList()
print("Middle: ",l.findMiddle())
for i in range(k):
    l.insertNodeAtBegin(l.curNode.data)
    l.removeListAtEnd()
l.printList()