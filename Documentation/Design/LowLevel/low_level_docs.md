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
### Branching Strategy

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

-----------
## Frontend Design




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

-----------
### Django URL Design (Nate M)

What urls will we need? What views will they map to?
|   URL      |   Method |   Notes       |
|------------|----------|---------------|
|   /        |  GET     | Welcome       |
|   /login/  |  GET     | Login page    |
|   /login/  |  POST    | Send form     |
|   /signup/ |  GET     | Signup page   |
|   /signup/ |  POST    | Send form     |
|   /home/   |  GET     | SPA home      |
|            |          |               |

#### API URLs
|   URL                         |   Method  |   Notes               |
|-------------------------------|-----------|-----------------------|
|   /user/                      |   POST    | Create user           |
|   /user/<int:id>/             |   GET     | Get user data         |
|   /chat/                      |   POST    | Send message          |
|   /quest/create/              |   POST    | Create intervention   |
|   /quest/accept/<int:id>/     |   POST    | Accept intervention   |
|   /quest/complete/<int:id>/   |   POST    | Complete intervention |
|   /cupid/rate/                |   POST    | Send a cupd rating    |
|   /geo/stores/                |   GET     | List of nearby stores |
|   /geo/activities/            |   GET     | Nearby activities     |
|   /geo/events/                |   GET     | Nearby events         |
|   /geo/attractions/           |   GET     | Nearby attractions    |
|                               |           |                       |
|                               |           |                       |


-----------
### Django View Functions Design 

What views will we need? What will they do? What will they take in? What will they return? What internal APIs will they use?

-----------
### Internal API Design

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
     * Email (string)
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
8. Get Nearby Stores - for Daters/AI
    * Purpose: Allow a dater to get nearby stores
    * Input (json):
      * User location (string)
    * Output (json):
      * If the stores are found, return a success message
      * If the stores are not found, return an error message
9. Get Nearby Restaurants - for Daters/AI
    * Purpose: Allow a dater to get nearby restaurants
    * Input (json):
      * User location (string)
    * Output (json):
      * If the restaurants are found, return a success message
      * If the restaurants are not found, return an error message
10. Get Nearby Activities - for Daters/AI
    * Purpose: Allow a dater to get nearby activities
    * Input (json):
      * User location (string)
    * Output (json):
      * If the activities are found, return a success message
      * If the activities are not found, return an error message
11. Get Nearby Events - for Daters/AI
    * Purpose: Allow a dater to get nearby events
    * Input (json):
      * User location (string)
    * Output (json):
      * If the events are found, return a success message
      * If the events are not found, return an error message
12. Get Nearby Attractions - for Daters/AI
    * Purpose: Allow a dater to get nearby attractions
    * Input (json):
      * User location (string)
    * Output (json):
      * If the attractions are found, return a success message
      * If the attractions are not found, return an error message
13. Transfer Cupid Cash - for Cupids
    * Purpose: Allow a cupid to transfer cupid cash
    * Input (json):
      * Cupid name (string)
      * Amount (decimal)
    * Output (json):
      * If the transfer is successful, return a success message
      * If the transfer is not successful, return an error message
14. Get Cupid Cash Balance - for Cupids
    * Purpose: Allow a cupid to see their cupid cash balance
    * Input (json):
      * Cupid name (string)
    * Output (json):
      * If the balance is found, return the balance
      * If the balance is not found, return an error message
15. Speech to Text - for AI
    * Purpose: Allow AI to convert speech to text
    * Input (json):
      * Speech (mp3 file
    * Output (json):
      * If the speech is converted, return the text
      * If the speech is not converted, return an error message
16. Edit User profile - for all users
    * Purpose: Allow a user to edit their profile
    * Input (json):
      * User (string)
      * ... 
    * Output (json):
      * If the profile is edited, return a success message
      * If the profile is not edited, return an error message
17. Get User Profile - for all users
    * Purpose: Allow a user to see their profile
    * Input (json):
      * User (string)
    * Output (json):
      * If the profile is found, return the profile
      * If the profile is not found, return an error message
18. Get Dater Calendar - for Daters
    * Purpose: Allow a dater to see their calendar
    * Input (json):
      * Dater name (string)
    * Output (json):
      * If the calendar is found, return the calendar
      * If the calendar is not found, return an error message
19. Get Manager Report - for Managers
    * Purpose: Allow a manager to see a report
    * Input (json):
      * Manager name (string)
    * Output (json):
      * If the report is found, return the report
      * If the report is not found, return an error message
20. Get Cupid Requests - for Cupids
    * Purpose: Allow a cupid to see available requests
    * Input (json):
      * Cupid name (string)
    * Output (json):
      * If the requests are found, return the requests
      * If the requests are not found, return an error message
21. Rate Dater - for Cupids
    * Purpose: Allow a cupid to rate a dater
    * Input (json):
      * Cupid name (string)
      * Dater name (string)
      * Rating (integer)
    * Output (json):
      * If the rating is submitted, return a success message
      * If the rating is not submitted, return an error message
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

-----------
### Django Models (Nate M)
Each model will correspond to a table. Bold denotes unique identifiers. Django may provide an ID, but in the case of OneToOne fields, we may more often use those relationships.
* Dater
    * **User : OneToOne Field (As provided by Django)**
    * Phone Number : Text Field (validate user input)
    * Cupid Cash Balance : Decimal Field
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
* Cupid
    * **User : OneToOne Field (As provided by Django)**
    * isActive : Boolean Field (Is cupid accepting interventions)
    * Location : //TODO (GeoDjango or use Text Field for whatever API we use)
    * Cupid Cash Balance : Decimal Field
    * Average Rating : Decimal Field
    * Total interventions completed : Integer Field
    * Total interventions failed : Integer Field
    * Date Joined : Date Field
    * Last Active : DateTime Field
    * Payment //TODO (probably will become multiple fields)
    * Status : Text Choices
* Message
    * **id : Auto Field**
    * Owner : Foreign Key (User)
    * Text : Text Field
    * fromAI : Boolean Field (Indicates which side of the convo this message belongs to)
* Manager
    * User : OneToOne Field (As provided by Django)
    * //TODO surely there is more than just a user
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
    * Items Requested : //TODO simplest would be a string, but if we get more advanced that will change.
* Date
    * **id : Auto Field**
    * Dater : Foreign Key
    * Date & Time : DateTime Field
    * Location : //TODO see above
    * Description : Text Field
    * Status : Text Choices //TODO all these choices could be argued as int choices
    * Budget : Decimal Field
* Feedback
    * **id : Auto Field**
    * User : Foreign Key (can be a cupid or dater as both have a OneToOne user)
    * Intervention Request : Foreign Key
    * Message : Text Field
    * Star Rating : Integer Field (bound to 1-5)
    * DateTime : DateTime Field 


-----------
### Django Migrations (Nate M)

What migrations will we need? What will they do?

-----------
### Django Settings

How will we configure the settings?

-----------
### Django Admin

How will we use the Django admin?

-----------
### Unit Tests

What will we test? How will we test it?

* Django debug toolbar
  * https://django-debug-toolbar.readthedocs.io/en/latest/

-----------
### Relationships

* User
  * General user class w/ email, username, password, etc.
  * Possibly use the default User in Django?


* Dater
  * Inherit from User and have sensitive data related to dater here only
    * This would include preferences & personal info

* Cupid
  * Inherit from User and have sensitive data related to cupid here only
    * Includes personal info for finding gigs


* Manager
  * Possibly implement the Django admin class?
  * Or inherit from a gen user class?
    * Composition lets you take objects of other classes and use them here so maybe that will work better than inheritance here

* AI Chat
  * Many-to-one relationship w/ Dater? 
  * Store chat ids and stuff

* Gigs
  * Store and display gigs sent to server by the AI?
  * Many-to-many relationship since many gigs can be shown to many cupids

* Budget
  * One to One relationship with a Dater
  * Encrypted since it'll be sensitive data
  * Leave monetary stuff separate from dater acc for abstraciton & security

* Finances
  * Similar to budget but for cupids
  * Same relationship and reason but won't hold the same type of info since it'll be payment to the cupid
