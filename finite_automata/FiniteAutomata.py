
class FA:

    def __init__(self, file):
        self.__file = file
        self.__all_states = []
        self.__alphabet = []
        self.__initial_state = ''
        self.__final_states = []
        self.__transitions = {}
        self.__read_from_file()

    @staticmethod
    def get_after_equal(line):
        return line.strip().split(' ')[2:]

    def __read_from_file(self):
        with open(self.__file) as f:
            self.__all_states = self.get_after_equal(f.readline())
            self.__alphabet = self.get_after_equal(f.readline())
            for i in range(len(self.__alphabet)):
                if self.__alphabet[i] == '<space>':
                    self.__alphabet[i] = ' '
            self.__initial_state = self.get_after_equal(f.readline())[0]
            self.__final_states = self.get_after_equal(f.readline())
            f.readline()
            line = f.readline()[:-1]
            while line != '':
                fr = line[1]
                through = line[3]
                to = line[9]
                if (fr, through) in self.__transitions:
                    self.__transitions[(fr, through)].append(to)
                else:
                    self.__transitions[(fr, through)] = [to]
                line = f.readline()[:-1]

    def is_deterministic(self):
        for v in self.__transitions.values():
            if len(v) > 1:
                return False
        return True

    def is_valid_sequence(self, sequence):
        if not self.is_deterministic():
            print(self.__alphabet)
            print('FA must be deterministic')
            return
        state = self.__initial_state
        for el in sequence:
            if (state, el) in self.__transitions:
                state = self.__transitions[(state, el)][0]
            else:
                return False
        return state in self.__final_states

    def get_all_states(self):
        return self.__all_states

    def get_alphabet(self):
        return self.__alphabet

    def get_initial_state(self):
        return self.__initial_state

    def get_final_states(self):
        return self.__final_states

    def get_transitions(self):
        return self.__transitions

    def __str__(self):
        return 'All_states: ' + str(self.__all_states) + '\n' +\
               'Alphabet: ' + str(self.__alphabet) + '\n' + \
               'Initial state: ' + self.__initial_state + '\n' + \
               'Final states: ' + str(self.__final_states) + '\n' + \
               'Transition function: ' + str(self.__transitions) + '\n'
