@products
Feature: Products feature

    @create_product_manually
    Scenario: Create product manually
        Given I go to the products page
        When I add a new product manually
        Then I confirm the product was placed in "PENDING" status

#    @create_product_manualee
#    Scenario: Create product manually
#        Given I go to the products page
#        When I add a new product manually
#        Then I confirm the product was placed in "PENDING" status