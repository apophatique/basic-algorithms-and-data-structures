class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.current = None

    def append(self, obj):
        node = Node(obj)

        if self.is_empty():
            self.head = node
            self.current = node
        else:
            node.set_previous(self.current)
            self.current.set_next(node)
            self.current = node


    def remove(self, value):
        pass



    def get_current_value(self):
        return self.current.get_value()

    def size(self):
        tmp_node = self.head
        count = 0
        while tmp_node is not None:
            count = count + 1
            tmp_node = tmp_node.get_next()
        return count

    def show(self):
        tmp_node = self.head
        count = 0
        while tmp_node is not None:
            print(tmp_node.get_value(),
                  tmp_node.get_next(),
                  tmp_node.get_previous(),
                  sep=' ')
            tmp_node = tmp_node.get_next()
        print('\n')

    def is_empty(self):
        return self.head is None


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

    def get_next(self):
        return self.next

    def get_previous(self):
        return self.previous

    def set_next(self, obj):
        self.next = obj

    def set_previous(self, obj):
        self.previous = obj

    def get_value(self):
        return self.value

    def set_value(self, obj):
        self.value = obj


linked_list = DoubleLinkedList()
linked_list.append(42)
linked_list.append(50)
linked_list.append(68)
linked_list.show()

linked_list.remove(50)
linked_list.show()

linked_list.remove(42)
linked_list.show()

linked_list.remove(68)
linked_list.show()
