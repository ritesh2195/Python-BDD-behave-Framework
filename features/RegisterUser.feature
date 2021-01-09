Feature: user signup in the application

  @register
  Scenario: SignUp with valid credentials

    Given user navigate to home page
    And user navigate to register page
    And user enter all required information
    When user click on privacy button and click to continue
    Then user should be able to signup into the application
