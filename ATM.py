print('welcome user')
print('credit=1','debit=2','Mini_statement=3')
n=int(input('Enter your choice'))
def credit():
    print('credit amount')
def debit():
    print('debit amount')
def Mini_statement():
    print('Mini_statement')
if n==1:
    credit()
elif n==2:
    debit()
elif n==3:
    Mini_statement()
else:
    print('Your Enter The Wrong Number')


output:
welcome user
credit=1 debit=2 Mini_statement=3
Enter your choice1
credit amount
