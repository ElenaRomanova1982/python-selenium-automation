# Created by rev19 at 10/12/2019
Feature: Test for Orders functionality
  # Enter feature description here

  Scenario: Logged our user sees Sign in page when clicking Orders
    Given Open Amazon page
    When Click Amazon Orders link
    Then Verify Sign In page is opened
