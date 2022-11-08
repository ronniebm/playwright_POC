Feature: products feature

    @products
    Scenario: Create product manually
      Given I go to the products page
      When I add a new product manually
#      Then I confirm the product is placed in "PENDING" status

  #  Scenario: products scenario
  #    Given the products page is displayed
  #    When the user performs a log in
  #    And the user set client and service area
  #    Then is redirected to the entry page
