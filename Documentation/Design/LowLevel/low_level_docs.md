# **Cupid Code**

## **Low Level Design Document**

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
### Relationships

#### User

* General user class w/ email, username, password, etc.
* Possibly use the default User in Django?


#### Dater

* Inherit from User and have sensitive data related to dater here only
  * This would include preferences & personal info


#### Cupid

* Inherit from User and have sensitive data related to cupid here only
  * Includes personal info for finding gigs


#### Manager

* Possibly implement the Django admin class?
* Or inherit from a gen user class?
  * Composition lets you take objects of other classes and use them here so maybe that will work better than inheritance here

#### AI Chat

* Many-to-one relationship w/ Dater? 
* Store chat ids and stuff

#### Gigs

* Store and display gigs sent to server by the AI?
* Many-to-many relationship since many gigs can be shown to many cupids

OR

#### Gig

* Store data for a single gig, and use frontend components to load and list a bunch 
* Then have a one to one with a cupid if accepted?

#### Budget
* One to One relationship with a Dater
* Encrypted since it'll be sensitive data
* Leave monetary stuff separate from dater acc for abstraciton & security

#### Finances
* Similar to budget but for cupids
* Same relationship and reason but won't hold the same type of info since it'll be payment to the cupid


-----------
### Branching Strategy

* Master 
  * what we are showing
* Hot Fixes 
  * quick fixes on master
* Releases 
  * the next version to be merged with master
* Development 
  * what we are working on
* Features 
  * new features for the development branch

-----------
### Testing Strategy

* Write tests for all code
* Write tests while you go

-----------
### Internal API Design


### Django Models
* Dater
    * User : OneToOne Field (As provided by Django)
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
    * User : OneToOne Field (As provided by Django)
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
    * Owner : Foreign Key (User)
    * Text : Text Field
    * fromAI : Boolean Field (Indicates which side of the convo this message belongs to)
* Manager
    * User : OneToOne Field (As provided by Django)
    * //TODO surely there is more than just a user
* Intervention Request
    * Dater : Foreign Key
    * Cupid : Foreign Key (nullable, may not be assigned to cupid yet)
    * Quest : OneToOne Field
    * Status : Text Choices
    * DateTime of request : DateTime Field
    * DateTime of claim : DateTime Field
    * DateTime of completion : DateTime Field
* Quest (separate for modularity)
    * Intervention : *Established by OneToOne Field on Quest*
    * Budget : Decimal Field
    * Items Requested : //TODO simplest would be a string, but if we get more advanced that will change.
* Date
    * Dater : Foreign Key
    * Date & Time : DateTime Field
    * Location : //TODO see above
    * Description : Text Field
    * Status : Text Choices //TODO all these choices could be argued as int choices
    * Budget : Decimal Field
* Feedback
    * User : Foreign Key (can be a cupid or dater as both have a OneToOne user)
    * Intervention Request : Foreign Key
    * Message : Text Field
    * Star Rating : Integer Field (bound to 1-5)
    * DateTime : DateTime Field 
