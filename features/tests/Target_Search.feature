# Created by Anjeneau at 9/21/2024
Feature: Search Test
  Verify test feature work properly

  
  Scenario: User can search for mug
    Given Open Target page
    When Search for mug
    Then Verify search results correct for mug

