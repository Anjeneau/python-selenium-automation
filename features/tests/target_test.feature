# Created by Anjeneau at 9/17/2024
Feature: Target Features
 Verifies that “Your cart is empty” message is shown and user can navigate to Sign In Page


  Scenario: Verify a logged out user can navigate to Sign In Page
    Given Open Target page
    When Click Sign In Button
    And From right side navigation menu, click Sign In
    Then Verify Sign In form opened


  Scenario: Verify Target Circle Benefits
    Given Open Target Circle page
    When Find Benefits
    Then Verify Benefits