Feature: Login into application

  @login
  Scenario Outline: login into application using valid credential

    Given user navigate to login page
    And user enter valid "<email>" and "<password>"
    When user click on the login button
    Then user should be able login successfully
    Examples:
      | email  | password  |
      | mnju@gmail.com  | qwerty  |
      #|vinod1254@gmail.com  | qwerty  |
      #| hddej@gmail.com | hdgefug |

  Scenario: forget password with valid email

