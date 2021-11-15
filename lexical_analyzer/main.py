from SymbolTable import ST
from Scanner import Scanner
from ProgramInternalForm import PIF
from finite_automata.FiniteAutomata import FA
import re


class Parser:

    def __init__(self):
        self.ST = ST(20)
        self.PIF = PIF()
        self.separators, self.operators, self.reserved = self.read_tokens()
        self.Scanner = Scanner(self.separators, self.operators, self.reserved)

    @staticmethod
    def is_identifier(token):
        return re.match(r'^[a-zA-Z]([a-zA-Z]|[0-9])*$', token) is not None

    @staticmethod
    def is_constant(token):
        return re.match(r'^(0|[+-]?[1-9][0-9]*)$|^\'.*\'$', token) is not None

    @staticmethod
    def read_tokens():
        separators = []
        operators = []
        reserved = []
        f = open('../lab1b/token.txt', 'r', encoding='utf-8-sig')
        lines = f.readlines()
        i = 0
        while i < len(lines):
            line = lines[i][:-1]
            if i < 11:
                if line == 'space':
                    separators.append(' ')
                else:
                    separators.append(line)
            elif i < 28:
                operators.append(line)
            else:
                reserved.append(line)
            i += 1
        return separators, operators, reserved

    def run(self):
        file = '../lab1a/p1.txt'
        faC = FA('./constant_fa.txt')
        faI = FA('./identifier_fa.txt')
        error = ''
        with open(file, 'r') as program:
            lines = 0
            for line in program:
                lines += 1
                tokens = self.Scanner.parse_line(line.strip())
                for i in range(len(tokens)):
                    if tokens[i] in self.separators + self.operators + self.reserved:
                        if tokens[i] != ' ':
                            self.PIF.add(tokens[i], (-1, -1))
                    elif faI.is_valid_sequence(tokens[i]):  # self.is_identifier(tokens[i]):
                        idd = self.ST.add(tokens[i])
                        self.PIF.add("id", idd)
                    elif faC.is_valid_sequence((tokens[i])):  # self.is_constant(tokens[i]):
                        const = self.ST.add(tokens[i])
                        self.PIF.add("const", const)
                    else:
                        error = 'Lexical error at line ' + str(lines) + ', token ' + tokens[i] + '\n'
                        break
                if len(error) > 0:
                    break
        with open('pif.out', 'w') as w:
            w.write(str(self.PIF))
        with open('st.out', 'w') as w:
            w.write(str(self.ST))
        if len(error) > 0:
            print(error)
        else:
            print('No lexical errors')


parser = Parser()
parser.run()

