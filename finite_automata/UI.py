
class UI:

    def __init__(self, FA):
        self.__FA = FA

    @staticmethod
    def display_menu():
        print(
            '1 - Display all states\n' +
            '2 - Display final states\n' +
            '3 - Display the initial state\n' +
            '4 - Display the alphabet\n' +
            '5 - Display all transitions\n' +
            '6 - Check if sequence is accepted by FA'
        )

    def all_states(self):
        print(self.__FA.get_all_states())

    def final_states(self):
        print(self.__FA.get_final_states())

    def initial_state(self):
        print(self.__FA.get_initial_state())

    def alphabet(self):
        print(self.__FA.get_alphabet())

    def transitions(self):
        print(self.__FA.get_transitions())

    def check_sequence(self):
        sequence = input('Input sequence: ')
        if self.__FA.is_valid_sequence(sequence):
            print('Accepted sequence!')
        else:
            print('Sequence not accepted!')

    def run(self):
        commands = {
            '1': self.all_states,
            '2': self.final_states,
            '3': self.initial_state,
            '4': self.alphabet,
            '5': self.transitions,
            '6': self.check_sequence
        }

        while True:
            self.display_menu()
            cmd = input('>> ')
            if cmd == '0':
                return
            elif cmd in commands:
                commands[cmd]()
            else:
                print('Invalid option\n')
