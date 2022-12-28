'''# Write a program that prints the numbers from 1 to 5 using a while loop. 
# Each number in a separate line

counter = 1

while counter <= 5:
    print(counter)
    counter += 1

# Write a program that prints the numbers from 1 to 5 using a while loop
# So that it prints the numbers one after another, delimited with space. 
# Example: 1 2 3 4 5

counter = 1

while counter <= 5:
    print(counter, end=" ")
    counter += 1

# Write a program that inputs a string that will be output in capital case (capitalized string).
# Program should run in an infinite loop.
# Specifically, if letter `q` is entered, program should exit

while True:
    word = input("Unesi rijec (q - za izlaz): ")
    if word == 'q':
        break
    else:
        print(word.capitalize())

# Write a program that asks for two numbers.
# If first number is smaller than the second one, increase it in loop until it get equal as the second one.
# If second number is smaller than the first one, increase it in loop until it get equal as the first one.
# At the end, write the values.

# BONUS
# Change the last example so that it outputs all the even numbers between the given two numbers.


number_1 = int(input("Prvi broj: "))
number_2 = int(input("Drugi broj: "))

while number_1 < number_2:
    if number_1 % 2 == 0:
        print("Number 1: ", number_1)

    number_1 += 1

# while number_1 > number_2:
#     print("Number 2: ", number_2)
#     number_2 += 1
'''

## ZA NAPRAVITI

# Write a program that prints numbers from 1 to 10 
# separated by *tabs* using a for loop.
'''
counter = 1

while counter <= 5:
    print(counter, '\t')
    counter += 1

# Write a program that prints all odd numbers between 
# 10 and 30 separated by tabs using a for loop.

for i in range(11, 30, 2):
  print(i, end='')

#---------


list1 = list(range(10,31))

for num in list1:

    if num % 2 != 0:
       print(num, end=' ')'''
       

# Write a program that manages a counter in an infinite loop.
# Counter starts from 0.
# Prompt for command should be `cmd>`

# Support these commands:
#   * `inc`: increase counter by 1
#   * `dec`: decrease counter by 1
#   * `rst`: resets counter to 0
#   * `quit`: ends the program
#   * if any unknown command is entered, ignore it

#   After any command except `quit` and unknown, output `ok` and the current counter value.

# Note: for last two points (`quit` and unknown) use `break` and `continue`



counter = 0

while True:
 
  cmd = input("cmd> ")

  if cmd == "inc":
    # Increase counter by 1
    counter += 1
  elif cmd == "dec":
    # Decrease counter by 1
    counter -= 1
  elif cmd == "rst":
    # Reset counter to 0
    counter = 0
  elif cmd == "quit":
    # End the program
    break
  else:
    # Ignore unknown command
    continue

  # Output 'ok' and the current counter value
  print("ok", counter)