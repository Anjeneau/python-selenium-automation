# Created by Anjeneau at 9/21/2024
Feature: Cart
 Verifies that “Your cart is empty” message is shown


  Scenario: User can see “Your cart is empty” message
    Given Open Target page
    When Click on Cart icon
    Then Verify “Your cart is empty” message is shown


  Scenario: User can add item to cart
    Given Open Target page
    When Search for plate
    And Click Add to Cart button
    And Confirm Add to Cart
    And View Cart
    Then Verify cart has 1 item
    And Verify cart has correct product


