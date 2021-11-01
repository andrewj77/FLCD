

class PIF:
    def __init__(self):
        self.__content = []

    def add(self, token, position):
        self.__content.append((token, position))

    def __str__(self):
        output = ''
        for el in self.__content:
            output += el[0] + ' -> ' + str(el[1]) + '\n'
        return output
