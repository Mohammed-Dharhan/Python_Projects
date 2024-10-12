class Node:
    def __init__(self,data = None,next = None):
        self.data = data
        self.next = next
        
        
class linkedList:
    def __init__(self):
        self.head = None
        
        
    def add(self,data):
        newNode = Node(data) #create a new node
        if self.head: #if head is not empty
            current = self.head
            while (current.next): #traverse the linked list
                current = current.next #updata each time
            current.next = newNode #we've reached the tail set it to equal the newnode
        else:
            self.head = newNode
            
    def remove(self,data):
        if self.head is None: #if the list is empty
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while(current.next):
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next
        
if __name__ == "__main__":
  ll = linkedList()
  ll.add(5)
  ll.add(89)
  ll.add(100)
  curr = ll.head
  while(curr):
      print(curr.data)
      curr = curr.next