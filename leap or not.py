# code:


def check_year(year):
    return(((year%4==0)and(year%100!=0))or(year%400==0))
year=int(input('check which year you want to know '))
if (check_year(year)):
    print('Leap Year')
else:
    print('Not a leap year')


# Explanation
#2004%4==0 ---------------- TRUE
# 2004%100!=0--------------TRUE
# IT GIVES TRUE
# 2004%400==0-------------FALSE
# it gives FALSE
# TRUE   FALSE ==== TRUE
# 1    0 ===== 1



# output:
# check which year you want to know 2004
# Leap Year