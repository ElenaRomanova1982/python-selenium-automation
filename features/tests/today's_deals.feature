# Created by rev19 at 10/31/2019
Feature: User can add a product from today's deals into the cart and then go back to the previous window,refresh and see cart counter updated to 1
  # Enter feature description here

  Scenario: User can add a product from today's deals into the cart
    Given Open Amazon page
    When Click on Todays deals button
    # And Find first product which allows to add to the cart from Deals page
    And Click Add to cart button todays deals
    And Go back to the previous window and refresh
    Then Verify cart has 1 item