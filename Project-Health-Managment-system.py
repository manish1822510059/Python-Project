#Health Management System
def getdate():
    import datetime
    return datetime.datetime.now()


 #now code start
import datetime
def gettime():
     return datetime.datetime.now()

def take(k):
    if (k==1):
        c=int(input("Enter 1 for Exercise 2 For Food"))
        if (c==1):
            value=input("Type here\n")
            with open("manish-ex.txt","a") as op:
                    op.write(str([str(gettime())])+": "+value+"\n")
            print("Successfully written : ")
        elif(c==2):
            value=input("Type here\n")
            with open("manish-food.txt","a") as op:
                    op.write(str([str(gettime())])+": "+value+"\n")
            print("Successfully written : ") 

    elif (k==2):
        c=int(input("Enter 1 for Exercise 2 For Food"))
        if (c==1):
            value=input("Type here\n")
            with open("harry-ex.txt","a") as op:
                    op.write(str([str(gettime())])+": "+value+"\n")
            print("Successfully written : ")
        elif(c==2):
            value=input("Type here\n")
            with open("harry-food.txt","a") as op:
                    op.write(str([str(gettime())])+": "+value+"\n")
            print("Successfully written : ") 
    elif(k==3):
        c=int(input("Enter 1 for Exercise 2 For Food"))
        if (c==1):
            value=input("Type here\n")
            with open("ankit-ex.txt","a") as op:
                    op.write(str([str(gettime())])+": "+value+"\n")
            print("Successfully written")
        elif(c==2):
            value=input("Type here\n")
            with open("ankit-food.txt","a") as op:
                    op.write(str([str(gettime())])+": "+value+"\n")
            print("Successfully written")
    else:
        print("plz enter valid input (1(manish),2(harry),3(ankit)") 
def retrive(k):
    if (k==1):
        c=int(input("Enter 1 for Exercise 2 For Food"))
        if (c==1):
            with open("manish-ex.txt") as op:
                for i in op:
                        print(i,end="")
        elif(c==2):
             with open("manish-food.txt") as op:
                 for i in op:
                        print(i,end="")
    elif(k==2):
        c=int(input("Enter 1 for Exercise 2 For Food"))
        if (c==1):
            with open("harry-ex.txt") as op:
                for i in op:
                        print(i,end="")
        elif(c==2):
             with open("harry-food.txt") as op:
                for i in op:
                        print(i,end="")

    elif(k==3):
        c=int(input("Enter 1 for Exercise 2 For Food"))
        if (c==1):
            with open("ankit-ex.txt") as op:
                for i in op:
                        print(i,end="")
        elif(c==2):
             with open("ankit-food.txt") as op:
                    for i in op:
                        print(i,end="")
                                      


    else:
        print("plz enter valid input (manish,harry,ankit)")
                
         
                       
                        
            
           





print("*******Health Management System*******")
a=int(input("Press 1 for log and  2 For retrive "))
if a==1:
   b=int(input("Press 1 for Manish 2 for Harry 3 for Ankit "))
   take(b)
else: 
    b=int(input("Press 1 for Manish 2 for Harry 3 for Ankit "))
    retrive(b)   
