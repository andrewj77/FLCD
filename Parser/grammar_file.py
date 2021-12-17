class Grammar:

    def __init__(self, file):
        self.__file = file
        self.__non_terminals = []
        self.__terminals = []
        self.__start = ''
        self.__productions = {}
        self.__read_from_file()

    @staticmethod
    def get_after_equal(line):
        return line.strip().split(' ')[2:]

    def __read_from_file(self):
        with open(self.__file) as f:
            self.__non_terminals = self.get_after_equal(f.readline())
            self.__terminals = self.get_after_equal(f.readline())
            self.__start = self.get_after_equal(f.readline())[0]
            f.readline()
            line = f.readline()[:-1]
            while line != '':
                left, right = line.split('->')
                left = left.strip()
                right = [p.strip() for p in right.split('|')]
                self.__productions[left] = right
                line = f.readline()[:-1]

    def get_non_terminals(self):
        return self.__non_terminals

    def get_terminals(self):
        return self.__terminals

    def get_start(self):
        return self.__start

    def get_productions(self):
        return self.__productions

    def get_productions_for(self, terminal):
        if terminal not in self.__terminals:
            return None
        return self.__productions[terminal]

    def check_cfg(self):
        for key in self.__productions:
            if key not in self.__non_terminals:
                return False
            for val in self.__productions[key]:
                for elem in val:
                    for char in elem:
                        if char not in self.__non_terminals and char not in self.__terminals:
                            return False
        return True
