import re

# "^" means needs to have "Hello" at the beginning
beginsWithHelloRegex = re.compile(r'^Hello')
print(beginsWithHelloRegex.search("He said 'Hello' there!"))


# "$" means that this needs to be at the end of the string
endsWithWorldRegex = re.compile(r'world!$')
print(endsWithWorldRegex.search("Hello world!"))

# ^ and $ means it has to match the entire text
allDigitsRegex = re.compile(r'^\d+$')
print(allDigitsRegex.search("123d"))

# . means can have any single characters
atregex = re.compile(r'.at')
print(atregex.findall('The cat in the hat sat on the flat mat'))



atregex2 = re.compile(r'.{1,2}at')
print(atregex2.findall('The cat in the hat sat on the flat mat'))


# .* to match anything -- 1) dot means any single characters. 2) star means 0 or more
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
print(nameRegex.findall('First Name: Al Last Name: Sweigart'))

# .* is greedy mode (new line excluded)
# .*? is non-greedy
serve = '<To serve humans> for dinner.>'
nongreedy = re.compile(r'<(.*?)>')
print(nongreedy.findall(serve))

greedy = re.compile(r'<(.*)>')
print(greedy.findall(serve))

prime = 'Serve the public trust. \nProtect the innocent. \nUpload the law'
print(prime)

dotStar = re.compile(r'.*')
print(dotStar.search(prime))

# re.DOTALL --> Truly takes everything into consideration even end of lines
dotStar2 = re.compile(r'.*',re.DOTALL)
print(dotStar2.search(prime))

#re.IgnoreCASE --> ignores capital cases
vowelRegex = re.compile(r'[aeiou]',re.IGNORECASE)
print(vowelRegex.findall('Al, why does your programming book talk about Robocop so much?'))
