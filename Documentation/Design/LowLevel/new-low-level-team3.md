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
0. [Frontend Design](#frontend-design)
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
0. [Middleend Design](#1-middleend-design)
0. [Backend Design](#2-backend-design)


# 0. Frontend Design
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
TODO - That said, I don't think there's a whole lot that we can do on the frontend for this except for make sure we keep it lightweight.

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
TODO

#### Implementing the router
TODO

### Vue URLs
TODO

### Testing
TODO

# 1. Middleend Design
[*Table of Contents*](#table-of-contents)
* This section for design how to connect the frontend and backend

# 2. Backend Design
[*Table of Contents*](#table-of-contents)