# Write a program that inputs two strings, swaps their values using tuples and outputs them.

string1 = input('first string: ')
string2 = input('second string: ')

x = string2[:2] + string1[2:]
y = string1[:2] + string2[2:]
 

print("Your first has become :- ",x)
print("Your second has become :- ",y)

#-------------------
string1 = input('first string: ')
string2 = input('second string: ')


string1, string2 = string2, string1   

print("Your first string has become: ", string1)
print("Your second string has become: ", string2)

#PITANJE
#zanima me sto radi linija koda 19

# Write a program that initializes 3 strings and starts the for loop that runs 10 times. 
# In for loop, it rotates 3 strings (str1=> str2, str2=>str3, str3=>str1) using tuples and writes strings in the same line, with number of iteration: 

# 0: str1 str2 str3
# 1: str3 str1 str2
# 2: str2 str3 str1


string1 = input('first string: ')
string2 = input('second string: ')
string3 = input('third string: ')



for i in range(10):  #tu me zanima zasto mi print nespravno radi ako je bez funkcije i viticastih zagrada i opet e zanima sta radi linija 44 da sama zna tako vrtit
    print(f"{i}: {string1} {string2} {string3}")
    string1, string2, string3 = string3, string1, string2
   


# Write a program that asks for two strings.

# Then it should print the following:

# - all characters that can be found in strings, but without repetition (for 'abc' and 'bcd', it should print 'abcd')
# - all the characters that exist in both strings (for 'abc' and 'bcd', it should print 'bc')
# - all the characters that exist in first but not in second string (for 'abc' and 'bcd', it should print 'a')
# - all characters in strings, but but without intersection (for 'abc' and 'bcd', it should print 'ad')



def unique_characters(s1, s2):
  unique_chars = set()
  for ch in s1:
    unique_chars.add(ch)
  for ch in s2:
    unique_chars.add(ch)
  return ''.join(unique_chars)

def common_characters(s1, s2):
  common_chars = set()
  for ch in s1:
    if ch in s2:
      common_chars.add(ch)
  return ''.join(common_chars)

def first_not_second(s1, s2):
  not_second = ''
  for ch in s1:
    if ch not in s2:
      not_second += ch
  return not_second

def no_intersection(s1, s2):
  no_intersection = ''
  for ch in s1:
    if ch not in s2:
      no_intersection += ch
  for ch in s2:
    if ch not in s1:
      no_intersection += ch
  return no_intersection


s1 = input('first string: ')
s2 = input('second string: ')

print('All characters:', unique_characters(s1, s2))
print('Common characters:', common_characters(s1, s2))
print('Characters in first but not second:', first_not_second(s1, s2))
print('Characters without intersection:', no_intersection(s1, s2))


##PITANJE
#ovo mi je bilo dost tesko, rijesenje sam uspijela nekako nac na netu al iskreno ni ne kuzim bas sta ovo tocno radi


# Write a program to enter survey data on students and their favorite programming language (key: name, value: favorite programming language).
# Allow the user to enter survey results as long as he wants. Ensure that survey entries are unique (the key to making the survey unique is the username). 

# Print the survey results in the form:
# - Name:
# - Favorite language:


survey = {} 

while True:
  
  name = input('Enter the name: ')
  language = input('Enter the favorite language: ')


  survey[name] = language

  more = input('Do you want to enter more survey results (y/n)? ')
  if more.lower() != 'y':
    break

for name, language in survey.items():
  print(f'Name: {name} favorite language is: {language}')



# Write a program that will parse the following string: `key1=value1;key2=value2;key3=value3`.
# Use an appropriate structure for that.

s = 'key1=value1;key2=value2;key3=value3'
items = s.split(';')  

parsed = {}

for item in items:
  key, value = item.split('=')  
  parsed[key] = value

print(parsed)




