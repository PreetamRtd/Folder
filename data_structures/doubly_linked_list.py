class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
    self.prev = None

class DoublyLinkedList:
  def __init__(self):
    self.head = None
  
  def append(self, data):
    new_node = Node(data)  
    if self.head is None:
        self.head = new_node
        return
    curr = self.head
    while curr.next:
        curr = curr.next
    curr.next = new_node  
    new_node.prev = curr
  
  def prepend(self, data):
    new_node = Node(data)
    new_node.next = self.head
    if self.head is not None:
      self.head.prev = new_node
    self.head = new_node
   
  def printList(self):  
    temp = self.head
    while temp:
      print(temp.data)
      temp = temp.next

# Driver code
dll = DoublyLinkedList()
dll.prepend(2)
dll.append(1) 
dll.prepend(4)
dll.append(3)

dll.printList()