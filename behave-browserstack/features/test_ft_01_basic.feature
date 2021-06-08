Feature: To test basic features of the website.
  Background: Log into the website
    Given user opens the store page "http://react-shooping-cart.netlify.app"

  Scenario: To test item values and functionality buttons
    Given user adds an item to the cart
      |name|
      |Cabbage - Nappa|
    When user goes to cart
    Then check that item exists in cart
    And check value of total items is "1" and total payment is correct
    And check that delete button appears for the added item
    And click clear button
    And check that cart is clear

  Scenario: To test quantity increase and decrease functionality
    Given user adds an item to the cart
      |name|
      |Bagels Poppyseed|
      |Bacardi Breezer - Tropical|
    When user goes to cart
    And for the first item, increase quantity to "3"
    Then check value of total items is "4" and total payment is correct
    And check that reduce button displays for the first item
    And check that Delete button displays for the second item
    And for the first item, decrease quantity to "2"
    And check value of total items is "3" and total payment is correct
    And delete the second item
    And check that the first item is removed from cart
    And click checkout button
    And check that message “Checkout successfully” displayed
    And check that cart is clear