# **Cupid Code **

## **Low Level Design Document**

Team 2

Sprint Leader: Nate Stott

Sprint Followers: Emma Wright, Brighton Ellis, Nate McKenzie, Eric DeBloois, Daniel Barfuss, Brandon Herrin

02/08/24

Frontend team

	Eric - Pinakamakapangyarihan

Brighton - design

	Brandon

Middle person: Emma

Backend team

	Nate Stott

	Nate McKenzie

	Daniel

Possible Classes

User

	General user class w/ email, username, password, etc.

	Possibly use the default User in Django?


    Dater


    	Inherit from User and have sensitive data related to dater here only


    Cupid


    	Inherit from User and have sensitive data related to cupid here only


    Manager/Admin 


    	Possibly implement the Django admin class?


    	Or inherit from a gen user class?


    	Composition lets you take objects of other classes and use them here so maybe that will work better than inheritance here

AI Chat

	Many-to-one relationship w/ Dater? Store chat ids and stuff

Gigs

	Store and display gigs sent to server by the AI?

	Many-to-many relationship since many gigs can be shown to many cupids

OR 

Gig

	Store data for a single gig, and use frontend components to load and list a bunch 

Then have a one to one with a cupid if accepted?

Frontend team responsibilities



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

Backend team responsibilities



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

Git Branches

	Master - what we are showing

	Hot Fixes - quick fixes on master

	Releases - the next version to be merged with Master

	Development - what we are working on

	Features - new features for the development branch
