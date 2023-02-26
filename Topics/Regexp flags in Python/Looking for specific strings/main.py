import re

string = input()

regexp = 'b.*l'


if re.match(regexp, string, flags=re.I + re.S + re.X):
    print(string)
else:
    print('No match')
