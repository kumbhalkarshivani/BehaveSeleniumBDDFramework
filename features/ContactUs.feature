Feature: Contact Us Feature

  Background:
    Given user has already logged in to application
    |username|password|
    |test123456789@test.com|password12345|

Scenario Outline: Contact Us scenario with different set of data
Given user navigates to contact us page
When user fills the form from given sheetname "<subjectHeading>" and rownumber "<RowNumber>"
And user clicks on send button
Then it shows a successful message "Your message has been successfully sent to our team."

Examples:
|subjectHeading|RowNumber|
|Customer service|1|
|Webmaster|2|
|Customer service|3|
|Webmaster|4|
|Customer service|5|
|Webmaster|6|