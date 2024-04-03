class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
    self.prev = None

class CircularDoublyLinkedList:
  def __init__(self):
    self.head = None

  def prepend(self, data):
    new_node = Node(data)
    cur = self.head
    
    new_node.next = self.head

    if self.head is not None:
      while cur.next != self.head:
        cur = cur.next
      cur.next = new_node
      new_node.prev = cur   

    else:
      new_node.prev = new_node   

    self.head = new_node

  def append(self, data):
    if not self.head:
      self.head = Node(data)
      self.head.next = self.head
      self.head.prev = self.head
    else:
      new_node = Node(data)
      cur = self.head
      new_node.next = self.head

      while cur.next != self.head:
        cur = cur.next

      cur.next = new_node
      new_node.prev = cur
      self.head.prev = new_node

  def printList(self):
    cur = self.head 
    while cur:
      print(cur.data)
      cur = cur.next
      if cur == self.head:
        break

# Driver program
dll = CircularDoublyLinkedList()
dll.append(6)
dll.prepend(4)
dll.prepend(2)
dll.append(8)

dll.printList()



