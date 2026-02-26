from random import*
print("Welcome to the Birthday Paradox!")
print("This program simulates the birthday paradox.")
months=["","Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sept","Oct","Nov","Dec"]
days_in_month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
def bday(months,days_in_month):
    month = randint(1, 12)
    day = randint(1, days_in_month[month])
    ret=months[month]+" "+str(day)
    return ret
def num_people():
    n=int(input("Enter the number of people in the group: "))
    while n<2 or n>100:
        print("Please enter a valid number of people (at least 2 and at most 100).")
        n=int(input("Enter the number of people in the group: "))
    return n
def birthdays(n):
    bdays=[]
    for i in range(n):
        bdays.append(bday(months,days_in_month))
    return bdays
def has_duplicates(bdays):
    seen = set()
    for b in bdays:
        if b in seen:
            return bdays.index(b)
        seen.add(b)
    return False
def main1():
    n=num_people()
    bdays=birthdays(n)
    for n in range(0,n):
        print(bdays[n]+","+" ")
    if has_duplicates(bdays)!=False:
        print("in these, multiple people have a birthday on the same day "+str(has_duplicates(bdays)+1))
        print("Generating"+n+"random birthdays"+"1000 times...")
    else:
        print("in these, no one has a birthday on the same day")
        print("Generating"+n+"random birthdays"+"1000 times...")
def main2():
    z=input("press enter to run 1000 simulations...")
    n=num_people()
    count=0
    for i in range(1000):
        bdays=birthdays(n)
        if has_duplicates(bdays)!=False:
            count+=1
        print(str(i)+" simulations run...")
    print("Out of 1000 simulations, "+str(count)+" had at least one shared birthday.")
    print("That means that in a group of "+str(n)+" people, there is a "+str(count/10)+"% chance that two people share a birthday.")