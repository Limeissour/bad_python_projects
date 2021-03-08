greeting = input('Are you ready for the game?: ')
if greeting == 'yes':
    print("Okay! let's start!\nFirst you'll have to read the paragraph and then fill in the adjectives")
else:
    print("Okay we'll start either way!\nFirst you'll have to read the paragraph and then fill in the adjectives")
input('Press Enter > ')
print('''
                                Star Wars
    Star Wars is a __adjective1__ __noun1__ of __adjective2__ versus evil 
    in a __noun;place2__ far far away. There are __adjective3__ battles between
    __adjective4__ __plural_noun;vehicle1__ in __adjective5__ space and 
    __adjective6__ duels with __plural noun2__ called __adjective7__ sabers. 
    __plural noun3__ called 'droids' are helpers and__plural noun4__ to the heroes.
    A __adjective8__ power called The __noun3__ __verb1__s people to do __adjective9__
    things, like __verb2__ __plural noun5__. The Jedi __plural noun;type of job6__
    use the Force for the __adjective10__ side and the Sith __verb3__ it for the
    __adjective11__ side.
''')

print('Type the following- ')
adjective1 = input('adjective: ')
noun1 = input('noun: ')
adjective2 = input('adjective: ')
noun2 = input('noun: ')
adjective3 = input('adjective: ')
adjective4 = input('adjective: ')
plural_noun1 = input('plural_noun: ')
adjective5 = input('adjective: ')
adjective6 = input('adjective: ')
plural_noun2 = input('plural_noun: ')
adjective7 = input('adjective: ')
plural_noun3 = input('plural_noun: ')
plural_noun4 = input('plural_noun: ')
adjective8 = input('adjective: ')
noun3 = input('noun: ')
verb1 = input('verb: ')
adjective9 = input('adjective: ')
verb2 = input('verb: ')
plural_noun5 = input('plural_noun: ')
plural_noun6 = input('plural_noun: ')
adjective10 = input('adjective: ')
verb3 = input('verb: ')
adjective11 = input('adjective: ')

input('Press Enter > ')
print(f'''                          
                                Star Wars
    Star Wars is a {adjective1} {noun1} of {adjective2} versus evil 
    in a {noun2} far far away. There are {adjective3} battles between
    {adjective4} {plural_noun1} in {adjective5} space and 
    {adjective6} duels with {plural_noun2} called {adjective7}sabers. 
    {plural_noun3}'droids' are helpers and {plural_noun4} to the heroes.
    A {adjective8} power called The {noun3} {verb1}s people to do 
    {adjective9} things, like {verb2} {plural_noun5}. The Jedi {plural_noun6} 
    use the Force for the {adjective10} side and the Sith {verb3} it for the 
    {adjective11} side.''')
