class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None
  
  def printList(self):
    temp = self.head
    while temp:
      print(temp.data, end=" ")
      temp = temp.next

  def push(self, new_data):
    new_node = Node(new_data)
    new_node.next = self.head
    self.head = new_node
  
  def insertAfter(self, prev_node, new_data):
    if prev_node is None:
      print("The given previous node must inLinkedList.")
      return
    
    new_node = Node(new_data)
    new_node.next = prev_node.next
    prev_node.next = new_node

  def append(self, new_data):
    new_node = Node(new_data)

    if self.head is None:
      self.head = new_node
      return

    last = self.head
    while last.next:
      last = last.next

    last.next = new_node

# Driver code
list = LinkedList()
list.head = Node(1)
list.append(2)
list.push(3)
list.insertAfter(list.head.next,5)
list.printList()