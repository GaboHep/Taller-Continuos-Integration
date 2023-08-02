# Challenge

This project aims to create a Dining Experience Manager application that allows users to select meals from a menu, specify the quantity for each meal, and calculate the total cost of the order, including any applicable discounts.

## Tool Configuration

![Tool Configuration](img/img1)

## Installing Behave

To run the tests for this project, you need to install Behave, a popular behavior-driven development (BDD) framework for Python. Follow these steps to install Behave:

1. Open your terminal or command prompt.
2. Use pip to install Behave:
   ```
   pip install behave
   ```

## Generating Features, Steps, Folders, and Files

To generate the required folders and files for Behave, follow these steps:

1. Navigate to the project directory in your terminal or command prompt.
2. Run the following Behave command to generate the necessary structure:
   ```
   behave --init
   ```

This will create the `features` folder and necessary files to start writing your test scenarios.

## Requirements Specified

### Menu and Meal Selection

- The system should display a menu with various dining options and their corresponding prices.
- Users can select multiple meals to order and specify the quantity for each meal.

### Meal Quantity Validation

- The system should validate that the quantity entered for each meal is a positive integer greater than zero.
- If invalid quantities are entered, the Dining Experience Manager should prompt users to re-enter the quantities.

### Cost Calculation

- The base cost for each meal can be decided individually by the system, or it can be $5 each.
- If the total quantity of meals ordered is more than 5, apply a discount of 10% to the total cost.
- If the total quantity of meals ordered is more than 10, apply a discount of 20% to the total cost.

### Special Offer Discount

- The system should have the ability to apply special offer discounts based on certain conditions.
- If the total cost of the meal order exceeds $50, apply a discount of $10 to the total cost.
- If the total cost of the meal order exceeds $100, apply a discount of $25 to the total cost.

## Acceptance Criteria

The project should fulfill the following acceptance criteria:

- Users can see the menu with dining options and prices.
- Users can select multiple meals and specify the quantity for each.
- The system validates the entered quantity for each meal.
- If invalid quantities are entered, users are prompted to re-enter the quantities.
- The system calculates the total cost of the order, including any applicable discounts.
- If the total quantity of meals ordered is more than 5, the system applies a 10% discount.
- If the total quantity of meals ordered is more than 10, the system applies a 20% discount.
- The system can apply special offer discounts if the total cost exceeds $50 or $100.

Feel free to modify this Readme as you add more details or implement additional features to the Dining Experience Manager application. Happy coding!
