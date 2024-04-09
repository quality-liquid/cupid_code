# Test Design

## Philosophy
Our goal was to have good general coverage for the most frequent use cases. By writing unit tests and using tools and testers to go through our app we will have at least [percentage]% coverage. 

**Serverside and Database**

Our backend views have been broken down to only do 1-2 things each. This allows the tests written for each view to be more in depth and detailed when testing the functionality.

The database is not being tested directly but moreso ensuring when accessing it, it gives good input. This is done with the views as we had dedicated views for doing explicitly that. This design decision was for abstraction and security and our tests will abide that rule as well.

**Testing Types**

*Unit Testing*

This will be the primary type of testing on the backend since most of what the server does is take input and return an expected output to be returned to the UI frontend. Unit Testing is great for testing components on their own and how they behave to controlled input. This is great for detecting potential bugs in the system at any point of the development or maintenance. 

*Integration Testing*

Not done yet. [Explain]

*Regression Testing*

This is technically not writing any new tests but instead just rerunning the old ones. Since we have Unit Tests written, these will be rerun whenever a new feature is added or a bug is fixed to ensure nothing else is broken after the fixes and updates.

For the UI, if any major changes occur we will run the tests written with Selenium and have testers run through the system to ensure that the UI is intuitive and every clickable component gives what is expected.

*System Testing*

We will ensure the app can be used on phone and computer, ensure the UI doesn't break, and make sure there is proper security both in the Frontend and Backend when getting data. This will include testing input validation so no code or SQL injections can occur.

*Acceptance Testing*

This will be done when we present the product to stakeholders and the customer when showing the MVP.

## Tools Being Used
-   MagicMock
-   Django & Django REST testing frameworks
-   Unit tests
-   Selenium

## Bug Handling
Write about known bugs here & if any what our plan for handling them is