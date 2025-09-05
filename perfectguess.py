import random as ran

def guessno():
    return int(input("Enter your guess from 1 to 10 :"))

def perfectguess(a):
    guess=ran.randint(1,100)
    count=1
    while(a!=guess):
        count+=1
        # if(count>10):
        #     break
        if(a>guess):
            print("guess lower")
            a=guessno()
        else:
            print("guess higher")
            a=guessno()
    else:
        print("total guesses:",count)

no=guessno()
perfectguess(no)

