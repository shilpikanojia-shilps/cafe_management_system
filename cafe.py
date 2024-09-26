# menu of restaurant

menu = {
    'Pizza': 100,
    'Pasta': 80,
    'Burger': 60,
    'Coffee': 70,
    'Coldrink': 40,
}

print("Welcome to the Python restaurant")
print('Pizza: 100, \nPasta: 80, \nBurger: 60, \nCoffee: 70, \nColdrink:40 ')

order_total = 0

item_1 = input("enter the name of the item you want to order: ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"your item {item_1} has been added to the cart.")
else:
    print(f"Orderd item_1 {item_1} is not available yet")
    
another_order = input("Do you want to order something else?(Yes/NO)")
if another_order == 'Yes':
    item_2 = input("enter the name of second item: ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item_2 {item_2} has been added to the cart") 
    else:
        print(f"Orderd item {item_2} is not available yet.")
        
        
print(f"The total amount of items to pay is {order_total} ")

    
    
