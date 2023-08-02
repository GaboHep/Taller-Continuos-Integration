#Parte de freddy
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
#Parte Gabriel 
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
#Jorge
def confirm_order(orders):
    print("\nOrder Confirmation:")
    for meal, quantity in orders.items():
        print(f"{meal}: {quantity}")
    total_cost = calculate_cost(orders)
    if total_cost == -1:
        return -1
    print(f"Total Cost: ${total_cost}")
    confirmation = input("Confirm order? (Y/N): ")
    if confirmation.upper() == 'Y':
        return total_cost
    else:
        print("Order canceled.")
        return -1
#Yonkani
def dining_experience_manager():
    print("Welcome to the Dining Experience Manager!")
    display_menu()

    orders = {}
    while True:
        meal = input("\nEnter the name of the meal you want to order (or 'done' to finish): ")
        if meal.lower() == 'done':
            break

        if meal not in menu:
            print(f"Meal '{meal}' is not available. Please select a meal from the menu.")
            continue

        quantity = input("Enter the quantity for this meal: ")
        quantity = validate_quantity(quantity)
        if quantity is None:
            continue

        orders[meal] = quantity

    total_cost = confirm_order(orders)
    if total_cost == -1:
        sys.exit(-1)

    print("\nThank you for using the Dining Experience Manager!")
    print(f"Total Cost: ${total_cost}")

if __name__ == '__main__':
    dining_experience_manager()
