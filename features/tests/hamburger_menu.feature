# Created by rev19 at 10/20/2019
Feature: Test for hamburger menu functionality
  # Enter feature description here

  Scenario: Amazon Music has 6 menu items
    Given Open Amazon page
    When Click on hamburger menu
    And Click on Amazon Music menu item
    Then 6 menu items are present

 Scenario: Verify ham menu present
    Given Open Amazon page
    Then Verify that hamburger menu is present

