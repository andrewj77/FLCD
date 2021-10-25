from HashTable import HashTable


class ST:

    def __init__(self, size):
        self.__table = HashTable(size)

    def __str__(self):
        return str(self.__table.get_content())

    def add(self, key):
        return self.__table.insert(key)

    def remove(self, key):
        return self.__table.remove(key)

    def get_position(self, key):
        return self.__table.get_position(key)

    def contains(self, key):
        return self.__table.contains(key)

