n=input("Enter any password:")
dg=sm=up=sp=0
if(len(n)>7):
    for i in n:
        if(i.isupper()):
            up=up+1
        elif(i.islower()):
            sm=sm+1
        elif(i.isdigit()):
            dg=dg+1
        else:
            sp=sp+1
    if(up>0 and sm>0 and dg>0 and sp>0):
        print("GOOD PASSWORD")
    else:
        print("BAD PASSWORD")
else:
    print("BAD DUE TO LESS NUM OF CHARACTERS")
     
