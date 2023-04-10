n=int(input("Enter a number: "))
temp=n
b=len(str(n))
sum=0
while n!=0:
    r=n%10
    sum=sum+(r**b)
    n=n//10
if temp==sum:
    print('Armstrong number')
else:
    print('Not a Armstrong number')


# output:
# Enter a number: 371
# Armstrong number

# 3^3+7^7+1^1=371