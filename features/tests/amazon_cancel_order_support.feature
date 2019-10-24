# Created by rev19 at 10/23/2019
Feature: Customer can search for solution to cancel an order
  # Enter feature description here

  Scenario:  User can search for help to Cancel an Order
    Given Open Amazon page
    When Click Help button
    And Input Cancel Order into search field
    And Click Go button on the Help page
    Then Cancel Items or Orders text is in results