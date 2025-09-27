# User Interface


The previous team's high-level design document includes almost everything that we intend to use for our user interface with a few minor changes. 

The UI will be optimized for mobile use for Cupids and Daters, but the manager interface will be optimized for desktop. However, it will be designed to be accessable on all devices. 

## Components
1. Log In/Sign Up
    * The log-in page is accessible to all users, while the sign-up page is available for new Daters and Cupids.
    * Daters and Cupids will input data in order to make their profiles.
    * Some data will be required, such as username and password, while other data will be optional, such as interests.
    * The sign-up page will be updated to indicate which fields are required
    * The sign-up page will allow the user to create an account even if optional fields are left blank.
2. Profile Viewing/Editing
    * Daters and Cupids will both be able to view a profile page which displays their own data and they will be able to edit any of their own data.
    * Dater profiles will show their dating history on the app.
    * Cupid profiles will show their gig history and finances.
3. AI Chat
    * This page will have a messaging feature with the AI chatbot, which will be configured to help with planning dates and other dating advice.
4. AI Listen-in
    * This page will listen to the conversation during the date and give real-time advice to the Dater as needed. 
    * It will also provide real-time information about Cupids or other dating opportunities.
5. Cupid Main Page
    * This will be the home page for Cupids.
    * It will provide links to the following pages
      - Cupid gigs
      - Profile
      - App feedback
6. Dater Main Page
    * This will be the home page for the Daters.
    * It will provide links to the following pages
      - Calendar
      - AI chat
      - Cupid Cash
      - Profile
      - App feedback
7. Manager Main Page
    * Managers will be able to see any feedback given by Daters or Cupids
    * They will also have the option to go to the report system page.
8. Calendar
    * Daters will be able to use the calendar to schedule their dates.
9. Cupid Cash
    * Daters will be able to purchase Cupid Cash via PayPal or Stripe.
    * They will be able to view their current amount and spending history.
10. Manager Report System
    * Managers can view statistics on users, such as number of Cupids, number of Daters, user rating, and financial information.
    * They will be able to generate reports with whatever information they select and save it as a PDF.
11. Feedback System
    * Daters will be able to give feedback to the developers on bugs/features and be able to rate and review any Cupids who have done gigs for them.
    * Cupids will be able to give feedback to the developers on bugs/features and be able to rate and review any Daters that they've done gigs for.
    * Managers will be ablo to review all feedback to developers or between Daters and Cupids.
    * Managers will also be able to remove/warn users with low ratings.
12. Cupid Gig Finder
    * This page will display a list of nearby available gigs.
    * Any gig in progress will be highlighted at the top.
    * Clicking on a gig will open it in a pop-up which will give more information about that gig.
13. Cupid Chosen Gig
    * The gig will display information such as distance, time, and dater rating.
    * The Cupid will be able to accept or reject the gig. Gigs already selected can be cancelled.

### Component interaction

--> GENERAL LOGIN UML DIAGRAM

**General Login**

The user will enter username and password. The system will validate the input. If valid, it will direct them to their respective homepage. Otherwise, it will tell the user that either username or password are incorrect.

--> DATER LOGIN UML DIAGRAM

**Dater Login**

The Dater homepage will allow them to select one of these pages: Calendar, AI chat, Cupid Cash, Profile, or App feedback.

--> CUPID LOGIN UML DIAGRAM

**Cupid Login**

The Cupid homepage will allow them to select one of these pages: Cupid gigs, Profile, or App feedback.

--> MANAGER LOGIN UML DIAGRAM

**Manager Login**

The Manager homepage will allaw them to select one of these pages: Report system, Feeback System.

**Login System Design Purpose**

The system will use modularization in order to break it down into seperate components. This makes each component more manageable and easier to change without disrupting the rest of the program. This allows the program to be better suited to future changes and additions. It will also make development simpler and easier to divide tasks between multiple team members.