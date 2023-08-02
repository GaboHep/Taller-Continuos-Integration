# dining_experience.feature

Feature: Menu and Meal Selection

  Scenario: Display Menu
    Given the Dining Experience Manager is running
    When I view the menu
    Then I should see a list of available meals and their prices

  Scenario: Select Meals and Quantities
    Given the Dining Experience Manager is running
    When I enter the name of a meal from the menu
    And I specify the quantity for the meal
    Then the meal and quantity should be added to the order list

  Scenario: Meal Quantity Validation
    Given the Dining Experience Manager is running
    When I enter the name of a meal from the menu
    And I specify an invalid quantity for the meal
    Then I should be prompted to re-enter the quantity

  Scenario: Cost Calculation
    Given the Dining Experience Manager is running
    When I select multiple meals with quantities
    Then the total cost should be calculated correctly based on the base cost and discounts

  Scenario: Special Offer Discount
    Given the Dining Experience Manager is running
    When I select multiple meals with quantities to exceed $50 in total cost
    Then a discount of $10 should be applied to the total cost

  Scenario: Special Offer Discount for Large Order
    Given the Dining Experience Manager is running
    When I select multiple meals with quantities to exceed $100 in total cost
    Then a discount of $25 should be applied to the total cost
