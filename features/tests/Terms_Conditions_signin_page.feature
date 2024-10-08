# Created by Anjen at 10/7/2024
Feature: Terms and Conditions from sign in page

  Scenario:User can open and close Terms and Conditions from sign in page
    Given Open sign in page
    And Store signin window
    When Click on Target terms and conditions link
    And Switch to the newly opened window
    Then Verify Terms and Conditions page is opened
    And User can close new window and switch back to original
