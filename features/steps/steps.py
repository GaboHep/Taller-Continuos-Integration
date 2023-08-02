# steps.py

from behave import given, when, then
from dining_experience_manager import (
    display_menu,
    validate_quantity,
    calculate_cost,
    confirm_order,
    dining_experience_manager
)

# Global variables to store the meal and quantity
meal = None
quantity = None

@given("the Dining Experience Manager is running")
def step_impl(context):
    # Initialize meal and quantity to None at the beginning of each scenario
    global meal, quantity
    meal = None
    quantity = None

@when("I view the menu")
def step_impl(context):
    # Capture the output to check later
    from io import StringIO
    from contextlib import redirect_stdout
    with redirect_stdout(StringIO()) as f:
        display_menu()
    context.displayed_menu = f.getvalue()

@when("I enter the name of a meal from the menu")
def step_impl(context):
    global meal
    meal = "Chaulafan"

@when("I specify the quantity for the meal")
def step_impl(context):
    global quantity
    quantity = 2

@then("the meal and quantity should be added to the order list")
def step_impl(context):
    orders = {meal: quantity}
    total_cost = calculate_cost(orders)
    assert meal in orders
    assert orders[meal] == quantity
    assert total_cost == quantity * 10

@when("I specify an invalid quantity for the meal")
def step_impl(context):
    global quantity
    quantity = -1

@then("I should be prompted to re-enter the quantity")
def step_impl(context):
    assert quantity is None, "Quantity should be None after invalid input"

@when("I select multiple meals with quantities")
def step_impl(context):
    global meal, quantity
    meal = "Chaulafan"
    quantity = 3

@then("the total cost should be calculated correctly based on the base cost and discounts")
def step_impl(context):
    orders = {meal: quantity}
    total_cost = calculate_cost(orders)
    assert total_cost == (quantity * 5)
    if quantity > 5:
        total_cost *= 0.9
    if quantity > 10:
        total_cost *= 0.8
    assert total_cost == calculate_cost(orders)

@when("I select multiple meals with quantities to exceed $50 in total cost")
def step_impl(context):
    global meal, quantity
    meal = "Chaulafan"
    quantity = 11

@then("a discount of $10 should be applied to the total cost")
def step_impl(context):
    orders = {meal: quantity}
    total_cost = calculate_cost(orders)
    assert total_cost == (quantity * 5)
    if quantity > 5:
        total_cost *= 0.9
    if total_cost > 50:
        assert total_cost == ((quantity * 5) * 0.8) - 10

@when("I select multiple meals with quantities to exceed $100 in total cost")
def step_impl(context):
    global meal, quantity
    meal = "Chaulafan"
    quantity = 21

@then("a discount of $25 should be applied to the total cost")
def step_impl(context):
    orders = {meal: quantity}
    total_cost = calculate_cost(orders)
    assert total_cost == (quantity * 5)
    if quantity > 5:
        total_cost *= 0.9
    if total_cost > 50:
        total_cost -= 10
    if total_cost > 100:
        assert total_cost == ((quantity * 5) * 0.8) - 25
