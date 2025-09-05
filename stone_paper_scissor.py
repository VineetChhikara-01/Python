import random as rd
'''
1=scissor
0=paper
-1=stone
'''
auto=rd.choice((-1,0,1))
you=input("Enter your choice:")
dict={"scissor":1,"stone":-1,"paper":0,"s":1,"p":0,"st":-1,1:1,0:0,-1:-1}
reverse={1:"scissor",0:"paper",-1:"stone"}

yourresult=dict[you]

if(yourresult==auto):
    print(f"Match draw!!\ncomputer choose {reverse[auto]} and you choose {reverse[yourresult]}")
else:
    if(auto-yourresult==-1 or auto-yourresult==2):
        print(f"You win!!\ncomputer choose {reverse[auto]} and you choose {reverse[yourresult]}")
    else:
        print(f"You lose!!\ncomputer choose {reverse[auto]} and you choose {reverse[yourresult]}")
'''
1-0=1
1--1=2
0-1=-1
0--1=1
-1-1=-2
-1-0=-1
'''