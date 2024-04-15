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

**Testing Types**

- **Unit Testing**
  - Unit testing forms the backbone of our testing strategy, particularly for the backend components of our application. 
  - Given the nature of our server-side operations, which primarily involve processing input and delivering expected output to the UI, unit tests are invaluable for isolating and validating individual components. 
  - By subjecting each component to controlled inputs and meticulously examining their responses, we can detect and address potential bugs early in the development lifecycle.
- **Integration Testing**
  - Integration testing plays a crucial role in validating the seamless interaction between different components of our application. 
  - While currently pending, our integration testing efforts will focus on testing the integration points between various modules and subsystems to ensure their cohesive operation.
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
