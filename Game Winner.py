import time,random
name1=input("enter the name of player1")
name2=input("enter the name of palyer2")
print("computer has fixed 5 number of integer in its mind")
print("you both have three turns each to guess it")
print("Ready for the game??")
nums=[]
while(len(nums)!=5):
    a=random.randint(1,10)
    while(a in nums):
        a=random.randint(1,10)
    nums.append(a)
player1=[]
player2=[]
s1=0
s2=0
for i in range(3):
    print("hai {} guess ur choice no {}".format(name1,i+1))
    x=int(input())
    while x in player1 or x in player2:
        print("already chosen , so guess some other number")
        x=int(input())
    player1.append(x)
    if x in nums:
        print("-->CORRECT")
        s1=s1+1
    else:
        print("-->WRONG")
        
    print("hai {} guess ur choice no {}".format(name2,i+1))
    x=int(input())
    while x in player1 or x in player2:
        print("already chosen , so guess some other number")
        x=int(input())
    player2.append(x)
    if x in nums:
        print("-->CORRECT")
        s2=s2+1
    else:
        print("-->WRONG")
        
print("lets have summary")
print("Comp has chosen {}".format(nums))
print("{} has chosen{}".format(name1,player1))
print("His Score is {}",format(s1))
print("{} has chosen{}".format(name2,player2))
print("His Score is {}",format(s2))
if(s1>s2):
    print("{} is Winner".format(name1))
elif(s2>s1):
    print("{} is Winner".format(name2))
else:
    print("Draw")
