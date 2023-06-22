a=[1,2,3]
c=0
print("Welcome to game")
print("You have 3 choices")
for i in range(3):
    b=int(input('Enter your choices:'))
    if b==a[0]:
        print(' Congrats! You Won the Game')
    elif b==a[1]:
        print('Congrats! You Won The Game')
    elif b==a[2]:
        print('Congrats! You Won The Game')
    else:
        print('You Lost the Chance')
        c+=1
if c==3:
    print('You lost the Game')


    output:-


Welcome to game
You have 3 choices
Enter your choices:2
Congrats! You Won The Game
Enter your choices:1
Congrats! You Won The Game
Enter your choices:3
Congrats! You Won The Game