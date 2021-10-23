

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.last = None

    def push1(self, data):
        if self.head == None:
            self.head = Node(data)
            self.last = self.head
        else:
            el = Node(data)
            self.last.next = el
            self.last = el

    def get_concatinated(self):
        temp = self.head
        o = ''
        while(temp):
            o = o + temp.data
            temp = temp.next
        return o


    def printme(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next


