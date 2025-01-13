



def prime_factors(n):
    factors=[]

    while(n%2==0):
        factors.append(2)
        n//=2

    for i in range(3, n+1, 2):
        while(n%i==0):
            factors.append(i)
            n//=i
    return factors


num=int(input("Enter the number : "))

if(num>1):
    result=prime_factors(num)
    print(result)
else:
    print("Enter a number greater then 1 ")
