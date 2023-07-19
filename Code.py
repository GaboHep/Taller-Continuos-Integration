import sys

# Menu with meal options and prices
menu = {
    'Chaulafan': 10,
    'Lasagna': 12,
    'Chocolate Cake': 8,
    'Encebollado': 15,
    'Restaurant Specials' : 13
}

def display_menu():
    print("Menu:")
    for meal, price in menu.items():
        print(f"{meal}: ${price}")

def validate_quantity(quantity):
    try:
        quantity = int(quantity)
        if quantity > 0:
            return quantity
        else:
            print("Invalid quantity. Please enter a positive integer greater than zero.")
            return None
    except ValueError:
        print("Invalid quantity. Please enter a positive integer greater than zero.")
        return None
