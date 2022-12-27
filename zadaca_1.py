
 
# 1.Write a program that prints three words: "Hello", "World", "Python", each on its own line, separated by a blank line
# 1.Napišite program koji ispisuje tri riječi: "Zdravo", "Svijet", "Python", svaka na svojoj liniji, odvojena praznom linijom

# print("Zdravo\n")
# print("Svijet\n")
# print("Python\n")

# PITANJE:
# ZASTO NE RADI NA OVAJ NACIN, STO JE KRIVO?  print("Zdravo\n","Svijet\n","Python\n")


# 2.Store the value 52 in the variable named *number*. Print the variable on the screen.
# 2.Spremi vrijednost 52 u varijabli pod nazivom *broj*. Ispišite varijablu na zaslonu.

# number= int(input("store the value 52: "))
# print(type(number))


# #3. Write a program that stores the number 10 in one variable, the number 25 in another, and prints the sum, product, difference and quotient of these numbers. 
# #Napišite program koji pohranjuje broj 10 u jednu varijablu, broj 25 u drugoj i ispisuje zbroj, proizvod, razliku i kvocijent tih brojeva. 


# number_1=10
# number_2=25


# print(number_1, "+", number_2, "=", (number_1 + number_2))
# print(number_1, "-", number_2, "=", (number_1 - number_2))
# print(number_1, "*", number_2, "=", (number_1 * number_2))
# print(number_1, "/", number_2, "=", (number_1 / number_2))

# # Format the printout so that each printout is on its own line, and both the operands and the operator are printed. 
# # Oblikujte ispis tako da je svaki ispis u svom retku, a ispisuju se i operandi i operator. 

# # For example, for the product it is necessary to print: "10 * 25 = 250".
# # Na primjer, za proizvod je potrebno ispisati: "10 * 25 = 250

# number_1= int(input("first number: "))
# print(type(number_1))
# number_2= int(input("second number: "))
# print(type(number_2))


# print(number_1, "+", number_2, "=", (number_1 + number_2))
# print(number_1, "-", number_2, "=", (number_1 - number_2))
# print(number_1, "*", number_2, "=", (number_1 * number_2))
# print(number_1, "/", number_2, "=", (number_1 / number_2))


# # Questions:
# # What is string concatenation, and what ways we can do that (provide example for each ways based on task above)? Feel free to google that
# #Pitanja:
# # Što je ulančavanje nizova i na koje načine to možemo učiniti (pružiti primjer za svaki način na temelju gornjeg zadatka)? Slobodno guglajte to

# #ODGOVOR
# #- spajanje varijabli na razne nacine 
# number_1=10
# number_2=25

# number_3=number_1 + number_2
# print(number_3)
# #---

# print(number_1 + number_2)
# #---
# print(number_1,"",number_2)
# #---
# print('%s %s' % (number_1, number_2))
# #---
# print('{} {}'. format (number_1,number_2))
# #---
# f"{number_1} {number_2}"

# print("".join([str(number_1), str(number_2)]))

#--- PITANJE, ZASTO OVO NE RADI print("".join([number_1, number_2]))


#4. Write a program that loads the length of the sides of a rectangle and prints its area and perimeter.
#4. Napišite program koji učitava duljinu stranica pravokutnika i ispisuje njegovo područje i perimetar

# l = float(input('Enter the length: ')) 
# w = float(input('Enter the width: '))
 
# print(f'The rectangle’s area is {round(l * w, 3)}.') 

# l = float(input("Enter the Length of the Rectangle : ")) 
# b = float(input("Enter the Breadth of the Rectangle : ")) 
 
# area = l*b 
 
# print(f"Area of Rectangle : {area} sq. units") 

#5. Read a character from the user and draw something like this using that character (assuming that user entered *x*):
#
#|   x     |
#|  xxx    |
#| xxxxx   |
##5. Pročitajte znak od korisnika i nacrtajte nešto slično pomoću tog znaka (pod pretpostavkom da je korisnik unio *x*):
#
#|   x |
#|  xxx |
#| xxxxx |
#
char = input("Unesite znak: ")
print(f"\t  {char}  \t|")
print(f"\t {char * 3}  \t|")
print(f"\t{char*5} \t|")

# POSALJI NA MAIL i NA GITHUB

a = 10
b = 12
c = 13

# not(true i true) = false
# not(false i true) = true
# not(true i false) = true
# not(false i false) = true

# true or true = true
# true or false = true
# false or true = true
# false or false = false

# if a != b or b != c or a != c:
#     print("10")
# elif 10 != 10:
#     print("10 != 10")
# elif 10 != 10:
#     print("10 != 10")
# elif 10 != 10:
#     print("10 != 10")
# elif 10 != 10:
#     print("10 != 10")
# else:
#     print("Else")

if a != b:
    print("DEMO")

if b != c:
    print("DEMO")

if a != c:
    print("DEMO")


############################

if a != b:
    print("DEMO")
elif b != c:
    print("DEMO")
elif a != c:
    print("DEMO")
