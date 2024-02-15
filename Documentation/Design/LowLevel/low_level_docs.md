# **Cupid Code**

# **Low Level Design Document**

Team 2

Sprint Leader: Nate Stott

Sprint Followers: Emma Wright, Brighton Ellis, Nate McKenzie, Eric DeBloois, Daniel Barfuss, Brandon Herrin

02/08/24

-----------
### Sub-team Members

#### Frontend team

* Eric 
* Brighton 
* Brandon

#### Middleend team 

* Emma

#### Backend team

* Nate Stott 
* Nate McKenzie 
* Daniel

-----------
### Sub-team Responsibilities

#### Frontend team

* Security 
    * Validate all input and output
* UI (Clean looking)
    * Attractive to look at (keep people coming back)
* UX (Easy to use)
    * Intuitive design
    * Easy to navigate
    * What is happening is clear
* Django Templates (if needed)
* Interact with backend (requests)
    * Deal with timeouts
* Test on many browsers
    * Phone
    * Desktop

#### Middleend team

* work with both teams to ensure that the frontend and backend work together
* do work as requested by either team
  * a team could be falling behind and need help

#### Backend team

* Security
    * Django Admin
    * User Authentication
    * Validate all input and output
* Django models (database)
* Map URLs to views
* Django views (Communicate with frontend, responses)
    * 200
    * 404
* Create system APIs to call external APIs (easy to switch out)
* Django Migrations
* Django settings
* Unit tests

-----------
### Team Conventions and Standards

#### Branching Conventions

* Master 
  * what we are showing
* Hot Fixes 
  * quick fixes for master
* Releases 
  * the next version to be merged with master
* Development 
  * what we are working on
* Features 
  * new features for the development branch

#### Naming Conventions

How will we name our files, directories, variables, functions, classes, etc.?

lowerCamelCase for frontend/Vue
underscore_naming for backend/Django

#### Coding Standards

How will we format our code?

How long can a line be?
  No horizontal scroll
  Every line should only do 1 thing normally
How long can a function be?
  No limit but try to keep efficient
Will we use type hints?
  Yes, for python
When nesting code how many levels deep can we go?

#### Commenting Standards

When will we use comments?
  Can make notes or use for testing, but clean up before merging
When will we use docstrings?
  Should annotate the I/O of a function
How will we format our comments? 

How will we format our docstrings?


#### Testing Standards

How will we test our code? What will we test? How will we document our tests?

-----------
## Frontend Design

### Security
  While a majority of the security will occur on the back, the front will do a little bit to ensure good data is being passed through. This will primarily be validating input and output. 
  If there is bad input, we will visually inform the user of it with sufficient detail. This gives them the opportunity to change it and comply with our standards.
  For example, if someone sends a chat to the AI, we will verify that there is no code injection or other malicious works inserted that would jeopardize the app. If bad input is given, we will inform the user (either via toast or other means) that something went wrong.
  This will also be done for requests from the backend to make sure the given json is correct and valid. This can be done as simple as a check between who the frontend considers the user and who the backend considers the user. This could be done with ids or other unique keys.

  This is the general format most of the asynchronous functions will follow for validating data before displaying it. 
  ```
  async function get<Data>() {
    await the results from getting the profile 
      - this will make a call to the external apis
      - also will use the make requests function referenced in connection
    validate the results
      - if good, set the data to the on screen refs and rerender
      - if bad, put up error on screen for user (toast or otherwise)
  }
  ```

### UI

### UX

### Templates
  A majority of the frontend design will occur in View, but we will want to implement Django Templates for 2 cases. 
    Case 1: A django template is needed to connect the back to the front.
    Case 2: To protect the system, we can make the signing up/logging in its own Django app that will authenticate logging in so that you must be a verified user to use the rest of the app. This method will utilize the Django settings.py variables as well since you can tell it what the login page will be.

  This won't deal with many of the external links since it will be an isolated app that's sole purpose is to add & validate users and redirect them based off of the type of account they are.

### Testing

-----------
## Connecting Vue and Django

The main method we will be implementing will be using these tools: Vite, NPM, and Poetry. 
The frontend will be setup using npm for vite and vue. The backend using poetry for django.

#### Poetry

* Python 3.11+
* Django 5.0.2+
* Requests 2.31.0+
* Python-dotenv 1.0.1+

#### Vite Config

``` javascript
  plugins: [vue()],
  build: {
    manifest: true,
    rollupOptions: {
      input: "./src/main.js"
    },
    outDir: "../<server>/core/static/core"
  },
  base: "/static"
```
#### NPM

* Vue 3.3.11+
* Cookie 0.6.0+

#### Serverside

*Note: Before doing this, make sure you've started a vite project, django project and started at least one app in the django project*

##### Files to Add

* middleware.py in core app
* .env & .env.example in server directory
* templates/core folder with an index.html file in core app

##### Environment

* Add "ASSET_URL=http://localhost:5173" to both.
* Change the url to whatever the client is hosted on.
* Port 5173 is the default of vite so we'll be using that.

##### Middleware

* Add the asset middleware here
* We already have a written one

##### In Server Settings

* Import load_dotenv from dotenv (python-dotenv)
* Add a Debug check for asset middleware:
  * if DEBUG: MIDDLEWARE.append('core.middleware.asset_proxy_middleware')
  * Note: This is the middleware we added/wrote earlier

##### In Core views.py

* Import django.conf settings, json, and os
* Create the MANIFEST variable ({}) and setup loading the manifest.
* Create the index view
  * Create context:
    * asset_url: Use os to get the ASSET_URL from .env
    * debug: Use settings to get the debug
    * manifest: MANIFEST variable
    * js_file: Set to emptry string is in debug mode otherwise set to the manifest file
    * css_file: Follow same protocol as js_file.
  * return a render of the request, index.html, and the context.

##### In Core index.html

  * Generate a default, basic html file
  * Using Django Template, add an if/else statement to the head tag.
    * If debug
      * Two scripts. One points to /@vite/client and one points to src/main.js
        * These will point towards the asset_url from the view as well
      * The else will hold a link and a script using the css and js file from the manifest
  * Add an empty div with id "app" do the body tag. This will connect it to vue's "app" div in its generated index.html file.


#### Clientside

For running the server by default, you won't need to add anything. However, if you want to make some actual requests then this is where Cookie comes in. 
Add a utils folder in your src folder, and make a file called make_requests.js here. Here you'll write a function to send and receive json from the server.

Pseudocode
``` python
import cookie

makeRequest(uri, method, body):
  cookies = parse the cookies 
  options = create a dictionary of what to send to server
    method, headers, credentials
  if the method is post then turn the body into valid JSON

  result = fetch to serverside
  json = the result's json
  return the json
```
``` python
import requests, os, and an http response tool

assetMiddleware(next):
middleware(req):
  if there is a .in the path:
    set response to the asset url with full path
    return a response (consists of the response, content type, status, and reason)
  return next in chain
return middleware
```

-----------
## Backend Design

The backend will be designed using the Django framework. 
Additionally, we will use the Django Rest Framework to create internal APIs. 
The purpose of using internal APIs is to make the system modular and easy to change. 
If we decide to change the way we handle a certain part of the system, we can do so without changing the entire system. 
This will also allow us to test the system in parts, and make sure that each part is working as intended.

Django view functions will be used to handle the requests and responses from the frontend. 
A view function will be able to complete the requested task by using the available internal APIs. 
A view function will not interact with the database or external APIs directly.
This allows us to change the way we handle the database or external APIs without changing the view functions.

### Django Project Structure (Nate S)

What will the project structure look like? What will the files be named? What will the directories be named?

* cupid_code/
  * cupid_code/
    * settings.py
    * urls.py
    * wsgi.py
  * app/
    * migrations/
    * static/
      * favicon.ico
    * templates/
      * app/
        * home.html
        * login.html
        * signup.html
    * admin.py
    * apps.py
    * models.py
    * tests.py
    * urls.py
    * views.py
  * api/
    * migrations/
    * admin.py
    * apps.py
    * models.py
    * serializers.py
    * tests.py
    * urls.py
    * views.py
  * manage.py
  * db.sqlite3

### Outward Facing Endpoints 

|   URL      |   Method |   Notes       |
|------------|----------|---------------|
|   /welcome/|  GET     | Welcome       |
|   /login/  |  GET     | Login page    |
|   /login/  |  POST    | Send form     |
|   /signup/ |  GET     | Signup page   |
|   /signup/ |  POST    | Send form     |
|   /        |  GET     | SPA home      |
|            |          |               |

### Internal Endpoints

|  URL                          |   Method  |   Notes                       |
|-------------------------------|-----------|-------------------------------|
|   /user/                      |   POST    | Create user or update user    |
|   /user/<int:id>/             |   GET     | Get user data                 |
|   /chat/                      |   POST    | Send message                  |
|   /intervention/create/       |   POST    | Create intervention           |
|   /intervention/accept/       |   POST    | Accept intervention           |
|   /intervention/complete/     |   POST    | Complete intervention         |
|   /intervention/<int:count>/  |   GET     | Return a list of count quests |
|   /geo/stores/                |   GET     | List of nearby stores         |
|   /geo/activities/            |   GET     | Nearby activities             |
|   /geo/events/                |   GET     | Nearby events                 |
|   /geo/attractions/           |   GET     | Nearby attractions            |
|   /geo/user/<int:id>/         |   GET     | Get a user's location         |
|   /cupid/rate/                |   POST    | Send a cupd rating            |
|   /cupid/ratings/             |   GET     | Get list of cupid's ratings   |
|   /cupid/avg_rating/<int:id>/ |   GET     | Get cupid's average rating    |
|   /cupid/transfer/            |   POST    | Initiate transfer out         |
|   /cupid/balance/             |   GET     | Get account balance           |
|   /dater/calendar/<int:id>/   |   GET     | Get the dater's cal           |
|   /dater/rate/                |   POST    | Send a dater rating           |
|   /dater/ratings/<int:id>/    |   GET     | Get list of dater's ratings   |
|   /dater/avg_rating/ <int:id>/|   GET     | Get dater's average rating    |
|   /manager/dater_count/       |   GET     | Manager reports               |
|   /manager/cupid_count/       |   GET     | Manager reports               |
|   /manager/active_cupids/     |   GET     | Manager reports               |
|   /manager/intervention_rate/ |   GET     | Manager reports               |
|   /stt/                       |   POST    | Convert speech to text        |
|   /sms/                       |   POST    | Send a text message           |
|   /email/                     |   POST    | Send an email message         |
|                               |           |                               |


-----------
### Django View Functions Design (Daniel)

What views will we need? What will they do? What will they take in? What will they return? What internal APIs will they use?

### Internal API Design (Nate S)

* Implement with the Django Rest Framework
  * https://www.django-rest-framework.org/tutorial/quickstart/
  * Makes building APIs easier
* The purpose of using Internal APIs is to make the system modular and easy to change. If we decide to change the way we handle a certain part of the system, we can do so without changing the entire system. This will also allow us to test the system in parts, and make sure that each part is working as intended.
  * For example, if we need to use another external API we dont have to change the way we use that API in our application, we can just change the internal API that calls the external API.
  * Another example is if we need to change the way we handle user authentication, we can do so without changing the entire system.
* Django API Reference
  * https://docs.djangoproject.com/en/5.0/ref/

1. Create User - for all users
   * Purpose: Create a new user
   * Input (json):
     * Usertype (string)
       * Dater
       * Cupid
       * Manager
     * Username (string)
       * Check for uniqueness
       * Must start with a letter and contain only letters, numbers, and underscores
     * Email (string)
       * Must be a valid email address
       * Check for uniqueness
     * Password (string)
       * Minimum 8 characters with at least one uppercase letter, one lowercase letter, one number, and one special character
     * Confirm Password (string)
       * Must match Password
     * Phone Number (string)
       * 10 digits
       * Check for uniqueness
   * Output (json): 
     * If the user is created, return a success message
     * If the user already exists, return an error message
     * If the user is not created, return an error message
2. Login - for all users
   * Purpose: Authenticate a user
   * Input (json):
     * Username (string)
     * Password (string)
   * Output (json):
     * If the user is signed in, return a success message
     * If the user is not signed in, return an error message
3. Chat with AI - for Daters only
   * Purpose: Allow a user to chat with the AI
   * Input (json):
     * User (string)
     * Message (string)
   * Output (json):
     * If the message is sent, return a success message
     * If the message is not sent, return an error message
4. Request Cupid - for Daters/AI
    * Purpose: Allow a user or AI to request a cupid
    * Input (json):
      * User location (string)
      * User budget (decimal)
      * User preferences (string)
      * User communication preferences (string)
      * User name (string)
      * Task description (string)
    * Output (json):
      * If the request is sent, return a success message
      * If the request is not sent, return an error message
5. Accept Cupid Request - for Cupids
    * Purpose: Allow a cupid to accept a request
    * Input (json):
      * Cupid name (string)
      * Request id (string)
    * Output (json):
      * If the request is accepted, return a success message
      * If the request is not accepted, return an error message
6. Complete Cupid Request - for Cupids
    * Purpose: Allow a cupid to complete a request
    * Input (json):
      * Cupid name (string)
      * Request id (string)
    * Output (json):
      * If the request is completed, return a success message
      * If the request is not completed, return an error message
7. Rate Cupid - for Daters
    * Purpose: Allow a dater to rate a cupid
    * Input (json):
      * Cupid name (string)
      * Dater name (string)
      * Rating (integer)
    * Output (json):
      * If the rating is submitted, return a success message
      * If the rating is not submitted, return an error message
8. Rate Dater - for Cupids
    * Purpose: Allow a cupid to rate a dater
    * Input (json):
      * Cupid name (string)
      * Dater name (string)
      * Rating (integer)
    * Output (json):
      * If the rating is submitted, return a success message
      * If the rating is not submitted, return an error message
9. Get Nearby Stores - for Daters/AI
    * Purpose: Allow a dater to get nearby stores
    * Input (json):
      * User location (string)
    * Output (json):
      * If the stores are found, return a success message
      * If the stores are not found, return an error message
10. Get Nearby Restaurants - for Daters/AI
    * Purpose: Allow a dater to get nearby restaurants
    * Input (json):
      * User location (string)
    * Output (json):
      * If the restaurants are found, return a success message
      * If the restaurants are not found, return an error message
11. Get Nearby Activities - for Daters/AI
    * Purpose: Allow a dater to get nearby activities
    * Input (json):
      * User location (string)
    * Output (json):
      * If the activities are found, return a success message
      * If the activities are not found, return an error message
12. Get Nearby Events - for Daters/AI
    * Purpose: Allow a dater to get nearby events
    * Input (json):
      * User location (string)
    * Output (json):
      * If the events are found, return a success message
      * If the events are not found, return an error message
13. Get Nearby Attractions - for Daters/AI
    * Purpose: Allow a dater to get nearby attractions
    * Input (json):
      * User location (string)
    * Output (json):
      * If the attractions are found, return a success message
      * If the attractions are not found, return an error message
14. Transfer Cupid Cash - for Cupids
    * Purpose: Allow a cupid to transfer cupid cash
    * Input (json):
      * Cupid name (string)
      * Amount (decimal)
    * Output (json):
      * If the transfer is successful, return a success message
      * If the transfer is not successful, return an error message
15. Get Cupid Cash Balance - for Cupids
    * Purpose: Allow a cupid to see their cupid cash balance
    * Input (json):
      * Cupid name (string)
    * Output (json):
      * If the balance is found, return the balance
      * If the balance is not found, return an error message
16. Speech to Text - for AI
    * Purpose: Allow AI to convert speech to text
    * Input (json):
      * Speech (mp3 file
    * Output (json):
      * If the speech is converted, return the text
      * If the speech is not converted, return an error message
17. Edit User profile - for all users
    * Purpose: Allow a user to edit their profile
    * Input (json):
      * User (string)
      * ... 
    * Output (json):
      * If the profile is edited, return a success message
      * If the profile is not edited, return an error message
18. Get User Profile - for all users
    * Purpose: Allow a user to see their profile
    * Input (json):
      * User (string)
    * Output (json):
      * If the profile is found, return the profile
      * If the profile is not found, return an error message
19. Get Dater Calendar - for Daters
    * Purpose: Allow a dater to see their calendar
    * Input (json):
      * Dater name (string)
    * Output (json):
      * If the calendar is found, return the calendar
      * If the calendar is not found, return an error message
20. Get Manager Report - for Managers
    * Purpose: Allow a manager to see a report
    * Input (json):
      * Manager name (string)
    * Output (json):
      * If the report is found, return the report
      * If the report is not found, return an error message
21. Get Cupid Requests - for Cupids
    * Purpose: Allow a cupid to see available requests
    * Input (json):
      * Cupid name (string)
    * Output (json):
      * If the requests are found, return the requests
      * If the requests are not found, return an error message
22. Get Cupid Rating - for Cupids
    * Purpose: Allow a cupid to see their rating
    * Input (json):
      * Cupid name (string)
    * Output (json):
      * If the rating is found, return the rating
      * If the rating is not found, return an error message
23. Get Dater Rating - for Daters
    * Purpose: Allow a dater to see their rating
    * Input (json):
      * Dater name (string)
    * Output (json):
      * If the rating is found, return the rating
      * If the rating is not found, return an error message
24. Get User Location - for all users
    * Purpose: Allow a user to see their location
    * Input (json):
      * User (string)
      * IP address (string)
    * Output (json):
      * If the location is found, return the location
      * If the location is not found, return an error message
25. Text Notification - for all users
    * Purpose: Allow a user to receive a text notification
    * Input (json):
      * User (string)
      * Message (string)
    * Output (json):
      * If the notification is sent, return a success message
      * If the notification is not sent, return an error message
26. Email Notification - for all users 
    * Purpose: Allow a user to receive an email notification
    * Input (json):
      * User (string)
      * Message (string)
    * Output (json):
      * If the notification is sent, return a success message
      * If the notification is not sent, return an error message

#### How to build an internal API

* Create a new app in the project
``` 
$ python manage.py startapp api
```

* In the project settings.py file, add the following to the INSTALLED_APPS list:
  * 'rest_framework'
  * 'api'
``` python
INSTALLED_APPS = [
    ...
    'rest_framework',
    'api',
    ...
]
```

* In the api's models.py file, create the models that will be used by the API
  * In the api's serializers.py file, create the serializers that will be used by the API (serializers are used to convert model instances to JSON)
  * In the UserSerializer class, have fields for the attributes of the User model that will be returned in the JSON response 
    * dont include confidential information like passwords
    * this will be the outward facing representation of the user while the model will be the internal representation
``` python
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=100)
    email = serializers.EmailField()
```

* In the api's views.py file, create the views that will be used by the API
``` python
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer

@api_view(['GET'])
def user_list(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)
    
@api_view(['GET'])
def user_detail(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = UserSerializer(user)
    return Response(serializer.data)
    
@api_view(['POST'])
def user_create(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```

* In the api's urls.py file, create the URLs that will be used by the API
``` python
from django.urls import path
from . import views

urlpatterns = [
    path('user/', views.user_list),
    path('user/<int:pk>/', views.user_detail),
    path('user/create/', views.user_create),
]
```

* In the project's urls.py file, include the api's urls
``` python
from django.urls import path, include

urlpatterns = [
    ...
    path('api/', include('api.urls')),
]
```

### Django Models
Each model will correspond to a table. Bold denotes unique identifiers. Django may provide an ID, but in the case of OneToOne fields, we will more often use those relationships.
* Dater
    * **User : OneToOne Field (As provided by Django)**
    * Phone Number : Text Field (validate user input)
    * Budget : Decimal Field
    * Communication preferences : IntegerChoices
    * Profile Picture : Image Field 
    * Average Rating : Decimal Field
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
        * Date Joined : Date Field
        * Last Active : DateTime Field
 
* Cupid
    * **User : OneToOne Field (As provided by Django)**
    * isActive : Boolean Field (Is cupid accepting interventions)
    * Total interventions completed : Integer Field
    * Total interventions failed : Integer Field
    * Payment : Text Field with payment info (encrypted) 
    * Status : Text Choices
    * Common with Dater
        * Cupid Cash Balance : Decimal Field
        * Location : Text Field (Containing geo coordinates) 
        * Average Rating : Decimal Field
        * Date Joined : Date Field
        * Last Active : DateTime Field
* Message
    * **id : Auto Field**
    * Owner : Foreign Key (User)
    * Text : Text Field
    * fromAI : Boolean Field (Indicates which side of the convo this message belongs to)
* Manager
    * User : OneToOne Field (As provided by Django)
* Intervention Request
    * **id : Auto Field**
    * Dater : Foreign Key
    * Cupid : Foreign Key (nullable, may not be assigned to cupid yet)
    * Quest : OneToOne Field
    * Status : Text Choices
    * DateTime of request : DateTime Field
    * DateTime of claim : DateTime Field
    * DateTime of completion : DateTime Field
* Quest (separate for modularity)
    * **Intervention : *Established by OneToOne Field on Quest***
    * Budget : Decimal Field
    * Items Requested : Text Field 
    * Pickup location : Text Field (address or geolocation to get object from)
* Date
    * **id : Auto Field**
    * Dater : Foreign Key
    * Date & Time : DateTime Field
    * Location : Text Field (Containing geo coordinates?) 
    * Description : Text Field
    * Status : Text Choices
    * Budget : Decimal Field
* Feedback
    * **id : Auto Field**
    * User : Foreign Key (can be a cupid or dater as both have a OneToOne user)
    * Intervention Request : Foreign Key
    * Message : Text Field
    * Star Rating : Integer Field (bound to 1-5)
    * DateTime : DateTime Field 
* Payment Card
    * **User : Foreign Key (can be a cupid or dater as both have a OneToOne user)**
    * Card Number : Text Field
    * CVV : Text Field
    * Expiration : Text Field
* Bank Account
    * **User : Foreign Key (can be a cupid or dater as both have a OneToOne user)**
    * Routing Number : Text Field
    * Account Number : Text Field
    
    
### Django Migrations

What migrations will we need? What will they be used for?

#### Dummy Daters
* username:dater1, password:password, 200 cupid coin balance, budget of 50
* username:dater2, password:password, 20 cupid coin balance, budget of 50
#### Dummy Cupids
* username:cupid1, password:password, 54 completed interventions, 12 failed
* username:cupid2, password:password, 4 completed interventions, 16 failed
#### Dummy Manager
* username:manager, password:password
#### Dummy messages
* Create a few dummy conversation for each dater.
#### Dummy Interventions
* Unclaimed intervention with a unique quest
* Unclaimed intervention with a unique quest
* Claimed intervention
#### Dummy Dates
* A dummy location, date is june 17th so it will never come during this semester.
#### Feedback
* A couple positive reviews for each cupid
* A couple negative reviews for each cupid
* A couple positive reviews for each dater
* A couple negative reviews for each dater

### Django Settings (Daniel)

The settings.py file is used to apply settings to the entire Django project. Here are the current additions to the settings.py file that are included beyond the base settings:

**Admin Allowed in INSTALLED_APPS**

The INSTALLED_APPS lists Django applications that are enabled in this project. To include the ability to have admins, this app is included in the list:

`django.contrib.admin`


### Django Admin (Daniel)

The Django admin site adds the possibility to have admin accounts with levels of management and control. The main functions this account can provide are the following:
* Easy creation, management, and deletion of user accounts
* Easy creation, management, and deletion of data
* Easy adjustment to permissions on user accounts
* Ability to export data (if needed)
* Logging and history of changes made to data

There are some concerns with the admin site and admin accounts. These include:
* Security concerns if an admin account is compromised (bad actor would have access to admin tools)
* Heavy resource usage when modifying accounts or data

To address these concerns, admins may be enforced to have strong passwords (12+ characters, including special characters, numbers, and a mix of lower and upper case characters). Then admin accounts may be used during times when the software experiences the least amount of activity to do intensive work (except for emergencies).


### Unit Tests (Daniel)

We will create unit tests to ensure that the software performs as expected. We will also ensure that security measures are in place to prevent improper usage of the software and protect user data, including Personal Identifiable Information (PII). 

These unit tests will consist of the following:

**Check that user input is sanitized**

*Execution:* Attempt inserting a line of code or SQL query to see if it executes.

*Purpose:* Make sure that data cannot be exfiltrated and code cannot be injected and ran to compromise data. 

**Check that users cannot access pages or chat history that they are not owners of**

*Execution:* Use the URL to attempt to navigate to pages that the user would not own.

*Purpose:* Make sure that users cannot get access to information of other users, and check that users cannot do anything under the account of another user.



* Django debug toolbar
  * https://django-debug-toolbar.readthedocs.io/en/latest/


### Pseudocode

cupid_code/urls.py
``` python



```

cupid_code/settings.py
``` python



```


app/urls.py
``` python



```

app/views.py
``` python
import requests

def get_dater_profile(request, id):
    url = 'http://localhost:8000/api/get_dater_profile/' + id + '/'
    response = requests.get(url)
    return response.json()


```

app/tests.py
``` python



```




api/urls.py
``` python

from django.urls import path
from . import views




```

api/models.py
``` python



```

api/serializers.py
``` python



```

api/views.py
``` python



```


api/tests.py
``` python



```