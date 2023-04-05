a=float(input('ENTER A VALUE'))
b=float(input('ENTER B VALUE'))
c=float(input('ENTER C VALUE'))
if ((a>b) and (a>c)):
    print(a,'is a greater number')
elif ((b>a) and (b>c)):
    print(b,'is a greater number')
elif ((c>a) and (c>b)):
    print(c,'is a greater number')
else:
    print('All The Three Values Are Equal')


# OUTPUT:
# ENTER A VALUE12
# ENTER B VALUE14
# ENTER C VALUE16
# 16.0 is a greater number
