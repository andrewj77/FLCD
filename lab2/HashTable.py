

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        l = [self.value]
        n = self
        while n.next is not None:
            n = n.next
            l.append(n.value)
        return str(l)

    def __repr__(self):
        l = [self.value]
        n = self
        while n.next is not None:
            n = n.next
            l.append(n.value)
        return str(l)


class HashTable:
    def __init__(self, size):
        self.__content = [None] * size
        self.__size = size

    def hash(self, key):
        ascii_sum = 0
        for char in key:
            ascii_sum += ord(char)
        return ascii_sum % self.__size

    def insert(self, key):
        index = self.hash(key)
        node = self.__content[index]
        if node is None:
            self.__content[index] = Node(key)
            return
        last = node
        pos = 0
        while node is not None:
            if node.value == key:
                return index, pos
            last = node
            node = node.next
            pos += 1
        last.next = Node(key)

    def remove(self, key):
        index = self.hash(key)
        node = self.__content[index]
        it = None
        while node is not None and node.value != key:
            it = node
            node = node.next
        if node is None:
            return None
        res = node.value
        if it is None:
            self.__content[index] = node.next
        else:
            it.next = it.next.next
        return res

    def get_position(self, key):
        index = self.hash(key)
        node = self.__content[index]
        pos = 0
        while node is not None:
            if node.value == key:
                return index, pos
            pos += 1
            node = node.next
        return -1, -1

    def contains(self, key):
        return self.get_position(key) != (-1, -1)

    def get_content(self):
        return self.__content


