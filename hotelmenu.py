menu = {
    'Pizza': 199,
    'Pasta': 120,
    'Burger': 150,
    'Salad': 70,
    'Coffee': 120,
}

print("Welcome to CafeName")
print("Pizza = Rs199\nPasta = Rs120\nBurger = Rs150\nSalad = Rs70\nCoffee = Rs120")

order_total = 0

item_1 = input("Enter the item you want to order: ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your cart")
else:
    print(f"Sorry! {item_1} is not available")

another_order = input("Do you want to add another item? (Yes/No): ")
if another_order.lower() == "yes":
    item_2 = input("Enter the name of the item: ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item {item_2} has been added to your cart")
    else:
        print(f"Ordered item {item_2} is not available")

print(f"The total amount of items to pay is Rs{order_total}")
