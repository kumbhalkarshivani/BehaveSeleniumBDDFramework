Feature: Account Page Feature

Background:
Given user has already logged in to application
|username|password|
|test123456789@test.com|password12345|

@accounts
Scenario: Accounts page title
When user gets the title of the page
Then page title should be "My account - My Shop"

@accounts
Scenario: Accounts section count
Then user gets accounts section
|SECTION NAMES|
|ADD MY FIRST ADDRESS|
|ORDER HISTORY AND DETAILS|
|MY CREDIT SLIPS|
|MY ADDRESSES|
|MY PERSONAL INFORMATION|
And accounts section count should be "5"
