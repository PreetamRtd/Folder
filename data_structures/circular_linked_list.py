class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class CircularLinkedList:
  def __init__(self):
    self.head = None

  def prepend(self, data):
    new_node = Node(data)
    cur = self.head
    
    new_node.next = self.head

    if not self.head:
      new_node.next = new_node
    else:
      while cur.next != self.head:
        cur = cur.next
      cur.next = new_node   

    self.head = new_node

  def append(self, data):
    if not self.head:
      self.head = Node(data)
      self.head.next = self.head
    else:
      new_node = Node(data)
      cur = self.head
      new_node.next = self.head

      while cur.next != self.head:
        cur = cur.next

      cur.next = new_node

  def printList(self):
    cur = self.head  
    while cur:
      print(cur.data)
      cur = cur.next
      if cur == self.head:
        break  

# Driver Code
cllist = CircularLinkedList()
cllist.append(6)
cllist.prepend(4)
cllist.prepend(2)
cllist.append(8)

cllist.printList()