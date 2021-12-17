class Parser:
    def __init__(self, grammar):
        self.__grammar = grammar
        self.__non_terminals = self.__grammar.get_non_terminals()
        self.__terminals = self.__grammar.get_terminals()
        self.__productions = self.__grammar.get_productions()

        self.__augmented_grammar = {}
        self.build_augmented_grammar()
        self.first_closure = {"S'": [self.__augmented_grammar["S'"][0]]}
        self.closure(self.first_closure, self.__augmented_grammar["S'"][0])

        self.canonical_collection()

    def build_augmented_grammar(self):
        self.__augmented_grammar = {"S'": [['.', 'S']]}
        for nt in self.__productions:
            self.__augmented_grammar[nt] = []
            for w in self.__productions[nt]:
                w = list(w)
                self.__augmented_grammar[nt].append(['.'] + w)

    def closure(self, closures, transition):
        di = transition.index('.')
        transitions = self.__augmented_grammar
        if di + 1 == len(transition):
            return
        after_dot = transition[di + 1]
        if after_dot in self.__non_terminals:
            nt = after_dot
            if nt not in closures:
                closures[nt] = transitions[nt]
            else:
                closures[nt] += transitions[nt]
            for tr in transitions[nt]:
                self.closure(closures, tr)

    def go_to(self, key, transition):
        shifted = self.shift_dot(transition)
        if shifted == {}:
            return {}
        closures = {key: [shifted]}
        self.closure(closures, shifted)
        return closures

    def canonical_collection(self):
        queue = [self.first_closure]
        states = []

        while len(queue) > 0:
            state = queue.pop(0)
            states.append(state)
            for key in state:
                for tr in state[key]:
                    closures = self.go_to(key, tr)
                    if closures not in states and closures not in queue and closures != {}:
                        queue.append(closures)

        parsing_table = self.parsing_table(states)
        productions_string = self.parse(parsing_table)
        print(productions_string)

        derivation_string = ""
        output = ""
        for current_production_index in productions_string:
            production_index = 0
            for nt in self.__productions:
                for production in self.__productions[nt]:
                    production_index += 1
                    if production_index == current_production_index:
                        if output == "":
                            output += production
                        else:
                            output = self.rreplace(output, nt, production, 1)
                        derivation_string += output + " -> "
        derivation_string = derivation_string[:-4]
        print(derivation_string)

    def parsing_table(self, states):
        table = {}
        prods = []
        for k in self.__productions:
            for l2 in self.__productions[k]:
                prods.append(l2)
        for index in range(len(states)):
            table[index] = ('', [])
        for index, state in enumerate(states):
            for key in state:
                transitions = state[key]
                for transition in transitions:
                    di = transition.index('.')
                    if di == len(transition) - 1:
                        prod = ''
                        for el in transition:
                            if el != '.':
                                prod += el
                        if prod == 'S':
                            table[index] = ('ACCEPT', [])
                        else:
                            for index2, prod2 in enumerate(prods):
                                if prod2 == prod and table[index][0] == '':
                                    table[index] = ('REDUCE' + str(index2+1), [])
                                elif prod2 == prod:
                                    if index2 != int(table[index][0][-1]):
                                        print('Error! Conflict at state ' + str(index))
                                        return {}
                    else:
                        after_dot = transition[di+1]
                        closures = self.go_to(key, transition)
                        for index2, state2 in enumerate(states):
                            if state2 == closures:
                                if table[index][0] == '':
                                    table[index] = ('SHIFT', [])
                                l = table[index][1]
                                l.append((after_dot, index2))
        return table

    def parse(self, parsing_table):
        sequence = input("Give sequence: ")
        print(sequence)
        print(self.__productions)
        print(parsing_table)

        work_stack = [0]
        input_stack = sequence
        output_band = []

        action = parsing_table[work_stack[-1]][0]
        while action != 'ACCEPT':
            print(action)

            if action == 'SHIFT':
                work_stack.append(input_stack[0])
                input_stack = input_stack[1:]

                for item in parsing_table[work_stack[-2]][1]:
                    if item[0] == work_stack[-1]:
                        work_stack.append(item[1])
                        break

                print(work_stack)
                print(input_stack)

            if action[:-1] == 'REDUCE':
                production_index = 0
                for nt in self.__productions:
                    for production in self.__productions[nt]:
                        production_index += 1
                        if production_index == int(action[-1]):
                            print(production)
                            output_band.append(production_index)

                            work_stack = work_stack[:(-1*2*len(production))]
                            work_stack.append(nt)
                            for item in parsing_table[work_stack[-2]][1]:
                                if item[0] == work_stack[-1]:
                                    work_stack.append(item[1])
                                    break

                            print(work_stack)

            action = parsing_table[work_stack[-1]][0]

        return output_band[::-1]

    @staticmethod
    def get_action():
        pass


    @staticmethod
    def can_shift(transition):
        di = transition.index('.')
        return len(transition) > di + 1

    @staticmethod
    def shift_dot(transition):
        di = transition.index('.')
        if not Parser.can_shift(transition):
            # print('Cannot shift')
            return {}
        if len(transition) > di + 2:
            r = transition[di + 2:]
        else:
            r = []
        return transition[:di] + [transition[di+1]] + ['.'] + r

    @staticmethod
    def rreplace(input_string, old, new, occurrence):
        li = input_string.rsplit(old, occurrence)
        return new.join(li)
