n= int(input("Enter the number: "))
result = []
a = 1

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def sum_dig(num):
    return sum(int(i) for i in str(num))

def tot_dig(num):
    return len(str(num))

while len(result) != n:
    if is_prime(a):
        s = sum_dig(a)
        t = tot_dig(a)
        if is_prime(s) and is_prime(t):
            result.append(a)
    a += 1

print(result)
