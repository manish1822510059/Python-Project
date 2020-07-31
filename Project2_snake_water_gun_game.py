import random
list1=["snake","water","gun"]

value=random.choice(list1)
print("******Snake Water Gun Game******")
name=input("Please Enter your name: ".upper())
cu=0
cp=0
c=5
while c>0:
    a = input("You Choice 1. for Snake 2. for Water 3.for Gun\n") 
    if  a == "snake":
        
        if a == value:
            print(f"Match is draw::{a} vs {value} ")
            c=c-1
            print("Chance left",c)
        elif value == "water":
            print(f"You won ::{a} vs {value}")
            cu+=1
            c=c-1
            print("Chance left",c)
        elif value == "gun":
            print(f"You Lost ::{a} vs {value}")
            cp+=1
            c=c-1
            print("Chance left",c) 
    elif a=="water":
        if a == value:
            print(f"Match is draw::{a} vs {value} ")
            c=c-1
            print("Chance left",c)
        elif value == "gun":
            print(f"You won ::{a} vs {value}")
            cu+=1
            c=c-1
            print("Chance left",c)
        elif value == "water":
            print(f"You Lost ::{a} vs {value}")
            cp+=1
            c=c-1
            print("Chance left",c)
     
    elif a=="gun":
        if a == value:
            print(f"Match is draw::{a} vs {value} ")
            c=c-1
            print("Chance left",c)
        elif value == "water":
            print(f"You won ::{a} vs {value}")
            cu+=1
            c=c-1
            print("Chance left",c)
        elif value == "snake":
            print(f"You Lost ::{a} vs {value}")
            cp+=1
            c=c-1
            print("Chance left",c)
        
if(cu>cp):
    print(f"\c{name} is the Winner Your score:\t".upper(),cu)
else:
    print("\nSorry Computer is a winner Computer score:\t".upper(),cp)

         
         

