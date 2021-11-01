

class Scanner:

    def __init__(self, separators, operators, reserved):
        self.separators = separators
        self.operators = operators
        self.reserved = reserved

    def can_be_operator(self, char):
        for o in self.operators:
            if char in o:
                return True
        return False

    def extract_operator(self, line, index):
        token = ''
        while index < len(line) and self.can_be_operator(line[index]):
            token += line[index]
            index += 1

        return token, index

    @staticmethod
    def extract_string(line, index):
        token = ''
        quotes = 0
        while index < len(line) and quotes < 2:
            if line[index] == '\'':
                quotes += 1
            token += line[index]
            index += 1
        return token, index

    def parse_line(self, line):
        position = 0
        tokens = []
        elem = ''
        while position < len(line):
            char = line[position]
            if char in self.separators:
                if len(elem) > 0:
                    tokens.append(elem)
                tokens.append(char)
                position, elem = position + 1, ''
            elif char == '\'':
                if len(elem) > 0:
                    tokens.append(elem)
                elem, position = self.extract_string(line, position)
                tokens.append(elem)
                elem = ''
            elif self.can_be_operator(char):
                if len(elem) > 0:
                    tokens.append(elem)
                op, position = self.extract_operator(line, position)
                tokens.append(op)
                elem = ''
            else:
                elem += char
                position += 1
        if elem:
            tokens.append(elem)
        return tokens




