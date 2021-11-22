from grammar import Grammar

grammar = Grammar('g1.txt')

print(grammar.get_non_terminals())
print(grammar.get_terminals())
print(grammar.get_start())
print(grammar.get_productions())