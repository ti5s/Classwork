class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBeginning(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while temp:
            print(f"{temp.data}", end=' >>> ')
            temp = temp.next
        print("None")


# Main block to run the code
if __name__ == '__main__':
    llist = LinkedList()

    # Insert nodes at the beginning
    llist.insertAtBeginning("Data")
    llist.insertAtBeginning("New")
    llist.insertAtBeginning("Is")
    llist.insertAtBeginning("Data")
    llist.insertAtBeginning("New")

    llist.printList()














#class linkedListsNode:
#    def __init__(self, value, nextNode=None):
 #       self.value = value
  #      self.nextNode = nextNode
#
#node1 = linkedListsNode("1")
#node2 = linkedListsNode("2")
#node3 = linkedListsNode("3")
#node4 = linkedListsNode("4")

#node1.nextNode = node2
#node2.nextNode = node3
#node3.nextNode = node4

#currentNode = node1


#while True:
 #   print(currentNode.value, ">>>", end=' ')

  #  if currentNode.nextNode is None:
   #     print("None")
    #    break

    #currentNode = currentNode.nextNode