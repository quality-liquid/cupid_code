# **Cupid Code**

# **Low Level Design Document**

Team 2

Sprint Leader: Nate Stott

Sprint Followers: Emma Wright, Brighton Ellis, Nate McKenzie, Eric DeBloois, Daniel Barfuss, Brandon Herrin

02/08/24

<!--toc:start-->
- [**Cupid Code**](#cupid-code)
- [**Low Level Design Document**](#low-level-design-document)
    - [Sub-team Members](#sub-team-members)
      - [Frontend Team Members](#frontend-team-members)
      - [Middleend Team Members](#middleend-team-members)
      - [Backend Team Members](#backend-team-members)
    - [Sub-team Responsibilities](#sub-team-responsibilities)
      - [Frontend team](#frontend-team)
      - [Middleend team](#middleend-team)
      - [Backend team](#backend-team)
    - [Team Conventions and Standards](#team-conventions-and-standards)
      - [Branching Conventions](#branching-conventions)
      - [Naming Conventions](#naming-conventions)
      - [Coding Standards](#coding-standards)
      - [Commenting Standards](#commenting-standards)
      - [Testing Standards](#testing-standards)
  - [Frontend Design](#frontend-design)
    - [Security](#security)
    - [UI](#ui)
    - [UX](#ux)
    - [Templates](#templates)
    - [Vue Router](#vue-router)
    - [Testing](#testing)
  - [Connecting Vue and Django](#connecting-vue-and-django)
      - [Poetry](#poetry)
      - [Vite Config](#vite-config)
      - [NPM](#npm)
      - [Serverside](#serverside)
        - [Files to Add](#files-to-add)
        - [Environment](#environment)
        - [Middleware](#middleware)
        - [In Server Settings](#in-server-settings)
        - [In Core views.py](#in-core-viewspy)
        - [In Core index.html](#in-core-indexhtml)
      - [Clientside](#clientside)
  - [Backend Design](#backend-design)
    - [Django Project Structure (Nate S)](#django-project-structure-nate-s)
    - [URL Mapping](#url-mapping)
      - [static endpoints](#static-endpoints)
      - [dynamic endpoints](#dynamic-endpoints)
      - [How to build an internal API](#how-to-build-an-internal-api)
    - [Django Models](#django-models)
    - [Django Migrations](#django-migrations)
      - [Dummy Daters](#dummy-daters)
      - [Dummy Cupids](#dummy-cupids)
      - [Dummy Manager](#dummy-manager)
      - [Dummy messages](#dummy-messages)
      - [Dummy Gigs](#dummy-gigs)
      - [Dummy Dates](#dummy-dates)
      - [Feedback](#feedback)
    - [Django Settings (Daniel)](#django-settings-daniel)
    - [Django Admin (Daniel)](#django-admin-daniel)
    - [Unit Tests (Daniel)](#unit-tests-daniel)
    - [Pseudocode](#pseudocode)
<!--toc:end-->

-----------
### Sub-team Members

#### Frontend Team Members

* Eric 
* Brighton 
* Brandon

#### Middleend Team Members

* Emma

#### Backend Team Members

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
  These functions will use the makeRequest function described in the connection of Vue and Django.

  ``` javascript
  async function get<Data>() {
    await the results from getting the profile 
      - this will make a call to the external apis
      - also will use the make requests function referenced in connection
    validate the results
      - if good, set the data to the on screen refs and rerender
      - if bad, put up error on screen for user (toast or otherwise)
  }
  async function post<Data>() {
    await the request with the method "post" & a body with the information to send
    navigate elsewhere OR rerender page
  }
  ```

### UI

### UX

### Templates
  A majority of the frontend design will occur in View, but we will want to implement Django Templates for 2 cases. 
    Case 1: A django template is needed to connect the back to the front.
    Case 2: To protect the system, we can make the signing up/logging in its own Django app that will authenticate logging in so that you must be a verified user to use the rest of the app. This method will utilize the Django settings.py variables as well since you can tell it what the login page will be.

  This won't deal with many of the external links since it will be an isolated app that's sole purpose is to add & validate users and redirect them based off of the type of account they are.

```html
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
### Vue Router

The Vue app will live at URL `/app/`. The following pages will be available through the Vue Router.

| URL                | Notes                                |
|--------------------|--------------------------------------|
| /dater/home/       | dater homepage                       |
| /dater/chat/       | dater chat page                      |
| /dater/listen/     | dater listen page                    |
| /dater/balance/    | dater cash page                      |
| /dater/calender/   | dater calender page                  |
| /dater/profile/    | dater profile page                   |
| /cupid/home/       | cupid homepage                       |
| /cupid/gigs/       | cupid gigs                           |
| /cupid/balance/    | cupid balance                        |
| /cupid/profile/    | cupid profile                        |
| /manager/home/     | manager homepage                     |
| /manager/cupids/   | manager reports                      |
| /manager/daters/   | manager reports                      |

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

### URL Mapping

#### static endpoints

| URL                | Method | Notes                                | View Function |
|--------------------|--------|--------------------------------------|---------------|
| /                  | GET    | Welcome                              | index         |
| /login/            | GET    | Login page                           | login         |
| /login/            | POST   | Send form                            | check_login   |
| /signup/           | GET    | Signup page                          | signup        |
| /signup/           | POST   | Send form                            | check_signup  |
| /app/              | GET    | Vue Router takes over from here      |               |

Additional pages offered by [Vue Router](#vue-router)

#### dynamic endpoints

* Implement with the Django Rest Framework
  * https://www.django-rest-framework.org/tutorial/quickstart/
  * Makes building APIs easier by providing a set of tools for building APIs
* Django API Reference
  * https://docs.djangoproject.com/en/5.0/ref/

| URL                             | Method | Notes                                | View Function |
|---------------------------------|--------|--------------------------------------|---------------|
| /api/user/create/               | POST   | Create user (use corresponding API)  |               |
| /api/user/<int:id>/             | GET    | Get user data                        |               |
| /api/chat/                      | POST   | Send message                         |               |
| /api/chat/<int:id>/             | GET    | Return the last five chat messages   |               |
| /api/dater/calendar/<int:id>/   | GET    | Get the dater's calendar (date list) |               |      
| /api/dater/rate/                | POST   | Cupid rate Dater                     |               |
| /api/dater/ratings/<int:id>/    | GET    | Get list of dater's ratings          |               |
| /api/dater/avg_rating/<int:id>/ | GET    | Get dater's average rating           |               |
| /api/dater/transfer/            | POST   | Initiate transfer in                 |               |
| /api/dater/balance/<int:id>/    | GET    | Get account balance                  |               |
| /api/dater/profile/<int:id>/    | GET    | Get dater's profile                  |               |
| /api/dater/profile/             | POST   | Set dater's profile                  |               |
| /api/cupid/rate/                | POST   | Dater rating a Cupid                 |               |
| /api/cupid/ratings/<int:id>/    | GET    | Get list of cupid's ratings          |               |
| /api/cupid/avg_rating/<int:id>/ | GET    | Get cupid's average rating           |               |
| /api/cupid/transfer/            | POST   | Initiate transfer out                |               |
| /api/cupid/balance/<int:id>/    | GET    | Get account balance                  |               |
| /api/cupid/profile/<int:id>/    | GET    | Get cupid's profile                  |               |
| /api/cupid/profile/             | POST   | Set cupid's profile                  |               |
| /api/gig/create/                | POST   | Create gig                           |               |
| /api/gig/accept/                | POST   | Accept gig                           |               |
| /api/gig/complete/              | POST   | Complete gig                         |               |
| /api/gig/drop/                  | POST   | Drop gig                             |               |
| /api/gig/<int:count>/           | GET    | Return number of gigs around cupid   |               |
| /api/geo/stores/                | GET    | List of nearby stores                |               |
| /api/geo/activities/            | GET    | Nearby activities                    |               |
| /api/geo/events/                | GET    | Nearby events                        |               |
| /api/geo/attractions/           | GET    | Nearby attractions                   |               |
| /api/geo/user/<int:id>/         | GET    | Get a user's location                |               |
| /api/manager/cupids/            | GET    | Get a list of cupids                 |               |
| /api/manager/daters/            | GET    | Get a list of daters                 |               |
| /api/manager/dater_count/       | GET    | Manager reports                      |               |
| /api/manager/cupid_count/       | GET    | Manager reports                      |               |
| /api/manager/active_cupids/     | GET    | Manager reports                      |               |
| /api/manager/gig_rate/          | GET    | Manager reports                      |               |
| /api/manager/suspend/           | POST   | suspend cupid / dater                |               |
| /api/manager/unsuspend/         | POST   | unsuspend cupid / dater              |               |
| /api/stt/                       | POST   | Convert speech to text               |               |
| /api/notify/                    | POST   | Send a message according to pref.    |               |

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

* in the app view
``` python

import requests

def get_dater_profile(request, id):
    url = 'http://localhost:8000/api/get_dater_profile/' + id + '/'
    response = requests.get(url)
    return response.json()

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
    path('/user/', views.user_list),
    path('/user/<int:pk>/', views.user_detail),
    path('/user/create/', views.user_create),
]
```

* In the project's urls.py file, include the api's urls
``` python
from django.urls import path, include

urlpatterns = [
    ...
    path('/api/', include('api.urls')),
]
```

### Django Models
Each model will correspond to a table. Bold denotes a primary key. For most tables,
this is the default id provided by Django. For certain one-to-one tables they will use that
relationship as their primary key. 

We will use the Django built in User model, but add roles to it. This comes with authentication functionality and the following fields. Details available in 
[Django docs](https://docs.djangoproject.com/en/5.0/ref/contrib/auth/#django.contrib.auth.models.User).

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

* Dater
    * **User : OneToOne Field (As provided by Django)**
    * Phone Number : Text Field (validate user input)
    * Budget : Decimal Field
    * Communication preferences : IntegerChoices
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
    * Payment : Text Field with payment info (encrypted) 
    * Status : Text Choices
    * Common with Dater
        * Cupid Cash Balance : Decimal Field
        * Location : Text Field (Containing geo coordinates) 
        * Average Rating : Decimal Field
        * Suspended : Boolean Field
* Message
    * **id : Auto Field**
    * Owner : Foreign Key (User)
    * Text : Text Field
    * fromAI : Boolean Field (Indicates which side of the convo this message belongs to)

* Manager doesn't need anything more than a Django user in the manager role

* Gig
    * **id : Auto Field**
    * Dater : Foreign Key
    * Cupid : Foreign Key
    * Quest : OneToOne Field
    * Status : Text Choices
    * DateTime of request : DateTime Field
    * DateTime of claim : DateTime Field
    * DateTime of completion : DateTime Field
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
    * Status : Text Choices
    * Budget : Decimal Field
* Feedback
    * **id : Auto Field**
    * User : Foreign Key (can be a cupid or dater as both have a OneToOne user)
    * Gig : Foreign Key
    * Message : Text Field
    * Star Rating : Integer Field (bound to 1-5)
    * DateTime : DateTime Field 
* Payment Card
    * **User : Foreign Key**
    * Card Number : Text Field
    * CVV : Text Field
    * Expiration : Text Field
* Bank Account
    * **User : Foreign Key**
    * Routing Number : Text Field
    * Account Number : Text Field
    
    
### Django Migrations


#### Dummy Daters
* username:dater1, password:password, 200 cupid coin balance, budget of 50
* username:dater2, password:password, 20 cupid coin balance, budget of 50
#### Dummy Cupids
* username:cupid1, password:password, 54 completed gigs, 12 failed
* username:cupid2, password:password, 4 completed gigs, 16 failed
#### Dummy Manager
* username:manager, password:password
#### Dummy messages
* Create a few dummy conversation for each dater.
#### Dummy Gigs
* Unclaimed gig with a unique quest
* Unclaimed gig with a unique quest
* Claimed gig
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

Check the following Pseudocode section for `tests.py`, which contains planned unit tests.



* Django debug toolbar
  * https://django-debug-toolbar.readthedocs.io/en/latest/


### Pseudocode

cupid_code/urls.py
``` python
path("", include("app.urls")),
path("api/", include("api.urls")),
path("admin/", admin.site.urls),
```

cupid_code/settings.py
``` python
# Very little will change from the settings.py initial configuration made on generation.
# Here are some adjustment(s)

INSTALLED_APPS = [
  ...
  'django.contrib.admin',
  rest_framework,
  'api',
  'app',
  ...
]
```

api/urls.py
``` python

from django.urls import path
from . import views

urlpatterns = [
    
]

```

api/models.py
``` python

from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    class Role(models.TextChoices):
        DATER = 'Dater'
        CUPID = 'Cupid'
        MANAGER = 'Manager'

    role = models.CharField(choices=Role.choices, max_length=7)

class Dater(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone_number = models.CharField(max_length=10)
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    communication_preferences = models.IntegerField()
    profile_picture = models.ImageField()
    description = models.TextField()
    dating_strengths = models.TextField()
    dating_weaknesses = models.TextField()
    interests = models.TextField()
    past = models.TextField()
    nerd_type = models.TextField()
    relationship_goals = models.TextField()
    ai_degree = models.TextField()
    cupid_cash_balance = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.TextField()
    average_rating = models.DecimalField(max_digits=10, decimal_places=2)
    suspended = models.BooleanField()

class Cupid(models.Model):
    class Status(models.IntegerChoices):
        OFFLINE = 0
        GIGGING = 1
        AVAILABLE = 2

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    accepting_gigs = models.BooleanField()
    gigs_completed = models.IntegerField()
    gigs_failed = models.IntegerField()
    payment = models.TextField()
    status = models.IntegerField(choices=Status.choices)
    cupid_cash_balance = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.TextField()
    average_rating = models.DecimalField(max_digits=10, decimal_places=2)
    
class Message(models.Model):
    owner = models.ForeignKey(User, primary_key=True, on_delete=models.CASCADE)
    text = models.TextField()
    from_ai = models.BooleanField()

class Gig(models.Model):
    class Status(models.IntegerChoices):
        UNCLAIMED = 0
        CLAIMED = 1
        COMPLETE = 2
        DROPPED = 2

    dater = models.ForeignKey(Dater, on_delete=models.CASCADE)
    cupid = models.ForeignKey(Cupid, on_delete=models.CASCADE)
    quest = models.OneToOneField(Quest, on_delete=models.CASCADE)
    status = models.IntegerField(chioces=Status.choices)
    date_time_of_request = models.DateTimeField()
    date_time_of_claim = models.DateTimeField()
    date_time_of_completion = models.DateTimeField()

class Quest(models.Model):
    gig = models.OneToOneField(Gig, on_delete=models.CASCADE, primary_key = True)
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    items_requested = models.TextField()
    pickup_location = models.TextField()
    
class Date(models.Model):
    dater = models.ForeignKey(Dater, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    location = models.TextField()
    description = models.TextField()
    status = models.TextField()
    budget = models.DecimalField(max_digits=10, decimal_places=2)

class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    gig = models.ForeignKey(Gig, on_delete=models.CASCADE)
    message = models.TextField()
    star_rating = models.IntegerField()
    date_time = models.DateTimeField()
    
class PaymentCard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    card_number = models.TextField()
    cvv = models.TextField()
    expiration = models.TextField()

class BankAccount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    routing_number = models.TextField()
    account_number = models.TextField()

```

api/serializers.py
``` python

from rest_framework import serializers



```

api/views.py
``` python

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Dater, Cupid, Message, Manager, Gig, Quest, Date, Feedback, PaymentCard, BankAccount
from .serializers import DaterSerializer, CupidSerializer, MessageSerializer, ManagerSerializer, GigSerializer, QuestSerializer, DateSerializer, FeedbackSerializer, PaymentCardSerializer, BankAccountSerializer

def sign_in(reqeust):
    if reqeust.method == "POST":
        username = reqeust.POST.get("email")
        password = reqeust.POST.get("password")
        user = authenticate(reqeust, username=username, password=password)
        if user is not None:
            login(reqeust, user)
            return redirect("/app/")

        if User.objects.filter(email=username):
            message = "Incorrect Password"
        else:
            message = "Email Not Found"
        return render(
            reqeust,
            "registration/sign_in.html",
            {
                "message": message,
                "email": username,
            },
        )
    else:
        return render(reqeust, "registration/sign_in.html")
        
def login(request):
    if request.method == "POST":
        username = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/app/")
        else:
            return render(request, "registration/login.html", {"message": "Incorrect Password"})
    else:
        return render(request, "registration/login.html")


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

  response = {method call to send to external AI chat API}

  return response.json()

def get_five_messages(request, id):
  dater = Dater.objects.get(id=id)

  list_of_messages = Message.objects.filter(owner=id)

  ordered_most_recent_messages = reorder list_of_messages from newest to oldest

  list_of_messages = first five of ordered_most_recent_messages

  response = list_of_messages.json()

  return response

def get_calendar(request, id):
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
  card_on_file = Payment_Card.objects.get(user=dater_id)

  transfer_amount = request.transfer_amount
  
  result = way to transfer money from card(card_on_file, transfer_amount)

  dater.balance = dater.balance + result

  send result to company bank account

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

def get_cupid_avg_rating(request, id):
  cupid = Cupid.objects.get(id=id)

  avg_rating = cupid.avg_rating

  response = avg_rating.json()

  return response

def cupid_transfer(request):
  cupid_id = request.cupid_id
  bank_account = Bank_Account.objects.get(user=cupid_id)

  transfer_amount = request.transfer_amount
  
  send transfer_amount to bank_account
  
  cupid.balance = dater.balance - transfer_amount

  cupid.save()

  return JsonResponse({'message': 'Deposit successful'})

def get_cupid_balance(request, id):
  dupid = Cupid.objects.get(id=id)

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

```

api/tests.py
``` python

from django.test import TestCase
from unittest.mock import MagicMock

# Testing APIs

class UserAPITestCase(TestCase):
    
    def test_create_user(self):
        # Mock the client.post method
        with MagicMock() as mock_post:
            mock_post.return_value.status_code = 201
            
            # Assign the mocked post method to self.client.post
            self.client.post = mock_post
            
            # Make the request using self.client.post (which is now mocked)
            response = self.client.post('/api/user/', {'username': 'testuser', 'email': 'test@test.test', 'password': 'password', 'phone_number': '1234567890', 'budget': 50, 'communication_preferences': 1, 'profile_picture': 'test.jpg', 'average_rating': 5, 'text_available_to_ai': 'test', 'cupid_cash_balance': 50, 'location': 'test', 'date_joined': '2021-01-01', 'last_active': '2021-01-01'})
            
            # Assert the response status code
            self.assertEqual(response.status_code, 201)
        

```
