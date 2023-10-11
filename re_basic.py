import re #regular expressions

text = ('But the wave – sometimes known as Big Mama – has changed that. Winter used to be dead in Nazaré: many restaurants wouldn’t even bother to open.')

# checks if 'But' matches the beginning of the text
match = re.match('But', text)
print(match)

# finds 'dead' in the text and writes its position
search = re.search('dead', text)
print(search)
print(search.group(0))

# finds all 'the' in the text
findall = re.findall('the', text)
print(findall)

# splits the text into separate parts by the letter 'o'
split = re.split('o', text)
print(split)

# substitudes the word 'Winter' by 'Autumn' in the text
substitude = re.sub('Winter', 'Autumn', text)
print(substitude)

# compile helps us decrease the amount of repeating code. this piece finds the word 'wave' in the text
pattern = re.compile('wave')
result = pattern.search(text)
print(result)
