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
def calculate_cost(orders):
    total_cost = 0
    total_quantity = 0
    special_meals = False

    for meal, quantity in orders.items():
        if meal in menu:
            meal_cost = menu[meal]
            total_cost += meal_cost * quantity
            total_quantity += quantity
            if meal == 'Chef\'s Specials':
                special_meals = True
        else:
            print(f"Meal '{meal}' is not available. Please re-select your meals.")
            return -1

    if total_quantity > 100:
        print("Maximum order quantity exceeded. Please re-enter the quantities.")
        return -1

    if total_quantity > 5:
        total_cost *= 0.9

    if total_quantity > 10:
        total_cost *= 0.8

    if total_cost > 50:
        total_cost -= 10

    if total_cost > 100:
        total_cost -= 25

    if special_meals:
        total_cost *= 1.05

    return int(total_cost)
