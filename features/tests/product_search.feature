# Created by rev19 at 10/16/2019
Feature: Test for Amazon Search functionality
  # Enter feature description here

 Scenario: User can search for a product
    Given Open Amazon page
    When Search for dress
    Then Search results for dress is shown
   #when and then can use any product, methods are defined for "product"

  Scenario: User can add printer paper product into the cart
    Given Open Amazon page
    When Search for printer paper
    And Open the firts product search result
    And Click Add to cart button
    Then Verify cart has 1 item
