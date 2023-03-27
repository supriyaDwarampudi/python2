from datetime import datetime
name = input("Enter the customer name:")
# List of items in the market
list = '''
rice        Rs 50/kg
salt        Rs 20/kg
oil         Rs 80/liter
wheat       Rs 55/kg
horlicks    Rs 150/each
'''
# Decleration
p = 0
price_list = []
total_price = 0
final_price = 0
item_list = []
quantity_list = []
plist = []
# Rates for items
items = {'rice': 50,  'salt':20, 'oil': 80, 'wheat':55,'horlicks':150}
option = int(input("For list of the items press 1:"))
if option == 1:
    print(list)
for i in range(len(items)):
    inp1 = int(input("Press 1 to buy, Press 2 to Exit:"))
    if inp1 == 2:
        break
    if inp1 == 1:
        item = input("Enter your item:")
        quantity = int(input("Enter your Quantity:"))
        if item in items.keys():
            price = quantity*(items[item])
            price_list.append((item,quantity,items,price))
            total_price+=price
            item_list.append(item)
            quantity_list.append(quantity)
            plist.append(price)
            GST = (total_price*5)/100
            final_price = total_price+GST
        else:
            print("Enter item is not available")
    else:
        print("You entered a wrong item")
# Generating the Bill or Bring the bill
    inp = input("Do you need print copy Yes or No:")
    if inp == "yes":
        pass
    if final_price !=0:
        print(25*"=", "Supriya Super Market",25*"=")
        print(28*" ", "West Godavari")
        print("Name:", name,30*" ", "Date:", datetime.now())
        print(75*" ")
        print("SNo", 8*" ",'items',8*" ", 'Quantity', 3*" ", 'price', )
        for i in range(len(price_list)):
            print(i, 8*' ',3*' ',item_list[i],8*' ',quantity_list[i],9*" ",plist[i])
        print(75*"-")
        print(50*" ", 'TotalAmount:', 'Rs', total_price)
        print("gst amount", 50*" ", 'Rs', GST)
        print(75*"-")
        print(50*" ", 'finalAmount:', 'Rs', final_price)
        print(75*"-")
        print(20*" ","Thanks for Visiting")
        print(75*"-")
