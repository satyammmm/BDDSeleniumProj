Feature:Amazon Test Case
@completed
Scenario: 1. Launch browser
    Given launch browser
    When get amazon url
    Then page should appear

@completed
Scenario: 2. Search For An Non-Existing Product
    Given assert flag from scenario 1
    When click on search icon and search for non existing product
    Then No result found should be displayed

@completed
Scenario: 3. Search For An Existing Product
    Given assert flag from scenario 2
    When click on search icon and search for existing product
    Then result should be displayed

@completed
Scenario: 4. Add a product to the cart
    Given assert flag from scenario 3
    When select first result from search result
    Then selected product should be added to cart

@completed
Scenario: 5. Remove product from the cart
    Given assert flag from scenario 4
    When remove product form the cart
    Then cart should be empty