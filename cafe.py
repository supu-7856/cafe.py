# deifne the menu in restarurant
menu= {
    'piza':50,
    'pasta':70,
    'Burger':90,
    'salad':30,
    'coffee':120,



}
#print(menu)
print("Welcome to Tosali")
print("piza:Rs50\n pasta:Rs70\n Burger:Rs90\n salad:Rs30\n coffee:Rs120")

order_total=0
# 50+40=90


item_1=input("Enter the name of item you want to order = ")

if item_1 in menu:
    order_total += menu[item_1]
    print(f"your item{item_1} has been order")
else:
    print(f"Order item {item_1} is not avaiable yet!")

Another_order = input("Do you want to add another item?(Yes/No)")
if Another_order == "Yes":
    item_2 = input("please enter the second item = ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"item{item_2}has been orderd")
    else:
        print(f"order item{item_2} is not avaiable ! please chose another")
# no 3 item
Another_order_2 = input("Do you want to add another item?(Yes/No)")
if Another_order_2== "Yes":
    item_3 = input("please enter the Third item = ")
    if item_3 in menu:
        order_total += menu[item_3]
        print(f"item{item_3}has been orderd")
    else:
        print(f"order item{item_3} is not avaiable ! please chose another")
# no 4 item
Another_order_3 = input("Do you want to add another item?(Yes/No)")
if Another_order_3== "Yes":
    item_4 = input("please enter the 4th item = ")
    if item_4 in menu:
        order_total += menu[item_4]
        print(f"item{item_4}has been orderd")
    else:
        print(f"order item{item_4} is not avaiable ! please chose another")

print(f"the total amount of item to pay is {order_total} ")