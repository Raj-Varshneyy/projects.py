import random

attempt= int(input("enter the number of attempt  :"))

a=random.randint(1,100)

while attempt>0:
     
     
    n=int(input("enter the number :"))
    if n<a:
        c=a-n
        print("your guessed number is :",n)
        print(" you are failed")
        

    elif n>a:
        c=n-a
        print("your guessed number is :",n)
        print(" you are failed")

    elif n==a:
          print("you are passed")
          print("your guessed number is correct: ", n)
    else :

        print("not acceptable")
    attempt-=1
    
print("correct no. is",a)