# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

# Order list setup
order_list = []

def add_to_order(item_name, item_price, quantity):
    order_item = {
        'Item name': item_name,
        'Price': item_price,
        'Quantity': quantity
    }
    order_list.append(order_item)

print("Welcome to the variety food truck.")

place_order = True
while place_order:
    print("From which menu would you like to order? ")
    i = 1
    menu_items = {}
    for key in menu.keys():
        print(f"{i}: {key}")
        menu_items[i] = key
        i += 1

    menu_choice = input("Type menu number: ")

    if menu_choice.isdigit():
        menu_choice = int(menu_choice)
        if menu_choice in menu_items.keys():
            menu_category_name = menu_items[menu_choice]
            print(f"You selected {menu_category_name}")
            print(f"What {menu_category_name} item would you like to order?")
            
            i = 1
            menu_items = {}
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")
            for key, value in menu[menu_category_name].items():
                if isinstance(value, dict):
                    for sub_key, sub_value in value.items():
                        num_item_spaces = 24 - len(key + sub_key) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {key} - {sub_key}{item_spaces} | ${sub_value}")
                        menu_items[i] = {"Item name": key + " - " + sub_key, "Price": sub_value}
                        i += 1
                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value}")
                    menu_items[i] = {"Item name": key, "Price": value}
                    i += 1

            menu_item = input("Please choose the menu item number: ")

            if menu_item.isdigit():
                menu_item = int(menu_item)
                if menu_item in menu_items.keys():
                    item_name = menu_items[menu_item]["Item name"]
                    item_price = menu_items[menu_item]["Price"]
                    quantity_input = input(f"How many '{item_name}' would you like to order? ")

                    quantity = 1 if not quantity_input.isdigit() else int(quantity_input)
                    add_to_order(item_name, item_price, quantity)
                    print(f"Added {quantity} of {item_name} to your order.")
                else:
                    print("That is not a valid menu option.")
        else:
            print(f"{menu_choice} was not a menu option.")
    else:
        print("You didn't select a number.")

    while True:
        keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o: ")
        if keep_ordering == "Y":
            break
        elif keep_ordering == "N":
            place_order = False
            print("Thank you for your order!")
            break
        else:
            print("Invalid entry. Please answer with 'Y' or 'N'.")

print("This is what we are preparing for you:\n")
print("Item name                 | Price  | Quantity")
print("--------------------------|--------|----------")

for item in order_list:
    item_name = item['Item name']
    price = item['Price']
    quantity = item['Quantity']
    name_spaces = " " * (25 - len(item_name))
    price_spaces = " " * (7 - len(str(price)))
    print(f"{item_name}{name_spaces}| ${price}{price_spaces}| {quantity}")

total_cost = sum(item['Price'] * item['Quantity'] for item in order_list)
print(f"\nTotal Cost: ${total_cost:.2f}")
