print("=" * 20)
customerNames = ['Supriya', 'Sai', 'Krishna', "Radha", 'Priya']
customerPins = ['0123', '12575', '71275', '23112', '50491']
customerBalances = [10000, 30000, 20000, 50000, 100000]
deposition = 0
withdrawal = 0
balance = 0
counter1 = 1
counter2 = 5
i = 0
while True:
    print("=====================================")
    print(" ----Welcome to Sai Bank----       ")
    print("*************************************")
    print("1. Open a new account        ")
    print("2. Withdraw Money            ")
    print("3. Deposit Money             ")
    print("4. Check Customers & Balance ")
    print("5. Exit/Quit                 ")
    print("*************************************")
    choiceNumber = input("Select your choice number from the above menu : ")
    if choiceNumber == "1":
        print("Choice number 1 is selected by the customer")
        NOC = eval(input("Number of Customers : "))
        i = i + NOC
        if i > 5:
            print("\n")
            print("Customer registration exceed reached or Customer registration too low")
            i = i - NOC
        else:
            while counter1 <= i:
                name = input("Input Fullname : ")
                customerNames.append(name)
                pin = str(input("Please input a pin of your choice : "))
                customerPins.append(pin)
                balance = 0
                deposition = eval(input("Please input a value to deposit to start an account : "))
                balance = balance + deposition
                customerBalances.append(balance)
                print("\nName=", end=" ")
                print(customerNames[counter2])
                print("Pin=", end=" ")
                print(customerPins[counter2])
                print("Balance=", end=" ")
                print(customerBalances[counter2], end=" ")
                print("-/Rs")
                counter_1 = counter1 + 1
                counter_2 = counter2 + 1
                print("\nYour name is added to customers system")
                print("Your pin is added to customer system")
                print("Your balance is added to customer system")
                print("----New account created successfully !----")
                print("\n")
                print("Your name is avalilable on the customers list now : ")
                print(customerNames)
                print("\n")
                print("Note! Please remember the Name and Pin")
                print("========================================")
        mainMenu = input("Please press enter key to go back to main menu to perform another function or exit ...")
    elif choiceNumber == "2":
        j = 0
        print("Choice number 2 is selected by the customer")
        while j < 1:
            k = -1
            name = input("Please input name : ")
            pin = input("Please input pin : ")
            while k < len(customerNames) - 1:
                k = k + 1
                if name == customerNames[k]:
                    if pin == customerPins[k]:
                        j = j + 1
                        print("Your Current Balance:", end=" ")
                        print(customerBalances[k], end=" ")
                        print("-/Rs\n")
                        balance = (customerBalances[k])
                        withdrawal = eval(input("Input value to Withdraw : "))
                        if withdrawal > balance:
                            deposition = eval(input(
                                "Please Deposit a higher Value because your Balance mentioned above is not enough : "))
                            balance = balance + deposition
                            print("Your Current Balance:", end=" ")
                            print(balance, end=" ")
                            print("-/Rs\n")
                            balance = balance - withdrawal
                            print("-\n")
                            print("----Withdraw Successfull!----")
                            customerBalances[k] = balance
                            print("Your New Balance: ", balance, end=" ")
                            print("-/Rs\n\n")
                        else:
                            balance = balance - withdrawal
                            print("\n")
                            print("----Withdraw Successfull!----")
                            customerBalances[k] = balance
                            print("Your New Balance: ", balance, end=" ")
                            print("-/Rs\n\n")
            if j < 1:
                print("Your name and pin does not match!\n")
                break
        mainMenu = input("Please press enter key to go back to main menu to perform another function or exit ...")
    elif choiceNumber == "3":
        print("Choice number 3 is selected by the customer")
        n = 0
        while n < 1:
            k = -1
            name = input("Please input name : ")
            pin = input("Please input pin : ")
            while k < len(customerNames) - 1:
                k = k + 1
                if name == customerNames[k]:
                    if pin == customerPins[k]:
                        n = n + 1
                        print(customerBalances[k], end=" ")
                        print("-/Rs")
                        balance = (customerBalances[k])
                        deposition = eval(input("Enter the value you want to deposit : "))
                        balance = balance + deposition  # 1000+500=1500
                        customerBalances[k] = balance
                        print("\n")
                        print("----Deposition successful!----")
                        print("Your New Balance: ", balance, end=" ")
                        print("-/Rs\n\n")
            if n < 1:
                print("Your name and pin does not match!\n")
                break
        mainMenu = input("Please press enter key to go back to main menu to perform another function or exit ...")
    elif choiceNumber == "4":
        print("Choice number 4 is selected by the customer")
        k = 0
        print("Customer name list and balances mentioned below : ")
        print("\n")
        while k <= len(customerNames) - 1:
            print("->.Customer =", customerNames[k])
            print("->.Balance =", customerBalances[k], end=" ")
            print("-/Rs")
            print("\n")
            k = k + 1
        mainMenu = input("Please press enter key to go back to main menu to perform another fuction or exit ...")
    elif choiceNumber == "5":
        print("Choice number 5 is selected by the customer")
        print("Thank you!")
        print("Come Again")
        print("Bye")
        break
    else:
        print("Invalid option selected by the customer")
        print("Please Try again!")
        mainMenu = input("Please press enter key to go back to main menu to perform another function or exit ...")