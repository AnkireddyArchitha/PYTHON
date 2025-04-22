def isround(n):
    res=[]
    while(n!=1):
        if (n in res):
            return False
        res.append(n)
        n=sum(int(i)*int(i) for i in str(n))
    return True
print(isround(19))
print(isround(10))
print(isround(34))
