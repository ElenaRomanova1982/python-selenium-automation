# Created by rev19 at 11/30/2019
Feature: Test for Amazon Prime functionality
  # Enter feature description here

  Scenario: Amazon Prime  main page has 5 cards represented Prime benefits
    Given Open Amazon page
    When Click on Try Prime button
    Then 5 cards represented Prime benefits are present