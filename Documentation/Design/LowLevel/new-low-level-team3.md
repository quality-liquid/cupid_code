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
### Table of Contents
0. [Team Conventions](#0-team-conventions)
0. [Frontend Design](#1-frontend-design)
    - [Security](#security)
    - [Performance](#performance)
    - [UI](#ui)
      - [User flow:](#user-flow)
      - [Screen designs:](#screen-designs)                                                         
      - [Navigation Structure:](#navigation-structure)
      - [Layout guidelines:](#layout-guidelines)
      - [Color Palette:](#color-palette)
      - [Icon Use:](#icon-use)
      - [Responsive design:](#responsive-design)
      - [Making accounts and logging in](#making-accounts-and-logging-in)
      - [Dater](#dater)
      - [Cupid](#cupid)
      - [Manager](#manager)
    - [UX](#ux)
    - [Templates](#templates)
    - [Vue Router](#vue-router)
      - [How the Router works](#how-the-router-works)
    - [Testing](#testing)
0. [Middleend Design](#2-middleend-design)
0. [Backend Design](#3-backend-design)  

# 0. Team Conventions
[*Table of Contents*](#table-of-contents)

The Sinister-six will be following all of the same conventions outlined by the previous team, see [previous team's conventions](./low_level_docs.md#team-conventions-and-standards), except for the following changes outlined below.

## Branching
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
  * Development of features and experimentation of ideas which will merge into *development* once they are functioning.

## Coding Standards
We will follow all of the same coding standards, see [previous code standards](./low_level_docs.md#coding-standards), except for the following:
* New lines of code will be limited to 100 columns or less rather than the previous limit of 200 to increase code readability.
* Attention will be made to import only the methods, attributes, objects, etc...which we actually use from a package rather than blanket imports of entire packages. I.e. use `from _ import _, _, ...` rather than `import _`.


# 1. Frontend Design
[*Table of Contents*](#table-of-contents)

#### Subsections
- [Frontend Design](#frontend-design)
- [Security](#security)
- [UI](#ui)
- [UX](#ux)
- [Templates](#templates)
- [Vue Router](#vue-router)
  - [Implementation](#implementing-the-router)
- [Testing](#testing)

## Security
The previous team had done a good job in maintaining security within the app. They did not implement a strong password system, which we will implement by... 

If a user loses their account information, a form of Two-Step Authentication will be provided to allow them to reset their password and enter their account. Managers will also require Two-Step Authentication every time they log in. We will do this by...

We also intend to make calls to external APIs and thus we need to ensure that we safeguard any response that could be malicious. We will do this by...

## Performance
The frontend will verify any inputs that it can before making requests to the backend to lower the amount of requests made to the backend. For example, the frontend will check that an entered email is valid before making a request. Since the page is a single page application, we are also able to reduce the number of requests to the backend.

By reducing how many requests we make to the server, the user is able to interact with the app more without having to wait for constant responses from the server.

## UI
The application as handed to us was well designed for intuitive clicking and use for the features it had. We intend to make more features immediately accessible on the landing page and make some changes to the color scheme. There will be a dark scheme and a light theme to make it more accessible. Clear instructions will continue to be provided as needed

### User Flow:
The user flow as handed to us in the application was well designed. There will be slight changes to the home page relative to new features pertinent to the type of user. Daters will be able to see upcoming dates and their Cupid Cash balance. They will also be able to, from the home page, access their date calendar, an AI chatbot for advice and plans, the new Plan-a-Date feature, their Cupid Cash wallet and history, all their Gig requests, their profile page, a feedback page, and the ability to allow the AI to start listening and provide live feedback. Cupids will be able to clock in and out and see how many available gigs there are, how many gigs they've completed, and how much they've earned. Cupids will have home page access to the list of nearby gigs and how many are active, their active gig(s) and status(es), their profile page, and a feedback page. A recent activity list and a weekly earnings report will also be on the page. Platform admin managers will be able to see metrics on how many total and active daters, total and active cupids, total and monthly revenue, and critical issues including those that are pending. A general platform health dashboard with key performance indicators will also be displayed with recent platform activity. Access to a report system, the feedback reviews, user management, financial reports, analytics, and cupid schedule reports will also be available with a status page. Each of these buttons are tap sensitive and dynamically redirect the specific user to the destination indicated.

### Screen Designs:
Creating a dark theme while also maintaining the contrast present as handed to us across the application is important. Important information will be made more easily accessible with no need to scroll or swipe, the most important being locked at the top of the screen in the case of a scroll. Our main customer is a mobile user, so all screen designs will be designed as "mobile-first" architecture.

### Navigation Structure:
The existing design for the navigation structure will be kept in place.  
See [Previous Teams Navigation Structure](./low_level_docs.md#navigation-structure)

### Layout Guidelines:
The existing design for the layout guidelines will be kept in place.  
See [Previous Teams Layout Guidelines](./low_level_docs.md#layout-guidelines)

### Color Palette:
This represents the primary set of colors that will be used across the application in both its light and dark themes.
- **Black**: `#0A0908`
- **Salmon Pink**: `#E5989B`
- **Old Rose**: `#B5838D`
- **Gunmetal**: `#22333B`
- **Walnut Brown**: `#5E503F`
- **White**: `#FFFFFF`

### Icon Use:
The existing design for the use of icons will be kept in place.  
See [Previous Teams Icon Use](./low_level_docs.md#icon-use)

### Responsive Design:
The app's portrait orientation and general "mobile-first" design principles will be maintained as the app will primarily be used in mobile settings. Desktop functionality and scalability will be maintained.

### Making accounts and Logging in
The existing design for making accounts and logging in will be maintained.  
See [previous teams accounts section](./low_level_docs.md#making-accounts-and-logging-in)

The pages will be updated to reflect the updated visual interface. A new logo will also be integrated.

![create_account_image](images/createacc.png "Create_Acc")
![login_image](images/login.png "Login")
![logo](images/logo.png "Logo")

### Dater
The Daters will be able to access the 8 following features from their home pages:
- Date calendar from which to schedule and manage their dates.
- AI Chat for chatting and advice.
- Plan A Date for having AI-powered date planning and itineraries.
- Cupid Cash dashboard for getting credits and viewing their history.
- Gig Request dashboard to request Cupid assistance and see the status of their requests.
- Profile to view and edit their information.
- App Feedback to submit reviews and report app issues.
- AI Listening to get real-time date support.

![dater_home](images/uh.png "User_Home")
![dater_ai](images/aichat.png "Ai_Chat")
![dater_calendar](images/calendar.png "Calendar")
![dater_planner](images/planner.png "PlanADate")
![dater_cupid_cash](images/cupidcash.png "Cupid_Cash")
![dater_add_cash](images/addfunds.png "Add_Cupid_Cash")
![dater_profile](images/useracc.png "User_Acc")
![dater_listening](images/listen1.png "Listen")

### Cupid
The Cupids will be able to access the following 5 features from their home pages:
- Clock-in and Clock-out mechanism to make themselves available to receive gig notifications.
- Nearby and active Cupid gigs.
- Gigs currently active and their status.
- Profile to view gig history, manage finances, and edit information.
- App Feedback to submit reviews and report app issues.

![cupid_home](images/ch.png "Cupid_Home")
![cash_earned](images/ch_cash.png "Cash_Earned")
![gig1](images/ch_gig1.png "Gig_1")
![gig2](images/ch_gig2.png "Gig_2")

### Manager
The Manager users who act as administrators for the platform will be able to access the following features:
- Analytics Report System
- Inter-user Feedback
- User Management
- Financial Reports
- Cupid Schedule Reports
- System Status

![manager_home](images/manager_home.png "Manager_Home")
![user_management](images/manage.png "User_Management")

## UX
The existing design for the user experience will be maintained, striving to ensure that they enjoy the app and find a helpful tool to shoulder their dating burdens.  
See [previous teams UX section](./low_level_docs.md#ux)

## Templates

A Django Template is used to connect the Vue frontend to the backend. A second Django Template is used to make the sign-up/login process its own separate app to improve security. The sign-up/login process is only responsible for adding/validating users and then redirecting them to the appropriate homepage depending on what type of user they are.

Django templates take the following form:

``` html
{% load static %}
<head>
  <style>
    /* Write inline styles here */
  </style>  
</head>
<body>
  <div>
    Welcome to Cupid Code landing page here
  </div>
  <button> Login </button>
  <button> Sign up </button>
</body>  
```

## Vue Router

The previous team used Vue Router to switch between pages in the frontend. They used hash routing to control which page the user is on which allows the frontend to switch pages without contacting the server every time. We will continue to use this routing method and take care to keep track of the state of the application to keep the frontend light and responsive.

The following is an example of how Vue Router is used in the application:
```javascript
import create web history, web hash history from 'vue-router';

import Home from './components/Home.vue';
import About from './components/Dater.vue';
import Contact from './components/Cupid.vue';

const routes = [
  { path: '/', name: 'Home', component: Home },
  { path: '/dater/:id', name: 'Dater', component: Dater },
  { path: '/cupid', name: 'Cupid', component: Cupid }
];

const router = create_web_history({
  history: web hash history,
  routes
});

export default router;
```
The ':' in "path: '/dater/:id'" symbolizes a parameter to be passed through the path. This was used to pass the user id when making calls to the backend. We are unsure as to why the previous team passed the id in way as it is possible to accomplish this using state variables. As we work on the routing, if we discover that passing the id through the state instead of the url is more efficient, then we will make the necessary changes.

### Implementing the router

In the **main.js** file we include the router and mount it. Other pages can import the router to use programmatic routing or use the router-link tag in components:

``` javascript
import router from './router/router.js'

router.go(1) // Forward 1
router.forward() // ^
router.go(-1) // Back 1
router.back() // ^

// Route the user to this path with the given params.
router.push({name: "Path Name", params: {param: given param}})
```

```html
  <nav>
    <router-link :to="{name: 'Path name', params: {param: given param}}">
      Go here!
    </router-link>
    <router-link :to="{name: 'Path name', params: {param: given param}}">
      Or here!
    </router-link>
  </nav>
  <div>
    Other components from the page get displayed here.
  </div>  
<template>
```

## Vue URLs
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

## Testing
We intend to continue using and building upon the existing testing framework going forward in the development of the product. Testing is done in the following ways:

0. **Unit Testing**: Unit tests isolate functions and methods and verify that it outputs the way it is intended. Focus on testing edge cases and potential invalid inputs.

0. **Component Testing**: Vue Test Utils is used to test Vue components and simulate user interactions.

0. **Integration Testing**: Integration tests will verify that multiple components work together and ensure the entire application can work.

0. **Mocking**: Mocking is a technique used in testing to isolate a component that may rely on other components. By using mocking you can "mock" what a function should return and thereby control the behavior of external dependencies to focus entirely on the component under test.

The tests will be run in a CICD pipeline to ensure that changes to the app do not break working functionality. If a change to the code alters what a function inputs and outputs, the developer who made the change is in charge of fixing the corresponding test and ensuring that it works.

# 2. Middleend Design
[*Table of Contents*](#table-of-contents)
* This section for design how to connect the frontend and backend

# 3. Backend Design
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

## Backend Summary (Revisit this after everything else is done)
    The backend will be built using Django and the Django REST Framework. As a result much of the needed security is already implemented. A majority of the work will be in the models, views, and serializers. The models will be the database, the views will be the API, and the serializers will be the conversion of the models to JSON and vice versa. The frontend will communicate with the backend using HTTP GET and POST requests. The backend will respond with JSON data. This will be made easy by the Django Rest Framework. Mapping what endpoints the frontend needs is helpful for the backend to know what to build. This will be done in the URL Mapping section.
        Additionally, the data will be stored in Azure Cloud to make it more scalable, accessible, and secure.
        One more thing to note is that the Agentic AI will have access to communicate with both the back end and the front end. It will be expected to pull data from the database, and then transport it and use it automatically.

## Resources for the Backend 
We added additional links to the Azure Cloud Documentation, LM studio documentation and the LangChain Documentation.

[Django Rest Framework Quickstart](https://www.django-rest-framework.org/tutorial/quickstart/)   
[Django Rest Framework API Reference](https://docs.djangoproject.com/en/5.0/ref/)  
[Django Rest Framework Serializers](https://www.django-rest-framework.org/api-guide/serializers/)  
[Django Rest Framework Views](https://www.django-rest-framework.org/api-guide/views/)  
[Django Rest Framework Permissions](https://www.django-rest-framework.org/api-guide/permissions/)  
[Django Rest Framework Authentication](https://www.django-rest-framework.org/api-guide/authentication/)  
[Azure Cloud Documentation](https://learn.microsoft.com/en-us/azure/?product=popular)  
[LM Studio Documentation](https://lmstudio.ai/docs/app)  
[LangChain Agentic AI documentation](https://python.langchain.com/docs/tutorials/agents/)


## Performance
The following will determine the performance of the backend:
### Largest Changes from the Previous Team
The majority of the changes in this section have to do with updating the document to show that we are using Azure Cloud instead of SQL lite and that we are going to be using an agentic AI instead of a regular AI model.


- Django
    - Provides a lot of performance optimizations out of the box.
    - Mature framework that has been optimized for performance over many years.
    - Used by many large websites and can handle a lot of traffic.
    - Synchronous framework, which means it can handle a lot of requests at once.
    - Built-in caching system that can help improve performance.
    - Built-in ORM that can help optimize database queries.
    - Built-in middleware system that can help optimize requests.
- Django Rest Framework
    - Built on top of Django and inherits many of its performance optimizations.
    - Designed to be fast and efficient.
    - Used by many large websites and can handle a lot of traffic.
    - Built-in caching and throttling systems that can help improve performance.
    - Built-in serializers that can help optimize data serialization.
    - Built-in viewsets and routers that can help optimize request handling.
- Hardware
    - We plan to run the backend on the cloud. This will allow us to have a more accessible dataset and also more resources on our personal hardware.
    - We will need to monitor the hardware to ensure that it is running optimally and make any necessary changes to improve performance.
    - We will be running our AI agent locally from LM Studio and using frameworks such as LangChain. This will allow us more control over the AI, but we will need to be cognizant of how this might affect performance and how we will scale this as the product grows toward deployment.
- Network
    - The internet service provider will need to be able to handle the traffic that we are generating.
    - We will need to monitor the network to ensure that it is running optimally and make any necessary changes to improve performance.
    - Ideally, we will have servers in multiple locations to reduce latency and improve performance.
- Database
    - The default database is Azure Cloud. This will allow us to offload some work and improve performance.
    - Additionally, little data is being stored about each user. This will help keep the database small and fast.
- Code
    - How we write the backend will also affect performance.
    - We will need to write efficient code optimized for performance.
    - We won't be using recursion to avoid stack overflow errors.
    - We will make sure not to use nested loops to avoid performance issues.
    - Luckily, this type of application is not very performance intensive. We are not doing any heavy calculations or processing large amounts of data.
- Testing
    - Our tests will help us identify performance issues. If testing a feature is slow, we will need to optimize it.
    - We will use tools like Django Debug Toolbar to help identify performance issues.
- Security
    - Security is important, but sometimes it comes at a cost to performance.
    - We will need to balance security with performance.




## Django Project Structure
This is what our project structure will look like:

- _server/
    - _server/ - Main project settings.
        - settings.py - Main settings file.
        - urls.py - Main url file.
        - wsgi.py - Web server gateway interface.
    - api/ - App for the api.
        - admin.py - Admin configuration.
        - apps.py - App configuration.
        - geodata/ - Used by GeoLite to look up location by IP (NOT THIS)
        - migrations/ - Migrations for the api app.
        - models.py - Define the models.
        - serializers.py - Define the serializers.
        - tests.py - Write unit tests.
        - urls.py - Map the urls to the views.
        - views.py - Define and implement the views.
    - core/
        - admin.py - Admin configuration.
        - apps.py - App configuration.
        - middleware.py - Captures requests for static files and redirects to Vue server
        - static/ - Contains some images
        - templates/ - Contains the base template
    - manage.py - Command line utility for managing the project.
    - Azure cloud (Database)


## Django Admin
The Django admin site adds the possibility to have admin accounts with levels of management and control. The main functions this account can provide are the following:

    - Easy creation, management, and deletion of user accounts
    - Easy creation, management, and deletion of data
    - Easy adjustment to permissions on user accounts
    - Ability to export data (if needed)
    - Logging and history of changes made to data
There are some concerns with the admin site and admin accounts:

    - Security concerns
        - Admin accounts are a prime target for hackers
        - Admin accounts could be used to access sensitive data
        - Admin accounts could be used to modify data in a way that could be harmful
        - Admin accounts could be used to delete data
        - Admin accounts could be used improperly or maliciously
    - Resource usage
        - Admin accounts take a lot of resources to maintain
        - Admin accounts could be used to do intensive work that could slow down the software
The Django admin site will be used to create the initial Manager accounts to manage the site.

While the admin site is a powerful tool, it is not the best tool for day-to-day operations. While the server is in production, the admin site will be disabled. Instead, the API will be used to manage the data.

## Unit Tests
Each view will have a corresponding unit test. The unit tests will be used to verify that the views are functioning as expected.

- Good input will be used to verify that the views are functioning as expected
- Bad input will be used to verify that the views are functioning as expected
- Edge cases will be used to verify that the views are functioning as expected
The following tools will be used to create unit tests for the software:

- Django test framework will be used to create unit tests for the software.
    - See [Django Testing Documentation](https://docs.djangoproject.com/en/3.2/topics/testing/)
- Django debug toolbar will be used to monitor the performance of the software and to identify any potential issues.
    - See [Django Debug Toolbar Documentation](https://django-debug-toolbar.readthedocs.io/en/latest/)

Pseudocode can be found at the bottom of the [Test pseudocode](#test-pseudocode) section.

### Test pseudocode  
api/test.api:

    from django.test import TestCase
    from unittest.mock import MagicMock

    class APITestCase(TestCase):

        def test_sign_in(self):
            mock_request = MagicMock()
            mock_request.method = "POST"
            mock_request.POST.get = MagicMock(return_value="{
                "status": "success",
                "message": "User has been signed in"
                "code": 200
            }")
            response = sign_in(mock_request)
            self.assertEqual(response.status_code, 200)
            
            mock_request.POST.get = MagicMock(return_value="{
                "status": "failure",
                "message": "Incorrect Password"
                "code": 400
            }")
            response = sign_in(mock_request)
            self.assertEqual(response.status_code, 400)
            
        def test_login(self):
            mock_request = MagicMock()
            mock_request.method = "POST"
            mock_request.POST.get = MagicMock(return_value="{
                "status": "success",
                "message": "User has been logged in"
                "code": 200
            }")
            response = login(mock_request)
            self.assertEqual(response.status_code, 200)
            
            mock_request.POST.get = MagicMock(return_value="{
                "status": "failure",
                "message": "Incorrect Password"
                "code": 400
            }")
            response = login(mock_request)
            self.assertEqual(response.status_code, 400)
            
        def test_create_user(self):
            mock_request = MagicMock()
            mock_request.method = "POST"
            mock_request.POST.get = MagicMock(return_value="{
                "status": "success",
                "message": "User has been created"
                "code": 200
            }")
            response = create_user(mock_request)
            self.assertEqual(response.status_code, 200)
            
            mock_request.POST.get = MagicMock(return_value="{
                "status": "failure",
                "message": "User has not been created"
                "code": 400
            }")
            response = create_user(mock_request)
            self.assertEqual(response.status_code, 400)
        
        # etc ...

## URL Mapping

### Static endpoints

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

The file `server/settings.py` will apply settings to the Django project. All of the current settings will be kept the same with the note that:

* `DEBUG` will be set to `False` for the version that is deployed.

## Backend Pseudocode

**cupid_code/urls.py**
``` python
path("", include("api.urls")),
path("api/", include("api.urls")),
path("admin/", admin.site.urls),
```

**api/urls.py**

``` python

from django.url import path
from . import views

urlpatterns = [
  path = ("/" , views.home, name="home"),
  path = ("/login/", views.login, name="login"),
  path = ("/signup/", views.signup, name="signup"),
  path = ("/app/", views.app, name="app"),
  path = ("/api/user/create", views.create_user, name="create_user"),
  path = ("/api/user/<int:id>", views.get_user, name="get_user"),
  path = ("/api/chat/", views.send_chat_message, name="send_chat_message"),
  path = ("/api/chat/<int:id>/", views.get_five_messages, name="get_five_messages"),
  path = ("/api/dater/calendar/<int:id>/", views.calendar, name="calendar"),
  path = ("/api/dater/rate/", views.rate_dater, name="rate_dater"),
  path = ("|api/dater/ratings/<int:id>/", views.get_dater_ratings, name="get_dater_ratings"),
  path = ("/api/dater/ratings/<int:id>/", views.get_dater_avg_rating, name="get_dater_avg_rating"),
  path = ("/api/dater/money_transfer/", views.dater_transfer, name="dater_transfer")
  path = ("/api/dater/balance/<int:id>/" views.get_dater_balance, name="get_dater_balance"),
  path = ("/api/dater/profile/<int:id>/", views.get_dater_profile, name="get_dater_profile"),
  path = ("/api/dater/profile/", views.set_dater_profile, name="set_dater_profile"),
  path = ("/api/dater/gigs/<int:id>", views.get_dater_gigs, name="get_dater_gigs"),
  path = ("/api/dater/planner", views.planner, name="planner"),
  path = ("/api/cupid/rate/", views.rate_cupid, name="rate_cupid"),
  path = ("api/cupid/ratings/<int:id>/", views.get_cupid_ratings, name="get_cupid_ratings"),
  path = ("/api/cupid/ratings/<int:id>/", views.get_cupid_avg_rating, name="get_cupid_avg_rating"),
  path = ("/api/cupid/money_transfer/", views.cupid_transfer, name="cupid_transfer"),
  path = ("/api/cupid/balance/<int:id>/", views.get_cupid_balance, name="get_cupid_balance"),
  path = ("/api/cupid/profile/<int:id>/", get_cupid_profile, name="get_cupid_profile"),
  path = ("/api/cupid/profile/", views.set_cupid_profile, name="set_cupid_profile"),
  path = ("/api/cupid/accepting/", views.cupid_accepting, name="cupid_accepting"),
  path = ("/api/gig/create/", views.create_gig, name="create_gig"),
  path = ("/api/gig/accept/", views.accept_gig, name="accept_gig"),
  path = ("/api/gig/complete/", views.complete_gig, name="complete_gig"),
  path = ("/api/gig/drop/", views.drop_gig, name="drop_gig"),
  path = ("/api/gig/delete/", views.delete_gig, name="delete_gig"),
  path = ("/api/gig/<int:dist>", views.get_gigs, name="get_gigs"),
  path = ("/api/geo/stores/<int:id>/", views.get_stores, name="get_stores"),
  path = ("/api/geo/activities/<int:id>/", views.get_activities, name="get_activities"),
  path = ("/api/geo/events/<int:id>/", views.get_events, name="get_events"),
  path = ("/api/geo/attractions/<int:id>/", views.get_attractions, name="get_attractions"),
  path = ("/api/geo/user/<int:id>/", views.get_user_location, name="get_user_location"),
  path = ("/api/manager/daters/", views.get_daters, name="get_daters"),
  path = ("/api/manager/cupids/", views.get_cupids, name="get_cupids"),
  path = ("/api/manager/dater_count/", views.get_dater_count, name="get_dater_count"),
  path = ("/api/manager/cupid_count/", views.get_cupid_count, name="get_cupid_count"),
  path = ("/api/manager/active_daters/", views.get_active_daters, name="get_active_daters"),
  path = ("/api/manager/active_cupids/", views.get_active_cupids, name="get_active_cupids"),
  path = ("/api/manager/gig_rate", views.get_gig_rate, name="get_gig_rate"),
  path = ("/api/manager/gig_count", views.get_gig_count, name="get_gig_count"),
  path = ("/api/manager/gig_drop_rate", views.get_gig_drop_rate, name="get_gig_drop_rate"),
  path = ("/api/manager/gig_complete_rate", views.get_gig_complete_rate, name="gig_complete_rate"),
  path = ("/api/manager/suspend/", views.suspend, name="suspend"),
  path = ("/api/manager/unsuspend", views.unsuspend, name="unsuspend"),
  path = ("/api/manager/delete_user/<string:usertype>/<int:id>", views.delete_user, name="delete_user"),
  path = ("/api/stt/", views.speech_to_text, name="speech_to_text"),
  path = ("/api/notify/", views.notify, name="notify"),
]

```

**api/views.py**
``` python

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Dater, Cupid, Message, Manager, Gig, Quest, Date, Feedback
from .serializers import DaterSerializer, CupidSerializer, MessageSerializer, ManagerSerializer, GigSerializer, QuestSerializer, DateSerializer, FeedbackSerializer, PaymentCardSerializer, BankAccountSerializer

def home(request):
    return render(request, "home.html")
    
def signup(request):
    if request.method == "POST":
        validate the form
        return redirect("/login/")
    else:
        return render(request, "signup.html")
        
def login(request):
    if request.method == "POST":
        username = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/app/")
        else:
            return render(request, "login.html", {"message": "Incorrect Password"})
    else:
        return render(request, "login.html")

def create_user(request):
  for each profile data for user:
    create a variable = request.{specific data}

  dater = Dater(
    model_column = request.POST[matching variable]
  )

  dater.save()
  
  return redirect("/app/")


def get_user(request, id):
  user = {flag that identifies who the user is (Dater/Cupid/Manager)}.objects.get(id=id)

  response = user.json()

  return response

def send_chat_message(request):
  forward_message = request.{name of message in body}
  save forward_message to DB as Message

  response = {method call to send to external AI chat API}
  save response to DB as Message

  return response.json()

def get_five_messages(request, id):
  dater = Dater.objects.get(id=id)

  list_of_messages = Message.objects.filter(owner=id)

  ordered_most_recent_messages = reorder list_of_messages from newest to oldest

  list_of_messages = first five of ordered_most_recent_messages

  response = list_of_messages.json()

  return response

def calendar(request, id):
    if request.method == "POST":
        dater = Dater.objects.get(id=id)
        date = Date(
            dater = dater,
            date_time = request.date_time,
            location = request.location,
            description = request.description,
            status = request.status,
            budget = request.budget,
        )
        date.save()
        return JsonResponse({'message': 'Date has been created'})
    else:
        dater = Dater.objects.get(id=id)
        calendar = Date.objects.filter(dater=id)
        response = calendar.json()
        return response

def rate_dater(request):
  dater_id = request.dater_id
  dater = Dater.get(id=dater_id)
  rating = request.POST["rating"]

  feedback = Feedback(
    user = rating.user,
    intervention_request = rating.intervention_request, 
    message = rating.message,
    star_rating = request.star_rating,
    datetime = rating.datetime, 
  )

  feedback.save()

  new_rating = avg_rating(rating, dater_id)
  dater.avg_rating = new_rating

  dater.save()

  return JsonResponse({'message': 'Rating has been submitted'})

def get_dater_ratings(request, id):
  dater = Dater.objects.get(id=id)

  ratings = Feedback.objects.get(user=id)
  
  response = ratings.json()

  return response

def get_dater_avg_rating(request, id):
  dater = Dater.objects.get(id=id)

  avg_rating = dater.avg_rating

  response = avg_rating.json()

  return response

def dater_transfer(request):
  dater_id = request.user_id
  money_api = request.api_info

  transfer_amount = request.transfer_amount
  
  result = way to transfer money from api(money_api, transfer_amount)

  dater.balance = dater.balance + result

  send result to money_api

  dater.save()

  return JsonResponse({'message': 'Payment successful'})

def get_dater_balance(request, id):
  dater = Dater.objects.get(id=id)

  response = dater.balance.json()

  return response

def get_dater_profile(request, id):
  dater = Dater.objects.get(id=id)

  response = dater.json()

  return response

def set_dater_profile(request):
  dater_id = request.user

  dater = Dater.objects.get(dater_id)

  for each dater profile property sent in request:
    dater.property = profile property sent    

  dater.save()

  return JsonResponse({'message': 'Profile saved'})

def get_dater_gigs(request, id):
  dater = Dater.objects.get(id=id)

  gigs = Gig.objects.get(user=id)

  response = gigs.json()

def planner(request):
  return("planner.html")

def rate_cupid(request):
  cupid_id = request.cupid_id
  cupid = Cupid.get(id=cupid_id)
  rating = request.POST["rating"]

  feedback = Feedback(
    user = rating.user,
    intervention_request = rating.intervention_request, 
    message = rating.message,
    star_rating = request.star_rating,
    datetime = rating.datetime, 
  )

  feedback.save()

  new_rating = avg_rating(rating, cupid_id)
  cupid.avg_rating = new_rating

  cupid.save()

  return JsonResponse({'message': 'Rating has been submitted'}) 
  
def get_cupid_ratings(request, id):
  cupid = Cupid.objects.get(id=id)

  ratings = Feedback.objects.get(user=id)
  
  response = ratings.json()

  return response

def get_cupid_avg_rating(request, id):
  cupid = Cupid.objects.get(id=id)

  avg_rating = cupid.avg_rating

  response = avg_rating.json()

  return response

def cupid_transfer(request):
  cupid_id = request.cupid_id
  money_api = request.api_info

  transfer_amount = request.transfer_amount
  
  send transfer_amount to money_api
  
  cupid.balance = dater.balance - transfer_amount

  cupid.save()

  return JsonResponse({'message': 'Deposit successful'})

def get_cupid_balance(request, id):
  cupid = Cupid.objects.get(id=id)

  response = cupid.balance.json()

  return response

def get_cupid_profile(request, id):
  cupid = Cupid.objects.get(id=id)

  response = cupid.json()

  return response

def set_cupid_profile(request):
  cupid_id = request.user

  cupid = Cupid.objects.get(cupid_id)

  for each cupid profile property sent in request:
    cupid.property = profile property sent    

  cupid.save()

  return JsonResponse({'message': 'Profile saved'})

def cupid_accepting(request):
    cupid_ip_address = request.META.get('REMOTE_ADDR')
    cupid_id = request.cupid_id
    cupid = Cupid.get(id=cupid_id)
    cupid.location = cupid_ip_address  

    cupid.accepting = True
    cupid.save()

    return JsonResponse({'message': 'Cupid is now active'})

def create_gig(request):
    
    dater_id = request.dater_id
    dater = Dater.get(id=dater_id)
    quest = request.quest
    
    gig = Gig(
        dater = dater,
        cupid = None,
        quest = quest,
        status = 0,
        date_time_of_request = request.date_time_of_request,
        date_time_of_claim = None,
        date_time_of_completion = None,
    )
    
    gig.save()
    
    return JsonResponse({'message': 'Gig has been created'})
  
def accept_gig(request):

    cupid_ip_address = request.META.get('REMOTE_ADDR')
    cupid_id = request.cupid_id
    cupid = Cupid.get(id=cupid_id)
    cupid.location = cupid_ip_address

    gig_id = request.gig_id
    gig = Gig.get(id=gig_id)
    cupid_id = request.cupid_id
    cupid = Cupid.get(id=cupid_id)
    
    gig.cupid = cupid
    gig.status = 1
    gig.date_time_of_claim = request.date_time_of_claim
    
    gig.save()
    
    return JsonResponse({'message': 'Gig has been accepted'})
    
def complete_gig(request):

    cupid_ip_address = request.META.get('REMOTE_ADDR')
    cupid_id = request.cupid_id
    cupid = Cupid.get(id=cupid_id)
    cupid.location = cupid_ip_address
    
    gig_id = request.gig_id
    gig = Gig.get(id=gig_id)
    
    gig.status = 2
    gig.date_time_of_completion = request.date_time_of_completion
    
    gig.save()
    
    return JsonResponse({'message': 'Gig has been completed'})
    
def drop_gig(request):

    cupid_ip_address = request.META.get('REMOTE_ADDR')
    cupid_id = request.cupid_id
    cupid = Cupid.get(id=cupid_id)
    cupid.location = cupid_ip_address
    
    gig_id = request.gig_id
    gig = Gig.get(id=gig_id)
    
    gig.status = 1
    gig.date_time_of_claim = None
    gig.cupid = None
    
    gig.save()
    
    return JsonResponse({'message': 'Gig has been dropped'})

def delete_gig(request):

    cupid_ip_address = request.META.get('REMOTE_ADDR')
    cupid_id = request.cupid_id
    cupid = Cupid.get(id=cupid_id)
    cupid.location = cupid_ip_address
    
    gig_id = request.gig_id
    gig = Gig.get(id=gig_id)
    
    gig.delete()
    
    return JsonResponse({'message': 'Gig has been deleted'})
    
def get_gigs(request, count):
    gigs = Gig.objects.all()[:count]
    
    response = gigs.json()
    
    return response
    
def get_stores(request):
    
    dater_ip_address = request.META.get('REMOTE_ADDR')
    dater_id = request.dater_id
    dater = Dater.get(id=dater_id)
    dater.location = dater_ip_address
    
    stores = method call to get stores
    
    response = stores.json()
    
    return response
    
def get_activities(request):
    
    dater_ip_address = request.META.get('REMOTE_ADDR')
    dater_id = request.dater_id
    dater = Dater.get(id=dater_id)
    dater.location = dater_ip_address

    activities = method call to get activities
    
    response = activities.json()
    
    return response
    
def get_events(request):
    
    dater_ip_address = request.META.get('REMOTE_ADDR')
    dater_id = request.dater_id
    dater = Dater.get(id=dater_id)
    dater.location = dater_ip_address
    
    events = method call to get events
    
    response = events.json()
    
    return response
    
def get_attractions(request):

    dater_ip_address = request.META.get('REMOTE_ADDR')
    dater_id = request.dater_id
    dater = Dater.get(id=dater_id)
    dater.location = dater_ip_address
    
    attractions = method call to get attractions
    
    response = attractions.json()
    
    return response
    
def get_user_location(request, id):
    user = User.objects.get(id=id)
    
    location = user.location
    
    response = location.json()
    
    return response
    
def get_cupids(request):
    cupids = Cupid.objects.all()
    
    response = cupids.json()
    
    return response
    
def get_daters(request):
    daters = Dater.objects.all()
    
    response = daters.json()
    
    return response
    
def get_dater_count(request):
    dater_count = Dater.objects.count()
    
    response = dater_count.json()
    
    return response
    
def get_cupid_count(request):
    cupid_count = Cupid.objects.count()
    
    response = cupid_count.json()
    
    return response
    
def get_active_cupids(request):
    active_cupids = Cupid.objects.filter(status=2)
    
    response = active_cupids.json()
    
    return response
    
def get_active_daters(request):
    active_daters = Dater.objects.filter(status=2)
    
    response = active_daters.json()
    
    return response
    
def get_gig_rate(request):
    dates = Gig.objects.filter(status=1).count()
    gig_rate = Gig.objects.filter(status=1).count()
    
    rate = gig_rate / dates
    
    response = rate.json()
    
    return response

def get_gig_count(request):
    gig_count = Gig.objects.count()
    
    response = gig_count.json()
    
    return response
    
def get_gig_drop_rate(request):
    dates = Gig.objects.filter(status=3).count()
    gig_drop_rate = Gig.objects.filter(status=3).count()
    
    rate = gig_drop_rate / dates
    
    response = rate.json()
    
    return response
    
def get_gig_complete_rate(request):
    dates = Gig.objects.filter(status=2).count()
    gig_complete_rate = Gig.objects.filter(status=2).count()
    
    rate = gig_complete_rate / dates
    
    response = rate.json()
    
    return response
    
def suspend(request):
    user_id = request.user_id
    user = User.get(id=user_id)
    user.suspended = True
    
def unsuspend(request):
    user_id = request.user_id
    user = User.get(id=user_id)
    user.suspended = False

def delete_user(request, usertype, id):
  if usertype == "dater":
    user = Dater.objects.get(id=id)
  else if usertype == "cupid":
    user = Cupid.objects.get(id=id)
  else:
    return JsonResponse({'message': 'Invalid usertype'})
  
  user.delete()
  return JsonResponse({'message': 'The {usertype} has been deleted'})
    
def speech_to_text(request):

    dater_ip_address = request.META.get('REMOTE_ADDR')
    dater_id = request.dater_id
    dater = Dater.get(id=dater_id)
    dater.location = dater_ip_address
    
    file = request.file
    text = api call to convert speech to text
    
    message = Message(
        owner = dater,
        text = text,
        from_ai = False,
    )
    
    ai_response = api call to convert text to speech
    ai_message = Message(
        owner = dater,
        text = ai_response,
        from_ai = True,
    )
    
    message.save()
    ai_message.save()
    
    return ai_message.json()
    
def notify(request):
    user_id = request.user_id
    user = User.get(id=user_id)
    message = request.message
    
        message = Message(
        owner = user,
        text = message,
        from_ai = True,
    )
    
    communication_preference = user.communication_preference
    
    if communication_preference == 1:
        send message to user's phone
    elif communication_preference == 2:
        send message to user's email
    elif communication_preference == 3:
        send message to user's phone and email
        
    message.save()
    
    return message.json()

```

**server/settings.py**

``` python
DEBUG = False #for production
```