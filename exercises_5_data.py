'''# Write a program that initializes the list with 5 names.
# Reverse each name using a for loop, and print original and reversed list.

arr = ["Ivanka", "Marko", "Matija"]
arr_rev = []

for a in arr:
    arr_rev.append(a[::-1])

print(arr)
print(arr_rev)


# Start with the previous example.
# For each name in original list print also its index, 
# and the item at that index in reversed name list.

arr = ["Ivanka", "Marko", "Matija", "Petar", "Ivo"]
arr_rev = []

for a in arr:
    arr_rev.append(a[::-1])

list_len = len(arr) # 4

print("Len", list_len)

for idx in range(list_len):
    print(idx, arr[idx], arr_rev[idx])

# Write a program in which you fill the list with 100 random numbers between 1 and 1000. 
# Print how many even elements are there in a list.
# Then remove all the odd elements and count again how many elements are there in a list.
'''
import random

random_numbers = [random.randint(1, 1000) for _ in range(100)]

counter = 0
for i in range(len(random_numbers)):
    if random_numbers[i] % 2 == 0:
        counter += 1
print(f'Number of even elements: {counter}')

new_numbers = []
for i in range(len(random_numbers)):
    if random_numbers[i] % 2 == 0:
        new_numbers.append(random_numbers[i])


new_count = len(new_numbers)
print(f'Number of elements after removing odd elements: {new_count}')

### PITANJE: 
# nisam sigurna da je to bas ono sto si htio, ovdje ispada da su oba broja jesu even i ista su, 
# ovdje se prvi puta susrrecem s ovakvom fomulacijom random_numbers = [random.randint(1, 1000) for _ in range(100)], ako moze htjela bi da ju prokomentiramo



# Create an empty dictionary. Load the user's 5 domain tags and the country to which the domain belongs to the dictionary. 
# After entering, print the contents of the dictionary in the format of country - domain name.

dictionary = {}

dictionary['moj posao.com']='hrvatska'
dictionary ['moje delo.com']='slovenija'
dictionary ['metro.at']='ausrija'
dictionary ['calcedonia.it']='italia'
dictionary ['footlocker.de']='njemacka'
   
for domain, country in dictionary.items():
    print(f'{country} - {domain}')


## PITANJE 
#na liniji koda 71 zanima me odakle on vuce domenu jer ju nigdje nisam spomenula, zanima me odakle mu taj format isto tako zanima me odakle mu conutry kad ni toga nigdje nema



# Upgrade previous program (04-exercise), after input, allow the user to search endlessly by domain tag. 
# If the domain does not exist in the dictionary, inform the user about it.


while True:
    tag = input("Enter a domain (type 'q' to quit): ")
    if tag == 'q':
        break
    if tag in dictionary:
        print(f'{tag} belongs to {dictionary[tag]}')
    else:
        print(f'{tag} does not exist in the dictionary')



# Write a program that will for each letter of the alphabet store its ASCII code. Print the contents of the data structure.

###PITANJE 
# JA NEMAM POJMA STA SE ASCII, NASLA SAM PAR PRIMJERA NA NETU AL NE ZNAM DAL JE TO TO, ivi zadnje bi trebalo bit to al ne kuzim uopce sta radi sta, tipa sta radi ord i sta je tocno ascii

test_str = "abcdefghijklmnopqrstuvwxyz"
print(ascii(test_str))



alphabet = 'abcdefghijklmnopqrstuvwxyz'

ascii_codes = {}

for letter in alphabet:
  ascii_codes[letter] = ord(letter)

print(ascii_codes)