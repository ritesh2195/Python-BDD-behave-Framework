Feature: Searching product and placing order

  @search
  Scenario: searching a product by login into application

    Given user login into application
    And user search "N no. of product" in search menu
    When user add "product" in cart
    Then user should able to place order of that "product"
