Feature: login feature

    @login
    Scenario: login scenario
        Given the icyte login page is displayed
        When the user performs a log in
        And the user set client and service area
        Then is redirected to the entry page
