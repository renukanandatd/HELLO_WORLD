def factorial(n):
    if (n==0)|(n==1):
        return 1
    else:
        return n*factorial(n-1)


for i in range(0,36):
    print(i,factorial(i))


def sum_numbers(*n):
    sum=0
    for i in n:
        sum+=i
    return sum


x=sum_numbers(1,2,3.1)
print(x)