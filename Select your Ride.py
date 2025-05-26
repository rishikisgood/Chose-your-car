print("Select your ride:")
print("1. Bike")
print("2. Car")
Choice = int(input("Enter your choice: "))

if( Choice==1):
    print("What type of Bike?")
    print("1. Scooty \n")
    print("2. Scooter\n")
    choice2=int(input("Enter your choice 2: "))
    if choice2==1:
        print("You have selected Scotoy")
    else:
        print("You have selected Scooter")

elif(Choice==2):
    print("What type of Car?")
    print("1. Sedan")
    print("2. XUV")
    choice3=int(input("Enter your choice 3: "))
    if choice3==1:
        print("You have selected Sedan")
    else:
        print("You have selected XUV")
else:
    print("Wrong Choice")