from random import randint
finalx=randint(100,999)
print("Welcome to Bagels, a deductive logic game.")
print("I am thinking of a three-digit number. Try to guess what it is.")
x=int(input("Enter your guess: "))
f=0
while x!=finalx:
    if x//100==finalx//100:
        print("fermi")
        f=f+1
    if x%10==finalx%10:
        print("fermi")
        f=f+1
    if  (str(x)[1])==(str(finalx)[1]):
        print("fermi")
        f=f+1
    if x//100== int(str(finalx)[1]) or x//100==finalx%10:
        print("pico")
        f=f+1
    if x%10==finalx//100 or x%10==int(str(finalx)[1]):
        print("pico")
        f=f+1
    if str(x)[1]==finalx//100 or int(str(x)[1])==finalx%10:
        print("pico")
        f=f+1
    if f==0:
        print("bagels")
    f=0
    x=int(input("Enter your guess: "))
print("Congratulations! You guessed the number!")