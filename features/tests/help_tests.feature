Feature: Tests for Help pages

  Scenario: User can select Help topic Promotions & Coupons
    Given Open Help page for Returns
    Then Verify help Returns page opened
    When Select Help topic Promotions & Coupons
    Then Verify help Current promotions page opened

  Scenario: User can select Help topic About Target Circle
    Given Open Help page for Returns
    Then Verify help Returns page opened
    When Select Help topic Target Circle™
    Then Verify help About Target Circle page opened


  Scenario: User can select Help topic About Holiday Help
    Given Open Help page for Returns
    Then Verify help Returns page opened
    When Select Help topic Holiday Help
    Then Verify help Holiday Help page opened