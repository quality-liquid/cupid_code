# **New Cupid Code Low Level Design**

* Team 3, *The Sinister Six*
* Sprint Leader: Tyson Buxton
* Frontend Design
    * Reece Nielson
    * Saxton Calvert
* Middleend Design
    * Tyson Buxton
* Backend Design
    * Garrett Woodhouse
    * Felix Jacob
    * Benjamin Hickenlooper

### Links

0. [Requirements](../Requirements/new-requirements-team3.md)
0. [High Level Design](../HighLevel/new-high-level-team3.md)

Note: This document builds on the previous team's low-level design. For areas not explicitly changed here, see [previous team's low level docs](./low_level_docs.md).

### Table of Contents

0. [Team Conventions](#0-team-conventions)
0. [Frontend Design](#1-frontend-design)
    * [Security](#security)
    * [Performance](#performance)
    * [UI](#ui)
      * [User flow:](#user-flow)
      * [Screen designs:](#screen-designs)                                                         
      * [Navigation Structure:](#navigation-structure)
      * [Layout guidelines:](#layout-guidelines)
      * [Color Palette:](#color-palette)
      * [Icon Use:](#icon-use)
      * [Responsive design:](#responsive-design)
      * [Making accounts and logging in](#making-accounts-and-logging-in)
      * [Dater](#dater)
      * [Cupid](#cupid)
      * [Manager](#manager)
    * [UX](#ux)
    * [Templates](#templates)
    * [Vue Router](#vue-router)
    * [Testing](#testing)
0. [Middleend Design](#2-middleend-design-connecting-vue-and-django)
    * [Summary](#summary)
    * [Poetry](#poetry)
    * [Vite Config](#vite-config)
    * [Node.js](#nodejs)
    * [npm](#npm)
    * [Serverside](#serverside)
    * [Clientside](#clientside)
    * [Pseudocode](#pseudocode)
0. [Backend Design](#3-backend-design)  
    * [Backend Summary](#backend-summary-revisit-this-after-everything-else-is-done)
    * [Resources for the Backend](#resources-for-the-backend)
    * [Performance](#performance-1)
    * [Django Project Structure](#django-project-structure)
    * [Django Admin](#django-admin)
    * [Unit Tests](#unit-tests)
    * [URL Mapping](#url-mapping)
    * [Django Settings](#django-settings)
    * [Backend Pseudocode](#backend-pseudocode)
    * [Django Models](#django-models)
    * [Django Migrations](#django-migrations)
    * [External API's](#external-apis)
    * [Tutorial for Django REST](#quick-tutorial-on-how-to-use-the-django-rest-framework)

# 0. Team Conventions

*[Table of Contents](#table-of-contents)*

*See [previous team's conventions](./low_level_docs.md#team-conventions-and-standards)*

The Sinister-six will be following all of the same conventions outlined by the previous team except for the following changes outlined below.

## Branching

*See [previous team's branching conventions](./low_level_docs.md#branching-conventions)*

We will classify our branches into these four types, to keep our version control workflow consistent and coherent.
* *master*
  * Always working; whenever merges are done we do not get up/stop working until we are confident *master* is functioning with the new code that was merged in.
  * The actual application Users are using will be built/deployed with this code.
* *hotfix*
  * Branched off of *master*.
  * For fixing issues we missed when merging into *master* from *development*
* *development*
  * Branched off of *master*.
  * Get code ready to merge with *master*.
* *feature/fixes*
  * Branched off of *development*.
  * This category would also include *sub-feature* branches coming off of a *feature* branch; used to break up the work for the larger *feature* branches.
  * Development of features and experimentation of ideas which will merge into *development* once they are functioning.

## Coding Standards

*See [previous team's code standards](./low_level_docs.md#coding-standards)*

We will follow all of the previous team's coding standards except for the following:
* New lines of code will be limited to 100 columns or less rather than the previous limit of 200 to increase code readability.
* Attention will be made to import only the methods, attributes, objects, etc...which we actually use from a package rather than blanket imports of entire packages. I.e. use `from _ import _, _, ...` rather than `import _`.


# 1. Frontend Design

[*Table of Contents*](#table-of-contents)

#### Subsections

* [Security](#security)
* [UI](#ui)
* [UX](#ux)
* [Templates](#templates)
* [Vue Router](#vue-router)
  * [Implementation](#implementing-the-router)
* [Testing](#testing)

## Security

*See [Previous team's security design](./low_level_docs.md#security)*

The previous team had done a good job in maintaining security within the app. They did not implement a strong password system, which we will implement by... 

If a user loses their account information, a form of Two-Step Authentication will be provided to allow them to reset their password and enter their account. Managers will also require Two-Step Authentication every time they log in. We will do this by...

We also intend to make calls to external APIs and thus we need to ensure that we safeguard any response that could be malicious. We will do this by...

---
Final Note:
* We did implement a strong password system that was a good boost to security.
* We were unable to setup the two-step authentication for any type of user.
* We did make calls to external APIs, we worked to create security for this by using .env files properly to make all API keys grabbed dynamically from .env files so they could not be found in the repository.

---

## Performance

*See [Previous team's performance design](./low_level_docs.md#performance)*

The frontend will verify any inputs that it can before making requests to the backend to lower the amount of requests made to the backend. For example, the frontend will check that an entered email is valid before making a request. Since the page is a single page application, we are also able to reduce the number of requests to the backend.

By reducing how many requests we make to the server, the user is able to interact with the app more without having to wait for constant responses from the server.

---
Final Note:
* This was implemented as a single page application.
* We did work to implement error handling in frontend code to check for problems.

---

## UI

*See [Previous team's UI design](./low_level_docs.md#ui)*

The application as handed to us was well designed for intuitive clicking and use for the features it had. We intend to make more features immediately accessible on the landing page and make some changes to the color scheme. There will be a dark scheme and a light theme to make it more accessible. Clear instructions will continue to be provided as needed

---
Final Note:
* Toggle for light and dark theme was implemented.

---

### User Flow:

*See [Previous team's User Flow design](./low_level_docs.md#user-flow)*

The user flow as handed to us in the application was well designed. There will be slight changes to the home page relative to new features pertinent to the type of user. Daters will be able to see upcoming dates and their Cupid Cash balance. They will also be able to, from the home page, access their date calendar, an AI chatbot for advice and plans, the new Plan-a-Date feature, their Cupid Cash wallet and history, all their Gig requests, their profile page, a feedback page, and the ability to allow the AI to start listening and provide live feedback. Cupids will be able to clock in and out and see how many available gigs there are, how many gigs they've completed, and how much they've earned. Cupids will have home page access to the list of nearby gigs and how many are active, their active gig(s) and status(es), their profile page, and a feedback page. A recent activity list and a weekly earnings report will also be on the page. Platform admin managers will be able to see metrics on how many total and active daters, total and active cupids, total and monthly revenue, and critical issues including those that are pending. A general platform health dashboard with key performance indicators will also be displayed with recent platform activity. Access to a report system, the feedback reviews, user management, financial reports, analytics, and cupid schedule reports will also be available with a status page. Each of these buttons are tap sensitive and dynamically redirect the specific user to the destination indicated.

### Screen Designs:

*[Previous team's Screen Designs](./low_level_docs.md#screen-designs)*

Creating a dark theme while also maintaining the contrast present as handed to us across the application is important. Important information will be made more easily accessible with no need to scroll or swipe, the most important being locked at the top of the screen in the case of a scroll. Our main customer is a mobile user, so all screen designs will be designed as "mobile-first" architecture.

### Navigation Structure:

*See [Previous team's Navigation Structure](./low_level_docs.md#navigation-structure)*

The existing design for the navigation structure will be kept in place.  

### Layout Guidelines:

*See [Previous team's Layout Guidelines](./low_level_docs.md#layout-guidelines)*

The existing design for the layout guidelines will be kept in place.  

### Color Palette:

*See [Previous team's Color Palette](./low_level_docs.md#color-palette)*

This represents the primary set of colors that will be used across the application in both its light and dark themes.
* **Black**: `#0A0908`
* **Salmon Pink**: `#E5989B`
* **Old Rose**: `#B5838D`
* **Gunmetal**: `#22333B`
* **Walnut Brown**: `#5E503F`
* **White**: `#FFFFFF`

### Icon Use:

*See [Previous team's Icon Use](./low_level_docs.md#icon-use)*

The existing design for the use of icons will be kept in place.  

### Responsive Design:

*See [Previous team's Responsive Design](./low_level_docs.md#responsive-design)*

The app's portrait orientation and general "mobile-first" design principles will be maintained as the app will primarily be used in mobile settings. Desktop functionality and scalability will be maintained.

### Making accounts and Logging in

*See [previous team's accounts section](./low_level_docs.md#making-accounts-and-logging-in)*

The existing design for making accounts and logging in will be maintained.  

The pages will be updated to reflect the updated visual interface. A new logo will also be integrated.

![create_account_image](images/createacc.png "Create Account")
![login_image](images/login.png "Login")
![logo](images/logo.png "Logo")

### Dater

*See [previous team's Dater design](./low_level_docs.md#dater)*

The Daters will be able to access the 8 following features from their home pages:
* Date calendar from which to schedule and manage their dates.
* AI Chat for chatting and advice.
* Plan A Date for having AI-powered date planning and itineraries.
* Cupid Cash dashboard for getting credits and viewing their history.
* Gig Request dashboard to request Cupid assistance and see the status of their requests.
* Profile to view and edit their information.
* App Feedback to submit reviews and report app issues.
* AI Listening to get real-time date support.

![dater_home](images/uh.png "User Home")
![dater_ai](images/aichat.png "Ai Chat")
![dater_calendar](images/calendar.png "Calendar")
![dater_planner](images/planner.png "Plan A Date")
![dater_cupid_cash](images/cupidcash.png "Cupid Cash")
![dater_add_cash](images/addfunds.png "Add Cupid Cash")
![dater_profile](images/useracc.png "User Account")
![dater_listening](images/listen1.png "Listen")

### Cupid

*See [previous team's Cupid design](./low_level_docs.md#cupid)*

The Cupids will be able to access the following 5 features from their home pages:
* Clock-in and Clock-out mechanism to make themselves available to receive gig notifications.
* Nearby and active Cupid gigs.
* Gigs currently active and their status.
* Profile to view gig history, manage finances, and edit information.
* App Feedback to submit reviews and report app issues.

![cupid_home](images/ch.png "Cupid Home")
![cash_earned](images/ch_cash.png "Cash Earned")
![gig1](images/ch_gig1.png "Gig 1")
![gig2](images/ch_gig2.png "Gig 2")

### Manager

*See [previous team's Manager design](./low_level_docs.md#manager)*

The Manager users who act as administrators for the platform will be able to access the following features:
* Analytics Report System
* Inter-user Feedback
* User Management
* Financial Reports
* Cupid Schedule Reports
* System Status

![manager_home](images/manager_home.png "Manager Home")
![user_management](images/manage.png "User Management")

## UX

*See [previous team's UX design](./low_level_docs.md#ux)*

The existing design for the user experience will be maintained, striving to ensure that they enjoy the app and find a helpful tool to shoulder their dating burdens.  

## Templates

*See [previous team's Templates](./low_level_docs.md#templates) for the base Django template setup and the separate auth app template structure. We follow the same pattern for mounting the Vue bundle and for auth redirects.

## Vue Router

The previous team used Vue Router to switch between pages in the frontend. They used hash routing, which allows page transitions without server calls. We will continue this approach and manage state carefully for responsiveness.
See [previous team's Vue Router Design](./low_level_docs.md#vue-router) and the [Vue Router documentation](https://router.vuejs.org/) for route configuration and navigation guards (e.g., beforeEach) to protect role-specific pages.

### Implementing the router

*See [previous team's router design](./low_level_docs.md#implementing-the-router)*

In main.js, mount the router instance and use router-link for navigation within components. Programmatic navigation (router.push) is used after authentication or role checks.

Refer to [previous team's router setup](./low_level_docs.md#implementing-the-router) for the base router initialization and route guards. We add role guards to protect Dater/Cupid/Manager routes as described above.

## Vue URLs

*See [previous team's Vue URLs](./low_level_docs.md#vue-urls)*

The Vue app will live at URL `/app/`. The following pages will be available through the Vue Router. 

| URL                 | Notes               |
|---------------------|---------------------|
| /                   | Welcome page        |
| /login              | Login page          |
| /register           | Signup page         |
| /dater/home/:id     | dater homepage      |
| /dater/chat/:id     | dater chat page     |
| /dater/listen/:id   | dater listen page   |
| /dater/balance/:id  | dater cash page     |
| /dater/calendar/:id | dater calendar page |
| /dater/planner/:id  | dater planner page  |
| /dater/feedback/:id | dater feedback page |
| /dater/gigs/:id     | dater gigs page     |
| /dater/profile/:id  | dater profile page  |
| /cupid/home/:id     | cupid homepage      |
| /cupid/gigs/        | cupid gigs          |
| /cupid/balance/:id  | cupid balance       |
| /cupid/profile/:id  | cupid profile       |
| /cupid/feedback/:id | cupid feedback page |
| /manager/home/:id   | manager homepage    |
| /manager/cupids/    | manager reports     |
| /manager/daters/    | manager reports     |

The :id syntax is using the params syntax from the Vue Router. These are the URLs that are going to need an id of some sort. If the id is not valid for the page that is being accessed (i.e. dater user trying to access a manager page), a 404 page will be served instead.

See [previous team's URL list](./low_level_docs.md#vue-urls) for the original route map and params rationale. Our updates maintain the same structure with role validation.

## Testing

*See [previous team's preliminary testing designs](./low_level_docs.md#testing)*

We intend to continue using and building upon the existing testing framework going forward in the development of the product. Testing is done in the following ways:

0. **Unit Testing**: Unit tests isolate functions and methods and verify that it outputs the way it is intended. Focus on testing edge cases and potential invalid inputs.

0. **Component Testing**: Vue Test Utils is used to test Vue components and simulate user interactions.

0. **Integration Testing**: Integration tests will verify that multiple components work together and ensure the entire application can work.

0. **Mocking**: Mocking is a technique used in testing to isolate a component that may rely on other components. By using mocking you can "mock" what a function should return and thereby control the behavior of external dependencies to focus entirely on the component under test.

The tests will be run in a CICD pipeline to ensure that changes to the app do not break working functionality. If a change to the code alters what a function inputs and outputs, the developer who made the change is in charge of fixing the corresponding test and ensuring that it works.

See [previous team's Testing](./low_level_docs.md#testing) for the test organization and tooling. We keep per-app tests (api/tests.py) and follow their CI pipeline approach.

### Test pseudocode
Use Django’s test framework for unit and integration tests and Vue Test Utils for component tests. Organize tests per app (e.g., api/tests.py) and cover happy paths, invalid inputs, and edge cases. See [Django Testing Documentation](https://docs.djangoproject.com/en/5.0/topics/testing/) and reuse the existing project’s test structure.

# 2. Middleend Design: Connecting Vue and Django

[*Table of Contents*](#table-of-contents)

*See [previous team's Middleend Design](./low_level_docs.md#connecting-vue-and-django)*

#### Subsections

* [Summary](#summary)
* [Poetry](#poetry)
* [Vite Config](#vite-config)
* [Node.js](#nodejs)
* [npm](#npm)
* [Serverside](#serverside)
* [Clientside](#clientside)
* [Pseudocode](#pseudocode)

## Summary

*See [previous team's summary](./low_level_docs.md#summary)*

Note: Our newly proposed features and add-ons change little for the previous teams designs for connecting the frontend and backend. As such to focus more on our proposed changes and in the interest of following the DRY (Don't Repeat Yourself) principle, only the changes we make will be noted and for the sections where we choose to follow their same plan the previous teams document will be linked with a bit of explanation. 

We will continue to use Vite, Vue, NVM, and NPM for the frontend. With Poetry and Django used for the backend. They are still viable tools for connecting our client and server, maintaining the project packages (NVM, NPM), and maintaining the server environment (poetry).   

## Poetry

*See [previous team's Poetry notes](./low_level_docs.md#poetry)*

We will work to upgrade the lates packages for security and performance.
* `Python v3.12+`
* `Django v5.2.7+`
* `Requests v2.32.5+`
* `Python-dotenv v1.1.1+`

## Vite Config

*See [previous team's Vite Config](./low_level_docs.md#vite-config)*

Nothing should change here from the previous teams setup.  

## Node.js

*See [previous team's Node.js section](./low_level_docs.md#nodejs)*

The version of Node.js will be upgraded to the now [current LTS version](https://nodejs.org/en) `v22.20.0`. Otherwise, we will continue using `nvm` for Node.js management.  

## npm

*See [previous team's npm design](./low_level_docs.md#npm)*

`npm` will continue to be used for package management. We will upgrade the previous teams dependencies to the now current stable versions for security and performance.
* `Vue v3.5.22` see [Vue Releases](https://vuejs.org/about/releases.html)
* `Cookie v1.0.2` see [npm Cookie package](https://www.npmjs.com/package/cookie)

## Serverside

*See [previous team's Serverside](./low_level_docs.md#serverside)*

### Files to Add

See [previous team's Files to Add section](./low_level_docs.md#files-to-add)

This will continue with the same steps.  

### Environment

*See [previous team's Environment](./low_level_docs.md#environment)*

The same environment setup will be followed.  

### Middleware

*See [previous team's Middleware](./low_level_docs.md#middleware)*

* The Django framework comes with built in middleware to handle all of our needs for authentication, data passing, and the like. Thus we will rely on the optimized and professionaly build Django included middleware for connecting the frontend and backend.

### In Server Settings

*See [previous team's Server Settings](./low_level_docs.md#in-server-settings)*

* Import load_dotenv from dotenv (python-dotenv)
* Add a Debug check for asset middleware:
  * if DEBUG: MIDDLEWARE.append('core.middleware.asset_proxy_middleware')

### In Core views.py

See [previous team Core views section](./low_level_docs.md#in-core-viewspy)

The same setup will be followed as the previous team.

### In Core index.html

See [previous team Core index section](./low_level_docs.md#in-core-indexhtml)

The same setup will be followed as the previous team.


## Clientside

See [previous teams Clientside instructions](./low_level_docs.md#clientside).

The previous team's instructions here are the same for the project as it will become with out implementation.

## Pseudocode

See [previous team pseudocode](./low_level_docs.md#pseudocode)

Their pseudocode covers the same as what we will implement.  

# 3. Backend Design

*See [previous team's backend design](./low_level_docs.md#backend-design)*

[*Table of Contents*](#table-of-contents)

#### Subsections

* [Backend Summary](#backend-summary-revisit-this-after-everything-else-is-done)
* [Resources for the Backend](#resources-for-the-backend)
* [Performance](#performance-1)
* [Django Project Structure](#django-project-structure)
* [Django Admin](#django-admin)
* [Unit Tests](#unit-tests)
* [URL Mapping](#url-mapping)
* [Django Settings](#django-settings)
* [Backend Pseudocode](#backend-pseudocode)
* [Django Models](#django-models)
* [Django Migrations](#django-migrations)
* [External API's](#external-apis)
* [Tutorial for Django REST](#quick-tutorial-on-how-to-use-the-django-rest-framework)

## Backend Summary (Revisit this after everything else is done)

*See [previous team's Backend Summary](./low_level_docs.md#backend-summary) for the baseline DRF architecture and auth flow we continue to use.

    The backend will be built using Django and the Django REST Framework. As a result much of the needed security is already implemented. A majority of the work will be in the models, views, and serializers. The models will be the database, the views will be the API, and the serializers will be the conversion of the models to JSON and vice versa. The frontend will communicate with the backend using HTTP GET and POST requests. The backend will respond with JSON data. This will be made easy by the Django Rest Framework. Mapping what endpoints the frontend needs is helpful for the backend to know what to build. This will be done in the URL Mapping section.
        Additionally, the data will be stored in Azure Cloud to make it more scalable, accessible, and secure.
        One more thing to note is that the Agentic AI will have access to communicate with both the back end and the front end. It will be expected to pull data from the database, and then transport it and use it automatically.

## Resources for the Backend 

*See [previous team's Backend Resources](./low_level_docs.md#resources-for-the-backend) for core references; we add Azure, LM Studio, and LangChain links.

[Django Rest Framework Quickstart](https://www.django-rest-framework.org/tutorial/quickstart/)   
[Django Rest Framework API Reference](https://docs.djangoproject.com/en/5.0/ref/)  
[Django Rest Framework Serializers](https://www.django-rest-framework.org/api-guide/serializers/)  
[Django Rest Framework Views](https://www.django-rest-framework.org/api-guide/views/)  
[Django Rest Framework Permissions](https://www.django-rest-framework.org/api-guide/permissions/)  
[Django Rest Framework Authentication](https://www.django-rest-framework.org/api-guide/authentication/)  
[Azure Cloud Documentation](https://learn.microsoft.com/en-us/azure/?product=popular)  
[LM Studio Documentation](https://lmstudio.ai/docs/app)  
[LangChain Agentic AI documentation](https://python.langchain.com/docs/tutorials/agents/)


## Performance:

*See [previous team's backend performance designs](./low_level_docs.md#performance-1) for caching, throttling, and ORM guidance retained in our approach.

### Largest Changes from the Previous Team

The majority of the changes in this section have to do with updating the document to show that we are using Azure Cloud instead of SQL lite and that we are going to be using an agentic AI instead of a regular AI model.


* Django
    * Provides a lot of performance optimizations out of the box.
    * Mature framework that has been optimized for performance over many years.
    * Used by many large websites and can handle a lot of traffic.
    * Synchronous framework, which means it can handle a lot of requests at once.
    * Built-in caching system that can help improve performance.
    * Built-in ORM that can help optimize database queries.
    * Built-in middleware system that can help optimize requests.
* Django Rest Framework
    * Built on top of Django and inherits many of its performance optimizations.
    * Designed to be fast and efficient.
    * Used by many large websites and can handle a lot of traffic.
    * Built-in caching and throttling systems that can help improve performance.
    * Built-in serializers that can help optimize data serialization.
    * Built-in viewsets and routers that can help optimize request handling.
* Hardware
    * We plan to run the backend on the cloud. This will allow us to have a more accessible dataset and also more resources on our personal hardware.
    * We will need to monitor the hardware to ensure that it is running optimally and make any necessary changes to improve performance.
    * We will be running our AI agent locally from LM Studio and using frameworks such as LangChain. This will allow us more control over the AI, but we will need to be cognizant of how this might affect performance and how we will scale this as the product grows toward deployment.
* Network
    * The internet service provider will need to be able to handle the traffic that we are generating.
    * We will need to monitor the network to ensure that it is running optimally and make any necessary changes to improve performance.
    * Ideally, we will have servers in multiple locations to reduce latency and improve performance.
* Database
    * The default database is Azure Cloud. This will allow us to offload some work and improve performance.
    * Additionally, little data is being stored about each user. This will help keep the database small and fast.
* Code
    * How we write the backend will also affect performance.
    * We will need to write efficient code optimized for performance.
    * We won't be using recursion to avoid stack overflow errors.
    * We will make sure not to use nested loops to avoid performance issues.
    * Luckily, this type of application is not very performance intensive. We are not doing any heavy calculations or processing large amounts of data.
* Testing
    * Our tests will help us identify performance issues. If testing a feature is slow, we will need to optimize it.
    * We will use tools like Django Debug Toolbar to help identify performance issues.
* Security
    * Security is important, but sometimes it comes at a cost to performance.
    * We will need to balance security with performance.




## Django Project Structure

*See [previous team's Django Project Structure](./low_level_docs.md#django-project-structure) for the app layout; we follow the same structure.

This is what our project structure will look like:

* _server/
    * _server/ - Main project settings.
        * settings.py - Main settings file.
        * urls.py - Main url file.
        * wsgi.py - Web server gateway interface.
    * api/ - App for the api.
        * admin.py - Admin configuration.
        * apps.py - App configuration.
        * geodata/ - Used by GeoLite to look up location by IP (NOT THIS)
        * migrations/ - Migrations for the api app.
        * models.py - Define the models.
        * serializers.py - Define the serializers.
        * tests.py - Write unit tests.
        * urls.py - Map the urls to the views.
        * views.py - Define and implement the views.
    * core/
        * admin.py - Admin configuration.
        * apps.py - App configuration.
        * middleware.py - Captures requests for static files and redirects to Vue server
        * static/ - Contains some images
        * templates/ - Contains the base template
    * manage.py - Command line utility for managing the project.
    * Azure cloud (Database)


## Django Admin

*See [previous team's Django Admin](./low_level_docs.md#django-admin) for admin usage in non-production and initial Manager account setup.

The Django admin site adds the possibility to have admin accounts with levels of management and control. The main functions this account can provide are the following:

    * Easy creation, management, and deletion of user accounts
    * Easy creation, management, and deletion of data
    * Easy adjustment to permissions on user accounts
    * Ability to export data (if needed)
    * Logging and history of changes made to data
There are some concerns with the admin site and admin accounts:

    * Security concerns
        * Admin accounts are a prime target for hackers
        * Admin accounts could be used to access sensitive data
        * Admin accounts could be used to modify data in a way that could be harmful
        * Admin accounts could be used to delete data
        * Admin accounts could be used improperly or maliciously
    * Resource usage
        * Admin accounts take a lot of resources to maintain
        * Admin accounts could be used to do intensive work that could slow down the software
The Django admin site will be used to create the initial Manager accounts to manage the site.

While the admin site is a powerful tool, it is not the best tool for day-to-day operations. While the server is in production, the admin site will be disabled. Instead, the API will be used to manage the data.

## Unit Tests

*See [previous team's Unit Tests](./low_level_docs.md#unit-tests) for test coverage strategy; our additions remain aligned.

Each view will have a corresponding unit test. The unit tests will be used to verify that the views are functioning as expected.

* Good input will be used to verify that the views are functioning as expected
* Bad input will be used to verify that the views are functioning as expected
* Edge cases will be used to verify that the views are functioning as expected
The following tools will be used to create unit tests for the software:

* Django test framework will be used to create unit tests for the software.
    * See [Django Testing Documentation](https://docs.djangoproject.com/en/3.2/topics/testing/)
* Django debug toolbar will be used to monitor the performance of the software and to identify any potential issues.
    * See [Django Debug Toolbar Documentation](https://django-debug-toolbar.readthedocs.io/en/latest/)

## URL Mapping

*See [previous team's URL Mapping](./low_level_docs.md#url-mapping) for endpoint definitions and auth requirements; we preserve the same contract and add role checks.

### Static endpoints

*See [previous team's Static Endpoints design](./low_level_docs.md#static-endpoints)*

The static endpoints do not require user data.

| URL      | Method    | View Function | Notes                                                                                          |
|----------|-----------|---------------|------------------------------------------------------------------------------------------------|
| / | GET | home | The home page |
| /login/ | GET, POST | login | The login page, post the form |
| /signup/ | GET, POST | signup | The signup page, post the form |
| /app/ | GET | NA | This can only be called after a user is authenticated. The Vue Router will take over from here.
| /get_*/ | GET | get_* | This will get icon images for the front end

More pages will be covered by the [Vue Router] (#vue-router)

### Dynamic Endpoints

*See [previous team's Dynamic Endpoints design](./low_level_docs.md#dynamic-endpoints)*

The dynamic endpoints need user data. Authenication will be required to access all of these endpoints.

| URL      | Method    | View Function | Notes                                                                                          |
|----------|-----------|---------------|------------------------------------------------------------------------------------------------|
| /api/user/create | POST | create_user | Creates a user and makes them a cupid or dater as necessary |
| /api/user/<int:id> | GET | get_user | Gets the user's data based on their id number |
| /api/chat/ | POST | send_chat_message | Sends the chat message and returns the AI's response |
| /api/chat/<int:id>/ GET | get_five_messages | Returns the user's five most recent chat messages
| /api/dater/calendar/<int:id>/ | GET, POST | calendar | GET gathers the dater's calendar data, POST creates a new event/date |
| /api/dater/rate/ | POST | rate_dater | Dater rating cupids |
|api/dater/ratings/<int:id>/ | GET | get_dater_ratings | Gets a list of the dater's ratings |
| /api/dater/ratings/<int:id>/ | GET | get_dater_avg_rating | Gets a dater's average rating | 
| /api/dater/money_transfer/ | POST | dater_transfer | Dater can tranfer their money in exchange for cupid cash via an api |
| /api/dater/balance/<int:id>/ | GET | get_dater_balance | Gets the dater's cupid cash balance
| /api/dater/profile/<int:id>/ | GET | get_dater_profile | Get dater's profile
| /api/dater/profile/ | POST | set_dater_profile | Saves/updates the dater's profile |
| /api/dater/gigs/<int:id> | GET | get_dater_gigs | Gets all the gigs that the user has requested |
| /api/dater/planner/ | GET | planner | Gets the page for the plan-a-date |
| /api/cupid/rate/ | POST | rate_cupid | Cupid rating daters |
|api/cupid/ratings/<int:id>/ | GET | get_cupid_ratings | Gets a list of the cupid's ratings |
| /api/cupid/ratings/<int:id>/ | GET | get_cupid_avg_rating | Gets a cupid's average rating | 
| /api/cupid/money_transfer/ | POST | cupid_transfer | Cupids can transfer their earnings out of the app via an api |
| /api/cupid/balance/<int:id>/ | GET | get_cupid_balance | Gets the cupids's income balance
| /api/cupid/profile/<int:id>/ | GET | get_cupid_profile | Get cupid's profile
| /api/cupid/profile/ | POST | set_cupid_profile | Saves/updates the cupid's profile |
| /api/cupid/accepting/ | POST | cupid_accepting | Updates whether the cupid is currently accepting gigs |
| /api/gig/create/ | POST | create_gig | Creates a gig |
| /api/gig/accept/ | POST | accept_gig | Sets the gig as accepted |
| /api/gig/complete/ | POST | complete_gig | Sets the gig as completed |
| /api/gig/drop/ | POST | drop_gig | Sets the gig as dropped by the cupid |
| /api/gig/delete/ | POST | delete_gig | Gig is deleted by the dater |
| /api/gig/<int:dist> | GET | get_gigs | Returns a list of gigs within the cupid's preferred distance |
| /api/geo/stores/<int:id>/ | GET | get_stores | Gets a list of nearby stores |
| /api/geo/activities/<int:id>/ | Get | get_activities | Gets a list of nearby activities |
| /api/geo/events/<int:id>/ | Get | get_events | Gets a list of nearby events |
| /api/geo/attractions/<int:id>/ | Get | get_attractions | Gets a list of nearby attractions |
| /api/geo/user/<int:id>/ | GET | get_user_location | Get the user's current location |
| /api/manager/daters/ | GET | get_daters | Gets a list of daters |
| /api/manager/cupids/ | GET | get_cupids | Gets a list of cupids |
| /api/manager/dater_count/ | GET | get_dater_count | Gets a total count of dater accounts |
| /api/manager/cupid_count/ | GET | get_cupid_count | Gets a total count of cupid accounts |
| /api/manager/active_daters/ | GET | get_active_daters | Gets a count of daters currently using the app |
| /api/manager/active_cupids/ | GET | get_active_cupids | Gets a count of cupids currently using the app |
| /api/manager/gig_rate | GET | get_gig_rate | Returns the number of gigs created per day |
| /api/manager/gig_count | GET | get_gig_count | Returns the number of gigs currently active |
| /api/manager/gig_drop_rate | GET | get_gig_drop_rate | Returns the number of gigs dropped per day |
| /api/manager/gig_complete_rate | GET | get_gig_complete_rate | Returns the number of gigs completed per day |
| /api/manager/suspend/ | POST | suspend | Sets user as suspended |
| /api/manager/unsuspend | POST | unsuspend | sets user as unsuspended |
| /api/manager/delete_user/<string:usertype>/<int:id> | POST | delete_user | Deletes the user whose id number is used |
| /api/stt/ | POST | speech_to_text | Takes in audio and returns the words as text |
| /api/notify/ | POST | notify | Send a notification |

## Django Settings

*See [previous team's Django Settings](./low_level_docs.md#django-settings) for environment-driven configuration, static files, and production flags.

The file server/settings.py applies project settings. Use environment variables for secrets and set DEBUG to False in production.

## Backend Pseudocode

*See [previous team's Backend Pseudocode](./low_level_docs.md#backend-pseudocode) and DRF guides for view/serializer patterns and permission classes.

Use Django REST Framework’s function-based or class-based views and serializers for request handling. Map URLs with django.urls.path and enforce permissions per role (Dater, Cupid, Manager). See the previous team’s files and DRF guides for concrete patterns.

## Django Models

*See [previous team's Django Models](./low_level_docs.md#django-models) for field structures; our role extension of AbstractUser is consistent with their approach.

We will use the Django built-in User model, but add roles to it by extending `AbstractUser`. This comes with authentication functionality and the following fields. Details available in 
[Django docs](https://docs.djangoproject.com/en/5.0/ref/contrib/auth/#django.contrib.auth.models.User).

* User
  * **id**
  * *role added by us {Dater, Cupid, Manager}*
  * *phone_number added by us*
  * username
  * first_name
  * last_name
  * email
  * password
  * groups
  * user_permissions
  * is_staff
  * is_active
  * is_superuser
  * last_login
  * date_joined

Each model will correspond to a table. Bold denotes a primary key. For most tables,
this is the default id provided by Django. For certain one-to-one tables they will use that
relationship as their primary key. 

* Dater
    * **User : OneToOne Field (As provided by Django)**
    * Budget : Decimal Field
    * Communication preferences : IntegerChoices(EMAIL,TEXT)
    * Profile Picture : Image Field 
    * Text available to AI
        * Description of self : Text Field
        * Dating strengths : Text Field
        * Dating weaknesses : Text Field
        * Interests : Text Field
        * Past dating experiences : Text Field
        * Type of nerd : Text Field
        * Relationship goals : Text Field
        * Degree of AI assistance : Integer Field
    * Common with Cupid
        * Cupid Cash Balance : Decimal Field
        * Location : Text Field (Containing geo coordinates) 
        * Average Rating : Decimal Field
        * Suspended : Boolean Field
* Cupid
    * **User : OneToOne Field (As provided by Django)**
    * Accepting Gigs : Boolean Field (Is cupid accepting gigs)
    * Total gigs completed : Integer Field
    * Total gigs failed : Integer Field
    * Status : Text Choices (OFFLINE, GIGGING, AVAILABLE)
    * Gig Range : Integer Field
    * Common with Dater
        * Cupid Cash Balance : Decimal Field
        * Location : Text Field (Containing geo coordinates) 
        * Average Rating : Decimal Field
        * Suspended : Boolean Field
* Manager doesn't need anything more than a Django User in the manager role
* Message
    * **id : Auto Field**
    * Owner : Foreign Key (User)
    * Text : Text Field
    * fromAI : Boolean Field (Indicates which side of the convo this message belongs to)
* Gig
    * **id : Auto Field**
    * Dater : Foreign Key
    * Cupid : Foreign Key
    * Quest : OneToOne Field
    * Status : Text Choices (UNCLAIMED, CLAIMED, COMPLETE)
    * DateTime of request : DateTime Field
    * DateTime of claim : DateTime Field
    * DateTime of completion : DateTime Field
    * Dropped Count : Integer Field
    * Accepted Count : Integer Field
* Quest (separate for modularity)
    * **Gig : *Established by OneToOne Field on Gig***
    * Budget : Decimal Field
    * Items Requested : Text Field 
    * Pickup location : Text Field (address or geolocation to get object from)
* Date
    * **id : Auto Field**
    * Dater : Foreign Key
    * Date & Time : DateTime Field
    * Location : Text Field (Containing geo coordinates) 
    * Description : Text Field
    * Status : Text Choices (PLANNED, OCCURRING, PAST, CANCELED)
    * Budget : Decimal Field
* Feedback
    * **id : Auto Field**
    * Owner : Foreign Key (User)
    * Target : Foreign Key (User)
    * Gig : Foreign Key
    * Message : Text Field
    * Star Rating : Integer Field (bound to 1-5)
    * DateTime : DateTime Field 
* Payment Card
    * **User : Foreign Key**
    * Name On Card : Text Field
    * Card Number : Text Field
    * CVV : Text Field
    * Expiration : Text Field
* Bank Account
    * **User : Foreign Key**
    * Routing Number : Text Field
    * Account Number : Text Field

## Django Migrations

*See [previous team's Migrations](./low_level_docs.md#django-migrations) for seed data and test fixtures guidance reused here.

* Test Daters
  * username:dater1, email:bob@cupidcode.com, password:password, 200 cupid coin balance, budget of 50
  * username:dater2, email:Manny@cupidcode.com, password:password, 20 cupid coin balance, budget of 50
* Test Cupids
  * username:cupid1, email:joe@mail.com, password:password, 54 completed gigs, 12 failed
  * username:cupid2, email:really@me.com, password:password, 4 completed gigs, 16 failed
* Test Manager
  * username:manager, email:manager@cupidcode.com, password:password
* Test messages
  * Create a few test conversation for each dater.
* Test Gigs
  * Unclaimed gig with a unique quest
  * Unclaimed gig with a unique quest
  * Claimed gig
* Test Dates
  * A test location, date is june 17th, so it will never come during this semester.
* Feedback
  * A couple positive reviews for each cupid
  * A couple negative reviews for each cupid
  * A couple positive reviews for each dater
  * A couple negative reviews for each dater

## External API's

*See [previous team's External APIs](./low_level_docs.md#external-apis) for integration notes; we update AI and payments to Groq and Stripe respectively.

We will be using the following external APIs:

* [GeoLite2](https://www.maxmind.com/en/geoip2-databases)
  * Used to look up location by IP address.
  * Free to use.
  * Provides accurate location data.
  * Easy to integrate with Django.
* [OpenAI](https://openai.com/api/)
  * Used to generate responses for the chatbot.
  * Used for agentic AI features.
  * Free to use.
  * Provides high-quality responses.
  * Easy to integrate with Django.
* [yelpapi](https://www.yelp.com/developers)
  * Used to look up local businesses.
  * Free to use.
  * Provides accurate business data.
  * Easy to integrate with Django.
* [twilio](https://www.twilio.com/docs/usage/api)
  * Used to send SMS messages.
  * Paid service.
  * Provides reliable SMS delivery.
  * Easy to integrate with Django.

---
Final Note:
* We ended up using `Groq` api four our AI instead of `OpenAI`.
* We did not use `yelpapi` due to time constraints. The API keys and env data are there and some views were built but we not end up using or continueing development on these.
* We did not use `twilio` due to time constraints. The API keys and env data are there and some views were built but we did not end up finishing what was there however.
* We also used the external `stripe` api for payment handling, we forgot to add this into our documentation

---

## Quick Tutorial on how to use the Django Rest Framework

*See [previous team's DRF tutorial](./low_level_docs.md#quick-tutorial-on-how-to-use-the-django-rest-framework) and official docs for setup and usage.

Refer to the official DRF tutorials and API guide for setup, serializers, views, and routing:
- https://www.django-rest-framework.org/tutorial/quickstart/
- https://www.django-rest-framework.org/api-guide/
