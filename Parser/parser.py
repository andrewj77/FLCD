class Parser:
    def __init__(self, grammar):
        self.__grammar = grammar
        self.__non_terminals = self.__grammar.get_non_terminals()
        self.__terminals = self.__grammar.get_terminals()
        self.__productions = self.__grammar.get_productions()

        self.__augmented_grammar = {}
        self.build_augmented_grammar()
        print(self.__augmented_grammar)

    def build_augmented_grammar(self):
        self.__augmented_grammar = {'S\'': [['.', 'S']]}
        for nt in self.__productions:
            self.__augmented_grammar[nt] = []
            for w in self.__productions[nt]:
                w = list(w)
                self.__augmented_grammar[nt].append(['.'] + w)


