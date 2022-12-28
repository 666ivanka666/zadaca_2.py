# Write a program that will accept numbers and just for odd ones print squared values. Allow the program to exit on `q`.

# Explanation:
#   * In an endless loop, keep entering values.
#   * If value is `q`, then quit the program.
#   * Else, try to convert it to number. If it's an odd number, print its squared value.


'''
while True:
  num = input("Enter a number or 'q' to quit: ")
  if num == 'q':
    break

  # pretvara str u int
  num = int(num)
  if num % 2 != 0:
    print(num ** 2)'''
   

# Write a program that draws a triangle like this:
# ```
#   *
#   * *
#   * * *
#   * * * *
#   * * * * *
#
# Need to use loops, and create program in order that user need to insert character, and with inserted character draw a triangle


character = input("Inserted character: ")

for i in range(0,8):
    for j in range(i+1):
        print(character, end="")
    print("\n")

#-----

char = input("Enter a character: ")
rows = 5
for i in range(rows):
  print(char * (i+1))