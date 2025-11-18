# Test Design Overview

## Philosophy

Existentialism.

Just kidding. Our goal in testing is to ensure that we produce a quality application that can endure the myriad of cases presented by end users in production. The hope is that we can find most major bugs in development, and minimize the amount of bug finding performed by the end user. In order to accomplish this goal, we will employ tests across the spectrum: unit, integration, system, and acceptance tests. This will ensure that the application is of high quality from functions and classes up to user interface.

**Serverside and Database**

One important aspect of our testing process is testing the backend Django views and their interactions with the database. Ideally, backend behaviors have been separated into discrete, easy-to-use functions through Django's ORM. This is an important subject of our test design, as it is foundational to data integrity, security, and perhaps most importantly application functionality.

**Clientside and the End User**

In essence, acceptance testing will consist of ensuring that navigation in the UI is as expected, and every button leads where it is expected to. This will ensure usability and ease of navigation in production, and satisfaction for our users.

**Testing Types**

- **Unit Testing**
  - Unit testing forms the backbone of our testing strategy, particularly for the backend components of our application. 
  - Given the nature of our server-side operations, which primarily involve processing input and delivering expected output to the UI, unit tests are invaluable for isolating and validating individual components. 
  - By subjecting each component to controlled inputs and meticulously examining their responses, we can detect and address potential bugs early in the development lifecycle.
  - As a new team, our intention will be to better implement unit tests with the new components we have added as well as better flesh out the unit tests written by the old team. They stated that they didn't have a whole lot of time to fully implement it and we have lots of components that could easily be verifiable using unit tests.
  - As a new team, we also intend to better utilize this in our CI/CD pipeline as it is currently a lot of "CD" without a lot of "CI" automatically running the tests for us mostly because there aren't a lot of unit or integration tests to run.
- **Integration Testing**
  - Integration testing plays a crucial role in validating the seamless interaction between different components of our application. 
  - While currently pending, our integration testing efforts will focus on testing the integration points between various modules and subsystems to ensure their cohesive operation.
  - As a new team, our intention will be to better implement integration tests with the new components we have added. They stated that they didn't have a whole lot of time to fully implement it and in addition to having many components added we have also relied on a lot of moving parts within our system that could be tested as part of integration testing.
  - As a new team, we also intend to better utilize this in our CI/CD pipeline as it is currently a lot of "CD" without a lot of "CI" automatically running the tests for us mostly because there aren't a lot of unit or integration tests to run.
- **Regression Testing**
  - Regression testing forms an integral part of our ongoing maintenance and development efforts. 
  - Rather than solely focusing on crafting new tests, regression testing involves systematically rerunning existing tests whenever a new feature is added or a bug is resolved. 
  - This ensures that any changes or updates do not inadvertently introduce regressions or disrupt existing functionality.
  - As a new team, we intend to ensure good compatibility as we continue testing to prevent adding anything that breaks to our production branch. Regression testing will be done before it gets to touch production.
- **System Testing**
  - System testing encompasses a comprehensive evaluation of the entire application ecosystem, including its compatibility across different devices and platforms, UI consistency, and adherence to security standards. 
  - This includes rigorous validation of input data to mitigate the risk of code or SQL injections, ensuring robust data security measures are in place.
  - As a new team, we will try to understand what the previous team did for their system testing and adhere to those standards as well as make sure our new additions maintain the system security that they had.
- **Acceptance Testing**
  - Acceptance testing serves as the final validation phase before presenting the Minimum Viable Product (MVP) to stakeholders and customers. 
  - It involves meticulously verifying whether the delivered product meets the predefined acceptance criteria and aligns with the stakeholders' expectations.
  - Our presentation in class will simulate acceptance testing. As a new team, we will ensure that all requirements that were not met are accounted for in preparation for the next team to take over.

## Journey to Testing
We have struggled to put in a lot of formal testing work throughout the previous sprints. We planned to write at least some of the different types of tests whilst we worked in the development sprints, but this workflow was harder than we had anticipated and we all struggled to write and formal tests for our various features we worked on. 

Everyone has performed what appears to be sufficient informal testing (print statements, console logs, manual tests of the different website features, etc) for all of their work but we have not arrived at setting up the official Selenium testing suite or other written software tests yet.

We are now writing this test document to come up with our formalized testing plan, and will be spending much of sprint 5 implementing all of the test types we wish to employ to ensure our softwares funcionality.

We have some varying levels of expertise on testing software in the team. One team member works in mainly in software testing right now which we hope to put to use to accelerate and enhance our testing implementation process.

Overall, we have learned a lot about the importance of writing tests as your are implementing rather than at the feature freeze. It was easy to put them off, because there was already so much to do for our requirements on top of testing implementation, but our testing sprint would have been easier had we been writing more formal tests along the way. Though we should still be able to get everything working for the testing suite, we did do good work in the informal testing of our features before pushing them to develop so we expect to not find too many project critically damaging bugs.

### Lessons Learned

So far we have mainly done manual testing, but something that we have learned is that even small changes can have unintended side effects. We expect that automated testing will be much more telling and effective in finding bugs.

### Encountered Bugs

During development, we noticed some bugs that will require more investigation and resolution. Notable issues include a few buttons that stopped working in certain sections of the UI and inconsistent formatting across various pages. These are indicative of other potential issues and we expect to find more as we scale up our testing efforts. As we move into more comprehensive testing in the coming phases, we anticipate uncovering additional edge cases and integration issues that will require attention.

## Tools and Frameworks

In our testing endeavors, we leverage a variety of tools and frameworks to streamline our processes and enhance efficiency:

- MagicMock: 
  - Used for backend view testing, enabling the creation of mock objects to simulate real-world scenarios.
- Django & Django REST testing frameworks: 
  - Integral for testing Django-based applications and RESTful APIs, providing robust testing capabilities and streamlined workflow.
- Unit tests: 
  - Employed extensively for unit testing backend components, facilitating isolated testing and validation of individual units of code.
- Selenium: 
  - Used for UI testing, enabling automated testing of web applications across different browsers and platforms.
  - As the interactions with the UI rely on a functioning backend and frontend, the use of Selenium also allows us to test our system as a whole.
- Django Browsable API and Django Debug Toolbar:
  - Leveraged for API testing, allowing for interactive exploration of API endpoints and detailed debugging capabilities.

## Bug Handling Strategies

Our approach to bug handling is characterized by proactive identification, prompt resolution, and continuous improvement:

During the development phase, we prioritize the immediate resolution of bugs as they are discovered, fostering a culture of continuous improvement and quality assurance. 
Experiences have underscored the importance of addressing issues promptly, even if it entails making significant changes to the codebase. 
While such changes may occasionally be disruptive or inconvenient, they ultimately contribute to the enhancement and refinement of our application.

Post-deployment, our bug handling approach adopts a more cautious and methodical stance. 
Bugs identified after deployment are meticulously triaged and prioritized based on their severity and impact on functionality. 
Critical issues that significantly impede usability or compromise security are given the highest priority and addressed expediently. 
Conversely, lower-priority bugs, while acknowledged, may be deferred for resolution based on available resources and project timelines.

In all cases, known bugs are meticulously documented, and our bug handling plan is transparently communicated to all stakeholders. 
This ensures accountability, fosters collaboration, and facilitates effective bug resolution within the established timelines and constraints.


## Code Coverage

While making tests it is essential that the tests cover a significant portion of the code such that it can be ensured that the code works as expected. The optimal goal would be that we have tests for 100% of the code in our repository, however, as there is limited time and resources, we will focus on the most essential parts of the project. We will focus our automated tests on the key parts of the program such as the Vues, the helper functions, and the API calls that give functionality to the application. Examples include everything that the Daters, Cupids, and Administrators will see, AI calls, and making sure that the database holds and shares data correctly.

We are aiming to have 75% automated code coverage for the project in order to reduce bugs and ensure functionality. Additionally, we are hoping to have tests that will aim for odd cases of use to find failure paths in the application not just happy paths of use.

## Running tests

TODO (here to end of doc): update for testing updates specific to our team

### Unit tests  

**NOTE: There were complications using MagicMock, particularly with `@patch`, so tests currently won't run. Sorry for the inconvenience**

To set up the environment, navigate to the `Code/` directory and use `poetry` to install the dependencies situated in the `poetry.lock` file. Use the following command to do so:

```poetry install```

To run a unit test using Django's framework, navigate to the `Code/server/` directory, where `manage.py` resides. The tests we wrote are for the `api` application. Use the following command to run the tests:

```python manage.py test api.tests.unit_tests.cupid_tests```

### Automated system tests

One-time setup:

1. Follow the instructions in [Documentation/Manual/installation_manual.md](../../Manual/installation_manual.md) to get poetry set up.
    - The only dependency you really need is selenium, but if you have the project as a whole set up, then you will have selenium
2. Migrate the database (as described in [Code/README.md](../../../Code/README.md)) so you have a fresh database. The tests all rely on a fresh database, so each one restores a backup before running. To ensure there is a backup copy `Code/server/db.sqlite3` to `Code/server/db_backup.sqlite3`
3. Set up your options in `Code/selenium/options.conf`
    - `chrome=true` will use chrome, otherwise firefox will be used
    - `headless=true` will cause the tests to run headless(no browser window) otherwise you will see the browser

Every-time:

1. Ensure the server is up and running for the frontend and backend.[Code/README.md](../../../Code/README.md)
2. Navigate to [Code/selenium](../../../Code/selenium)
3. Ensure you have access to selenium, run `poetry shell` if using poetry.
4. Run all tests with `python run_tests.py`, or run specific tests with `python test_*.py`

### Manual system tests

Use-case: As a cupid, complete a gig and rate the dater.

0. Ensure the server is up and running for the frontend and backend.[Code/README.md](../../../Code/README.md)
1. Sign in as a cupid
    - username: really@me.com
    - password: password
2. Click the "find gigs" link on the home page
3. Claim a gig.
4. Mark the gig as complete.
5. Use the sidepanel to navigate to "Gigs Completed"
6. Click "Rate Dater"
7. Enter a message describing your rating, and select a heart count.
8. Click "Send"

Verify results:
1. Login as the dater (use a new container/profile, incognito/private, or logout first)
    - username: bob@cupidcode.com
    - password: password
2. Use the sidebar to navigate to "Feedback"
3. You should see your new review at the bottom of the list.

Use-case: As a dater, have a conversation with the AI as you plan a date.

0. Ensure the server is up and running for the frontend and backend.[Code/README.md](../../../Code/README.md)
0. Sign in as a dater
    - username: bob@cupidcode.com
    - password: password
0. Click the "Calendar" link on the home page.
0. Click "Plan a date w/AI" above the calendar.
0. In the chat box, give the AI a bare-bones idea for a date. This will force it to use data it already has from your profile in creating a date.
0. Tell the AI that you like the second option, but would prefer it be a full day event. This should have the AI more fully flesh out the date idea.
0. Tell the AI that you've changed your mind and would like a shorter date, and to keep it under a budget of $25. This should once again have the AI more fully flesh out the date idea.
0. Accept the new idea. It should generate a date according to the new specifications.

Use-case: As a dater, have a conversation with another person with the AI listening in.

0. Ensure the server is up and running for the frontend and backend.[Code/README.md](../../../Code/README.md)
0. Sign in as a dater
    - username: bob@cupidcode.com
    - password: password
0. Click the "AI Listen" link on the home page.
0. Find a friend.
0. Click "Start Listening" on the AI Listen page.
0. Have a conversation with your friend close to the built-in microphone.
0. Observe the AI's transcript of the conversation and note its accuracy.
