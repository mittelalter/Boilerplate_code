class Node:
    """Node class definition"""

    def __init__(self, data):
        self.data = data  # Data, what node saves
        self.next = None  # Reference about next node


head_node = Node(2)
node_1 = Node(3)
node_2 = Node(5)
node_3 = Node(7)
tail_node = Node(11)

iterator = head_node


while iterator is not None:
    print(iterator.data)
    iterator = iterator.next
