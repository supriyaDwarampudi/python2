#finding compound interest
P=int(input('Enter principle value'))
R=int(input('Enter rate value'))
N=int(input('Enter n value'))
T=int(input('Enter time value'))
CI=P*(1+(R/N))**(N*T)
print(CI)


output:

Enter principle value12
Enter rate value32
Enter n value5
Enter time value4
2.90948177199035e+18
