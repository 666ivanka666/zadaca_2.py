# Write a program that loads two integers and an operation from the user. Valid operations are +, -, * and /. 
# Print the result of the operation nicely formatted, with conditions:
# If the operation is not correct, print an error.
# If the second number is 0 and the operation is division, print an error.
'''
number_1 = int(input("Unesi 1 broj: "))
number_2 = int(input("Unesi 2 broj: "))
number_3=number_1*number_2

if number_3 == 0:
    print('first rule: sum is:', number_3, 'the operation is not correct, error')
elif number_1 == 0 or  number_2 == 0:
    print('second rule: sum is:', number_3, "one of the numbers is 0,  error.")
else:
    print('third rule: sum is:', number_3)
'''
#PITANJE: nisam shvatila dobro dali sam ovo postavila, cini mi se kao da mi stalno javlja odgovor sa prvog ifa i ne zavrti na elif, zavrti mi rule 1 i rule 3, 
#namjerno sam ih tako nazvala da vidim koji mi ne radi. ako stavim float javlja gresku pa sad ne znam razliku izmedju if i elif

##UPDATE
number_1 = int(input("Enter the first number: "))
number_2 = int(input("Enter the second number: "))

operation = input("Enter an operation (+, -, *, /): ")

if operation == "+":
    result = number_1 + number_2
elif operation == "-":
    result = number_1 - number_2
elif operation == "*":
    result = number_1 * number_2
elif operation == "/":
    if number_2 == 0:
        print("Error: Cannot divide by 0")
    else:
        result = number_1 / number_2
else:
    print("Error: Invalid operation")

if "result" in locals():
    print(f"Result: {result}")

# Write a program that loads a sentence.
# If there is a word "red" in the sentence then check if the last word in the sentence is "pill", and output "Accept life-changing facts". 
# If there is a word "blue" in the sentence then check if the last word in the sentence is "pill", and output "Remain ignorant".
# In "red" and "blue" case, if the second word is not "pill", then output "Red and blue are colors".

'''sentence_1 = input("Unesi rečenicu: ")

prvi_uvijet = 'crvena'
drugi_uvijet ='plava'
treci_uvijet ='pilula'



if sentence_1 == prvi_uvijet:
    print('Accept life-changing facts')
elif sentence_1 == drugi_uvijet:
    print('Remain ignorant')
else:
    print('Red and blue are colors')

'''
#ovo radi samo s jednom rijeci--------------------------------------

'''if sentence_1 == 'crvena pilula':
    print('Accept life-changing facts')
elif sentence_1 == 'plava pilula':
    print('Remain ignorant')
else:
    print('Red and blue are colors')

'''
#ovo radi ali mislim da nije dovoljno dobro jer ne daje mogucnost napisati npr crveno zuta pilula------------------------

'''crvena=True
plava=True
pilula=True

if crvena and pilula:
    print('Accept life-changing facts')
elif plava== True and pilula== True:
    print('Remain ignorant')
else:
    print('Red and blue are colors')'''


#-------------- ne valja

'''sentence_1 = input("Unesi rečenicu: ")

crvena=True
plava=True
pilula=True


if crvena and pilula:
    print('Accept life-changing facts')
elif plava and pilula:
    print('Remain ignorant')
else:
    print('Red and blue are color')
'''
#-------------- ne valja

'''
sentence_1 = input("Unesi rečenicu: ")
test_words = ['crvena', 'plava', 'pilula']
contains_1 = [0,1] 
contains_2 = [0,2]

for string in sentence_1:
    for test_word in test_words:
        if test_word not in string.split():
            contains_1 = False
            break           
    if not contains_1 :
        break

for string in sentence_1:
    for test_word in test_words:
        if test_word not in string.split():
            contains_2 = False
            break           
    if not contains_2 :
        break

if contains_1  :
    print("Accept life-changing facts")
if contains_2  :
    print("Remain ignorant")
else:
    print("Red and blue are color")'''

###--------- ne valja
'''
sentence_1 = input("Unesi rečenicu: ")
crvena=False
plava=False
pilula=False
for elem in sentence_1:

    if "crvena"  and 'pilula' in sentence_1:
        #crvena and pilula=True
        print('Accept life-changing facts')
        
    elif "plava" and 'pilula'in sentence_1:
        #motorbike=True
        print("Remain ignorant")
        
   
    else: 
        print("Red and blue are color")
        break'''

#--------- tu radi if i else, elif ne radi
'''
str =input("Unesi rečenicu: ")
myList_1 = ['crvena', 'pilula']
myList_2 = ['plava', 'pilula']

isMatch_1 = [True for x in myList_1 if x in str]
isMatch_2 = [True for x in myList_2 if x in str]
if True in isMatch_1:
  print("Accept life-changing facts")
elif True in isMatch_2:
   print("Remain ignorant")
else:
  print("remain ignorant")

###-----------opet ne radi elIF'''

## UPDATE
'''
sentence = input("Enter a sentence: ")

words = sentence.split()

if "crvena" in words:
    if words[-1] == "pilula":
        print("Accept life-changing facts")
    else:
        print("Red and blue are colors")
elif "plava" in words:
    if words[-1] == "pilula":
        print("Remain ignorant")
    else:
        print("Red and blue are colors")
else:
    print("Red and blue are colors")'''
#-----------
sentence = input("Enter a sentence: ")

words = sentence.split()

if "crvena" in words and words[-1] == "pilula":
    print("Accept life-changing facts")
elif "plava" in words and words[-1] == "pilula":
    print("Remain ignorant")
else:
    print("Red and blue are colors")