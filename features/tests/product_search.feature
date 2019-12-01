# Created by rev19 at 10/16/2019

Feature: Test for Amazon Search functionality
  # Enter feature description here

 Scenario: User can search for a product
    Given Open Amazon page
    When Search for dress
    Then Search results for dress is shown
   #when and then can use any product, methods are defined for "product"


  Scenario: User can add goggles into the cart
    Given Open Amazon page
    When Search for goggles
    And Open the first product search result
    And Click Add to cart button
    Then Verify cart has 1 item
    Then Verify Goggles in the cart



  Scenario: User can add phone into the cart
    Given Open Amazon page
    When Search for phone
    And Open the first product search result
    And Click Add to cart button
    Then Verify cart has 1 item
    #Then Verify goggles in the cart

  Scenario: User can add printer paper product into the cart
    Given Open Amazon page
    When Search for printer paper
    And Open the first product search result
    And Click Add to cart button
    Then Verify cart has 1 item

   Scenario: User can add pillow product into the cart
    Given Open Amazon page
    When Search for pillow
    And Open the first product search result
    And Click Add to cart button
    And Close suggestion side section
    Then Verify cart has 1 item