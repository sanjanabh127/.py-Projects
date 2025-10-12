#Define the menu of the resturent 
menu={
    'Pizza':120,
    'Burger':100,
    'Salad':70,
    'Pasta':80,
    'Coffee':50,
}
#greet
print("Welcome to PYTHON cafe")
print("Pizza : Rs120\nBurger : Rs100\nSalad : Rs70\nPasta : Rs80\nCoffee : Rs50")
order_total=0
item1=input("Enter the name of the item u want to order : ")
if item1 in menu:
    order_total+=menu[item1]
    print(f"Your {item1} is added to your order")
else:
    print("Order is not present in the menu")

another_order=input("Do you want to order something more ? (yes/no) :")
if another_order=="yes":
    item2=input("Enter the name of the item you want to order : ")
    if item2 in menu:
        order_total+=menu[item2]
        print(f"{item2} is added in the order")

    else:
        print(f"{item2} ordered item is unavailable yet!")
print(f"The total Bill sums upto : {order_total} ")        


