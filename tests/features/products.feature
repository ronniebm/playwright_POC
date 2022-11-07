@products
Feature: products feature

    Background:
      Given the icyte login page is displayed
      When the user performs a log in
      And the user set client and service area

    Scenario: products scenario
      Given the products page
  #  Scenario: products scenario
  #    Given the products page is displayed
  #    When the user performs a log in
  #    And the user set client and service area
  #    Then is redirected to the entry page
