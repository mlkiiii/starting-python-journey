from random import randint
finalx=randint(100,999)
print("Welcome to Bagels, a deductive logic game.")
print("I am thinking of a three-digit number. Try to guess what it is.")
x=int(input("Enter your guess: "))
while x!=finalx:
    if x//100==finalx//100:
        print("fermi")
    if x%10==finalx%10:
        print("fermi")