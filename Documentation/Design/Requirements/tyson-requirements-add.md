## Summary of Previous Teams Requirements

### What Previous Team Did Not Complete
#### Cupid Pages
* Range in profile update has no units on it, 20 what?
* Feedback page says undefined, does not work.
* No indication that updates to profile info actually saved.
* Gigs do not show how far away they are, we already (supposedly I have not
checked) calculate that to offer it to them within the cupid's desired range,
we should display it on the card.

#### Dater Pages
* Sign Up
    * Does not work. I filled out all the fields first with stuff that did not
    make sense for the field, then stuff that should work but when I click
    create account nothing happens on the page.
    * No password requirements enforced on sign up
    (at least 12 chars, has a symbol, etc...)

#### Non-Functional Requirements
* There was no requirements for strong passwords on signup, this goes against
their requirement for strong security.
* The documentation is unclear in some ways, following what they had 
written for project setup I have been unable to get the Dater signup page to 
work.


## Functional Requirements
### User Roles
#### User Role Definitions
0. *Dater* is defined as the regular user of our application. They are using 
the application for help to have successful dates and achieve a happy
relationship.
0. *Cupids* are workers who sign up to help out daters, not for themselves.
Similar to Uber Eats workers, but for more than just food, they fulfill jobs
created by the Dater/the Dater's AI.
0. *Business Leaders* are defined as any high level decision making
leadership at Duckiecorp and of course our esteemed customer 
Cowboy Erik Falor.

#### Daters will be able to:
* Recieve notifications from the webapp for:
    * Updates or help on date plans
    * Cupid order status
    * Get an advice message from the AI listening when the date is going 
    poorly.
* Use Stripe and/or PayPal to add funds to their CupidCash balance.
* Plan out a date's activities, costs, and location in our web application 
interface with smart assistance from the AI.
* Chat with the AI for help, ideas, or practicing for an upcoming date.
* Get occasional advice from the AI when dates are becoming sparse 
based on the user's profile, preferences, and what the AI learns about the user 
over time. 
* Create a work order for a Cupid
    * Choose how much Cupid cash to dedicate to the order.
    * Fill in instructions for Cupid.
    * Set time must be completed by. 

#### Cupids will be able to:
* Accept a job from a list displayed based on their chosen filters:
    * mile radius
    * level of difficulty/estimated time to complete
* See the jobs in priority order based on when they expire. 
* Sign-up as a Cupid so their app interface is different.

#### Business Leadership will be able to:
* Access metrics boards for Daters showing the following
    * Current number registered.
    * Current number online (in an active session on the webapp)
    * Current number in an active date.
    * Locations of all Daters.
* Access metrics boards for Cupids showing the following
    * Current number registered.
    * Current number online (in an active session on the webapp)
    * Current number in an active job.
    * Number of jobs fulfilled
    * Number of jobs expired (no cupid accepted)

## User Stories
### Daters
0. As a Dater, I want to get advice from the AI mid-date to save me when I mess
up.
1. As a Dater, I want to see my Cupid Cash balance easily so I do not end up
running out at a bad time.
2. As a Dater, I want to get location specific help with planning a date so I 
can have an easier experience plannning out a good date.
3. As a Dater, I want to schedule payments into my Cupid Cash account so I never
run out of funds to plan good dates.
4. As a Dater, I want to recieve messages from my AI companion on how I am doing
throughout the date so I can overcome my social awkwardness.
5. As a Dater, I want the AI to recognize when the data is going well and not be
messaging me so I am not distracted.
6. As a Dater, I want to see when a Cupid has picked up my work request so I 
can relax knowing it is getting done.
7. As a Dater, I want to be able to get funds out of my Cupid Balance, so I do
not end up in financial trouble if I accidently send too much money to my Cupid
account.
8. As a Dater, I want to have an interactive UI, so I know that actions I 
perform were successful and I do not worry that my work did not save.
9. As a Dater, I want to be able to input data about my potential date so my AI
will help me remember important details that I tend to forget.