# Test Design Overview

## Philosophy

Our overarching goal in test design is to ensure the robustness, reliability, and overall quality of our application. 
We strive to achieve comprehensive coverage for the most common use cases, aiming for a minimum test coverage of 80%. 
By leveraging a combination of unit tests, integration tests, system tests, and acceptance tests, along with meticulous manual testing, we aim to thoroughly validate the functionality and performance of our application.

**Serverside and Database**

A key aspect of our test design is the meticulous testing of backend views and their interactions with the database. 
We have meticulously structured our backend views to perform discrete tasks, ensuring clarity and simplicity in functionality. 
While direct testing of the database is limited, we prioritize ensuring that accessing it yields valid input and maintains data integrity. 
This is achieved through dedicated views and careful consideration of abstraction and security principles.

**Clientside and the End User**

The main approach is to ensure that every piece that should be clicked on does exactly what the user expects it to. We want our system to be usable and easy to navigate. By using tools and going through demonstrations with stakeholders, we are ensuring major coverage over our project so that any user can successfully navigate and use our website as expected. Making sure every press, link, and button does what it is assumed to do will prove that our UI is tested and properly works.

**Testing Types**

- **Unit Testing**
  - Unit testing forms the backbone of our testing strategy, particularly for the backend components of our application. 
  - Given the nature of our server-side operations, which primarily involve processing input and delivering expected output to the UI, unit tests are invaluable for isolating and validating individual components. 
  - By subjecting each component to controlled inputs and meticulously examining their responses, we can detect and address potential bugs early in the development lifecycle.
  - We did not have time to fully implement this, as there are many use cases we'd undoubtably miss. We also didn't have much time to be thorough. We did talk about potential cases as a team, though.
- **Integration Testing**
  - Integration testing plays a crucial role in validating the seamless interaction between different components of our application. 
  - While currently pending, our integration testing efforts will focus on testing the integration points between various modules and subsystems to ensure their cohesive operation.
  - We did not have time to fully implement this, but it is a crucial part of our testing strategy. Given more time, we would have provided further implementation to ensure that all of our components work together as expected.
- **Regression Testing**
  - Regression testing forms an integral part of our ongoing maintenance and development efforts. 
  - Rather than solely focusing on crafting new tests, regression testing involves systematically rerunning existing tests whenever a new feature is added or a bug is resolved. 
  - This ensures that any changes or updates do not inadvertently introduce regressions or disrupt existing functionality. 
  - Additionally, for UI changes, we employ Selenium tests and manual testing to verify intuitive UI behavior and expected responses from user interactions.
- **System Testing**
  - System testing encompasses a comprehensive evaluation of the entire application ecosystem, including its compatibility across different devices and platforms, UI consistency, and adherence to security standards. 
  - This includes rigorous validation of input data to mitigate the risk of code or SQL injections, ensuring robust data security measures are in place.
  - Testing the system via Selenium allows us to automate some of this work.
- **Acceptance Testing**
  - Acceptance testing serves as the final validation phase before presenting the Minimum Viable Product (MVP) to stakeholders and customers. 
  - It involves meticulously verifying whether the delivered product meets the predefined acceptance criteria and aligns with the stakeholders' expectations.
  - Our presentation in class will simulate acceptance testing.

## Journey to Testing

Daniel and Nate started writing unit tests for the backend components of the application during sprint five. 
We tested every view and helper function with one good and one bad test case. 
We did this in the interest of time and to ensure that we had a good amount of coverage over our backend components.
If we had more time, we would have written more tests for each view and helper function to ensure that we had more coverage over our backend components.
As the unit tests stand now, they cover most of the use cases that we could think of, but there are always more that could be added.
Writing unit tests was tiresome and time-consuming, but it was a good learning experience for both of us.

We then took time to write the user manuals and do manual testing of the application.

After that was done we moved to integration testing. 
We tried our best to get as much testing done as we could.
But we were unable to write all the cases that we wanted to test.
If our team continued to work on this project, we would have written more integration tests to ensure that all of our components work together as expected.
It was easier to write integration tests than unit tests because we had experience writing tests and we had a better understanding of how our components worked together.

We thought about doing white box or black box testing, but we decided that there was no time.
Our plan for black box testing was to pass in random inputs to our views and see if they returned the expected output.
For most of the random inputs, we would expect a 404 error. But no matter the input we would expect a response with no errors being thrown on the server. The random inputs would try to simulate someone trying to test our functionality without knowing how everything works. We could also get someone to test our program, similar to acceptance testing, to reduce bias on our part (even if we choose random inputs, we know how it works, so the "random" inputs may not be so random). 

For white box testing, we would need to find someone knowledgeable with our framework and web application development and/or design to look at the system and test its functionality. These kind of people are a bit trickier to hunt down.

If we wished to do grey box testing, we could find someone who is familiar with one of the frameworks we are using, restricting their clarity on our system. We'd also withhold sections, so then the "attacker" would only know part of our system.

### Lessons Learned


### Covered Bugs



## Tools and Frameworks

In our testing endeavors, we leverage a variety of tools and frameworks to streamline our processes and enhance efficiency:

- MagicMock: 
  - Utilized for backend view testing, enabling the creation of mock objects to simulate real-world scenarios.
- Django & Django REST testing frameworks: 
  - Integral for testing Django-based applications and RESTful APIs, providing robust testing capabilities and streamlined workflow.
- Unit tests: 
  - Employed extensively for unit testing backend components, facilitating isolated testing and validation of individual units of code.
- Selenium: 
  - Utilized for UI testing, enabling automated testing of web applications across different browsers and platforms.
  - As the interactions with the UI rely on a functioning backend and frontend, the use of Selenium also allows us to test our sytem as a whole.
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
Comparing the existing unit tests and integration tests to the views and helper functions, a rough estimate of code that is covered by these tests could be roughly 70%. Quite a few of the helper functions are not covered by the tests, and some of the views utilize those functions.

An important factor is the lack of comprehension for the tests. There are many different tests that could be written, but as stated previously, timme made it difficult to cover many cases, including edge cases. If these are factored in, then the code coverage could be considered to be roughly 60%.

We also calculated an estimate of how many bugs may be present in the code using the statistic that 15-50 bugs per 1,000 lines of code. In the backend, we have roughly 4,991 lines of code in the backend and 3,737 lines of code in the front end.