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
## Frontend Design

Subsections
- [Frontend Design](#frontend-design)
- [Security](#security)
- [UI](#ui)
- [UX](#ux)
- [Templates](#templates)
- [Vue Router](#vue-router)
  - [Implementation](#implementing-the-router)
- [Testing](#testing)

### Security
The previous team had done a good job in maintaining security within the app. They did not implement a strong password system, which we will implement by... 

If a user loses their account information, a form of Two-Step Authentication will be provided to allow them to reset their password and enter their account. Managers will also require Two-Step Authentication every time they log in. We will do this by...

We also intend to make calls to external APIs and thus we need to ensure that we safeguard any response that could be malicious. We will do this by...

### Performance
The frontend will verify any inputs that it can before making requests to the backend to lower the amount of requests made to the backend. For example, the frontend will check that an entered email is valid before making a request. Since the page is a single page application, we are also able to reduce the number of requests to the backend.

By reducing how many requests we make to the server, the user is able to interact with the app more without having to wait for constant responses from the server.

### UI
TODO - Add a dark theme, change up the colors and web page (we're going to need to update all the images), create a "Plan-a-Date" page

#### User Flow:
TODO

#### Screen Designs:
TODO

#### Navigation Structure:
TODO

#### Layout Guidelines:
TODO

#### Color Palette:
TODO

#### Icon Use:
TODO

#### Responsive Design:
TODO

#### Making accounts and Logging in
TODO

#### Dater
TODO: remember that we're adding an option for married individuals to seek dating assistance

#### Cupid
TODO

#### Manager
TODO

### UX
TODO

### Templates

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

### Vue Router

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

#### Implementing the router

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

### Vue URLs
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

### Testing
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

### Django Models

TODO: update 

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

### Django Migrations

TODO: update

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

### External API's

TODO: update

We will be using the following external APIs:

* [GeoLite2](https://www.maxmind.com/en/geoip2-databases)
  * Used to look up location by IP address.
  * Free to use.
  * Provides accurate location data.
  * Easy to integrate with Django.
* [gpt2](https://huggingface.co/openai-community/gpt2)
  * Used to generate responses for the chatbot.
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

### Quick Tutorial on how to use the Django Rest Framework

TODO: update

* Create a new app in the project
``` 
$ python manage.py startapp example
```

* In the project `settings.py` file, add the following to the INSTALLED_APPS list:
  * 'rest_framework'
  * 'example'
``` python
INSTALLED_APPS = [
    ...
    'rest_framework',
    'example',
    ...
]
```

* In the `example/models.py` file, create the models that will be used by the API
``` python

from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    is_suspended = models.BooleanField()
    is_cupid = models.BooleanField()
```

* In the `example/serializers.py` file, create the serializers that will be used by the API (serializers are used to convert model instances to JSON and vice versa)
  * ReaderUserSerializer will be used to convert User instances to JSON
  * WriterUserSerializer will be used to convert JSON to User instances
``` python
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
    
    def validate(self, data):
        if data['password'] == data['confirm_password']:
            return serializers.ValidationError('Password cannot be "password"')
        return data
    
    def create(self, validated_data):
        user = User(**validated_data)
        user.is_suspended = False
        user.save()
        return user
        
    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.password = validated_data.get('password', instance.password)
        instance.save()
        return instance
```

* In the `example/views.py` file, create the views that will be used by the API
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
    serializer.is_valid(raise_exception=True):
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)
    
@api_view(['PUT'])
def user_update(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = UserSerializer(user, data=request.data)
    serializer.is_valid(raise_exception=True):
    serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def user_delete(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
```

* In the `example/urls.py` file, create the URLs that will be used by the API
``` python
from django.urls import path
from . import views

urlpatterns = [
    path('/user/', views.user_list),
    path('/user/<int:pk>/', views.user_detail),
    path('/user/create/', views.user_create),
]
```

* In the project's `urls.py` file, include the api's urls
``` python
from django.urls import path, include

urlpatterns = [
    ...
    path('/api/', include('api.urls')),
]
```

