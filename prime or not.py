# A number which is divisible by itself and 1
# CODE:

# count=0
# n=int(input('Enter a number:'))
# for i in range(1,n+1):
#     if n%i==0:
#         count+=1
# if count==2:
#     print('Given number is prime number')
# else:
#     print('Given number is not a prime number')

# output:
# Enter a number:24
# Given number is not a prime number

#       OR
def is_prime(number):
    if number>1:
        for i in range(2,number):
            if number%i==0:
                return "not a prime"
        return "prime"
    return "not a prime"
print(is_prime(24))

 # output:
# not a prime