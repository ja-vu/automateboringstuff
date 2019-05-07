# Lecture 26

import re


resume = 'Cell: 415-555-9999 Work: 212-555-0000'

# findall() method searches for all matching re pattern
phoneRegex1 =re.compile(r'\d\d\d-\d\d\d\-\d\d\d\d')
print(phoneRegex1.findall('Cell: 415-555-9999 Work: 212-555-0000'))


# findall() with groups
phoneRegex2 = re.compile(r'((\d\d\d)-(\d\d\d-\d\d\d\d))')
print(phoneRegex2.findall(resume))

# character class \e

digitRegex = re.compile(r'\d')



lyrics = '12 drummers drumming, 11 pipers piping, 10 lords a leaping, 9 ladies dancing, 8 maids a milking, 7 swans a swimming, 6 geese a laying' \
         '5 golden rings, 4 calling birds, 3 french hens, 2 turtle doves, and 1 partridge in a pear tree'

# + means 1 or more
# \s means Any Space, tab or newline character
# \w means any letter, numeric digit, or the underscore character

xmasRegex = re.compile(r'\d+\s\w+')
print(xmasRegex.findall(lyrics))


vowelRegex1 = re.compile(r'[aeiouAEIOU]') # r'(a|e|i|o|u')
print(vowelRegex1.findall('Robocop eats babyfood'))

doublevowelRegex = re.compile(r'[aeiouAEIOU]{2}')
print(doublevowelRegex.findall('Robocop eats babyfood'))

# Negative
consonantRegex = re.compile(r'[^aeiouAEIOU]') # r'(a|e|i|o|u')
print(consonantRegex.findall('Robocop eats babyfood'))






