# Challenge

This project aims to create a Dining Experience Manager application that allows users to select meals from a menu, specify the quantity for each meal, and calculate the total cost of the order, including any applicable discounts.

## Tool Configuration

![Tool Configuration](img/img1.jpg)

## Installing Behave

![Behave](img/img2.jpg)
Use pip to install Behave:
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

## Acceptance Added

-Menu and Meal Selection 

![Tool Configuration](img/img3.jpg)

![Tool Configuration](img/img4.jpg)

-Meal Quantity Validation 

![Tool Configuration](img/img5.jpg)

![Tool Configuration](img/img6.jpg)

-Cost Calculation 

![Tool Configuration](img/img7.jpg)
![Tool Configuration](img/img8.jpg)

-Special Offer Discount

![Tool Configuration](img/img9.jpg)
![Tool Configuration](img/img10.jpg)


-Execution  ```behave --format=json --outfile=result.json ```
![Tool Configuration](img/img11.jpg)


-File result.json 
![Tool Configuration](img/img12.jpg)


