# CS3450 Fall 2025 Team 3 Requirements Document
## Summary of Previous Teams Requirements

The previous team’s requirements document for Cupid Code details a dating assistance platform built around artificial intelligence, human “Cupid” helpers, and robust user management. The app addresses the unique social and logistical challenges faced by its user base, especially those who may find dating intimidating or unfamiliar. Core functionalities include role-based features for Daters, Cupids, and Managers, such as scheduling, budgeting, AI-driven advice (before, during, and after dates), secure payments, and structured feedback. AI integrates tightly with the experience, offering real-time tips and summoning assistance during dates if needed.

In addition to essential features like authentication, calendar management, and budget controls, the platform places a strong emphasis on user privacy, data security, and responsive support systems for all parties. The business logic prioritizes quality of service, continuous innovation, and compliance with legal requirements, with mechanisms for revenue generation through subscriptions and service fees. The requirements also distinguish between must-have baseline features and more advanced, optional enhancements, supporting phased development as resources and feedback allow. The document’s user stories and structured priorities lay a foundation for an adaptable, user-focused, and secure dating solution.

[Paragraph to address which requirements they met, which they didn't, and what the documentation says about the requirements they didn't meet]

## MoSCoW Key for Requirements
- Mo = Must-Have requirement, a requirement that cannot be missing and will take the highest priority in this update.
    - `Cupid Code shall meet a requirement.` **(M)**
- S = Should-Have requirement, a requirement that is essential and will take higher priority in this update but is not critical to release. 
    - `Cupid Code shall meet a requirement.` **(S)**
- Co = Could-Have requirement, a requirement that is a good feature to add but is not a high priority in this update.
    - `Cupid Code shall meet a requirement.` **(C)**
- W = Will-Have Eventually requirement, a requirement that will not be included in this update but will be included later.
    - `Cupid Code shall meet a requirement.` **(W)**

### Rebranding Requirements
- Cupid Code shall provide a dark mode theme. **(M)**
- Cupid Code shall provide a light mode theme. **(M)**

### Push Notification Requirements
- Cupid Code shall send push notifications to Daters with reminders about planned dates. **(M)**
- Cupid Code shall send push notifications to Daters with conversation suggestions. **(M)**
- Cupid Code shall send push notifications to Daters with weather alerts. **(M)**
- Cupid Code shall send push notifications to Daters with date tips prior to a planned date. **(M)**
- Cupid Code shall send push notifications to Daters with date tips during a planned date. **(M)**
- Cupid Code shall send push notifications to Daters with date tips after a planned date. **(M)**
- Cupid Code shall send push notifications to Daters with encouragement to set up more dates. **(M)**
- Cupid Code shall send push notifications to Daters when a service is successfully ordered for a planned date. **(M)**
- Cupid Code shall send push notifications to Daters when a Cupid has arrived **(M)**
- Cupid Code shall send push notifications to Cupids with new job appearances. **(M)**
- Cupid Code shall integrate with a texting service to send messages to Daters. **(M)**
- Cupid Code shall integrate with a texting service to send messages to Cupids. **(M)**
- Cupid Code shall integrate with an email service to send messages to Daters. **(M)**
- Cupid Code shall integrate with an email service to send messages to Cupids. **(M)**
- Cupid Code shall allow a Dater to opt-in or opt-out of receiving specific types of push notifications. **(M)**
- Cupid Code shall allow a Cupid to opt-in or opt-out of receiving specific types of push notifications. **(M)**
- Cupid Code shall aggregate related notifications to avoid notification fatigue. **(M)**
- Cupid Code shall allow a Dater to set preferences for notification timing and frequency. **(M)**
- Cupid Code shall allow a Cupid to set preferences for notification timing and frequency. **(M)**
- Cupid Code shall use multiple methods of delivery for notifications supporting push, SMS, and email. **(M)**
- Cupid Code shall provide a notification center within the app for Daters to view all past notifications. **(M)**
- Cupid Code shall provide a notification center within the app for Cupids to view all past notifications. **(M)**
- Cupid Code shall prevent sending redundant notifications by deduplicating similar events. **(M)**
- Cupid Code shall integrate with the Weather Channel API to provide weather forecast data. **(M)**

### Agentic AI
- Cupid Code shall allow the Dater to customize the autonomy of the AI in their preferences. **(M)**
- Cupid Code shall allow the AI to edit a date's activity. **(M)**
- Cupid Code shall allow the AI to edit a date's estimated cost. **(M)**
- Cupid Code shall allow the AI to edit a date's address. **(M)**
- Cupid Code shall allow the AI to edit a date's partner. **(M)**
- Cupid Code shall allow the AI to edit a date's start time. **(M)**
- Cupid Code shall allow the AI to edit a date's date. **(M)**
- Cupid Code shall allow the AI to edit a date's estimated end time. **(M)**
- Cupid Code shall allow the AI to delete a date. **(M)**
- Cupid Code shall allow the AI to create a date. **(M)**
- Cupid Code shall implement a jobs queue for managing third-party service requests and Cupid-specific errands. **(M)**
- Cupid Code shall allow the AI to place food orders via UberEats API. **(M)**
- Cupid Code shall allow the AI to arrange rides via Uber API. **(M)**
- Cupid Code shall allow the AI to purchase movie tickets via Megaplex API. **(M)**
- Cupid Code shall allow the AI to fetch and recall Dater-specific preferences and history from the Dater database to personalize decisions and recommendations. **(M)**
- Cupid Code shall allow the AI to cancel previously arranged food orders via UberEats API. **(M)**
- Cupid Code shall allow the AI to cancel previously arranged rides via Uber API. **(M)**
- Cupid Code shall allow the AI to cancel previously arranged movie tickets via Megaplex API. **(M)**
- Cupid Code shall allow the AI to access weather forecast data. **(M)**
- Cupid Code shall allow the AI to make weather-based suggestions for date activities. **(S)**
- Cupid Code shall allow the AI to ask the Daters about how their date went and what could be improved. **(S)**
- Cupid Code shall allow the AI to provide Daters with actionable feedback after a date. **(S)**
- Cupid Code shall allow the AI to provide Dater profile completion to fill in missing interests, hobbies, or preferences. **(S)**
- Cupid Code shall allow the AI to build a dream partner profile for a Dater. **(S)**
- Cupid Code shall allow the Daters to enable conversation listening during a planned date. **(S)**
- Cupid Code shall allow the Daters to enable integration with the device microphone. **(S)**
- Cupid Code shall allow the AI to listen during planned dates when conversation listening is enabled. **(S)**
- Cupid Code shall allow the AI to provide an estimated time until relationship/marriage. **(C)**
- Cupid Code shall allow the AI to dream partner profile with the profiles of other Daters. **(C)**

### Cloud Deployment
- Cupid Code shall be deployed using Azure **(M)**

### Payment Processer APIs
- Cupid Code shall integrate with Stripe APIs to process payments. **(M)**
- Cupid Code shall integrate with PayPal APIs to process payments. **(M)**
- Cupid Code shall allow a Dater to connect a bank account to their Cupid Code CupidCash funds using Stripe APIs. **(M)**
- Cupid Code shall allow a Dater to connect a bank account to their Cupid Code CupidCash funds using PayPal APIs. **(M)**
- Cupid Code shall allow a Dater to make a request to withdraw funds from a bank account to their CupidCash funds using Stripe APIs. **(M)**
- Cupid Code shall allow a Dater to make a request to withdraw funds from a bank account to their CupidCash funds using PayPal APIs. **(M)**
- Cupid Code shall allow a Dater to make a request to deposit funds to a bank account from their CupidCash funds using Stripe APIs. **(M)**
- Cupid Code shall allow a Dater to make a request to deposit funds to a bank account from their CupidCash funds using PayPal APIs. **(M)**
- Cupid Code shall not allow a Dater to make a request to deposit funds to a bank account from their CupidCash funds if the amount exceeds their current balance of CupidCash. **(M)**
- Cupid Code shall display transaction history within the Dater's account dashboard. **(M)**
- Cupid Code shall display transaction history within the Cupid's account dashboard. **(M)**
- Cupid Code shall allow a Dater to set a default payment method for processing payments made by the Dater. **(M)**
- Cupid Code shall allow a Dater to set a default payment method for processing payments made by the AI. **(M)**
- Cupid Code shall not make use of microtransactions. **(M)**

### Plan-A-Date Feature
- Cupid Code shall implement a Plan-A-Date service. **(M)**
- Cupid Code Plan-A-Date service shall allow the Dater to make a request to the AI to build a date based on past interests. **(M)**
- Cupid Code Plan-A-Date service date interface shall allow the Dater to edit the date's activity. **(M)**
- Cupid Code Plan-A-Date service date interface shall allow the Dater to edit the date's estimated cost. **(M)**
- Cupid Code Plan-A-Date service date interface shall allow the Dater to edit the date's address. **(M)**
- Cupid Code Plan-A-Date service date interface shall allow the Dater to edit the date's partner. **(M)**
- Cupid Code Plan-A-Date service date interface shall allow the Dater to edit the date's start time. **(M)**
- Cupid Code Plan-A-Date service date interface shall allow the Dater to edit the date's date. **(M)**
- Cupid Code Plan-A-Date service date interface shall allow the Dater to edit the date's estimated end time. **(M)**
- Cupid Code Plan-A-Date service date interface shall allow the Dater to edit the date's prior notification with the default set to thirty minutes. **(M)**
- Cupid Code Plan-A-Date service date interface shall allow the Dater to disable the date's prior notification with the default set to enabled. **(M)**
- Cupid Code Plan-A-Date service date interface shall allow the Dater to delete a date. **(M)**
- Cupid Code Plan-A-Date service date interface shall allow the Dater to create a date. **(M)**
- Cupid Code Plan-A-Date service date interface shall allow the Dater to rate previous dates. **(M)**
- Cupid Code shall enable integration with Tinder API. **(C)**
- Cupid Code shall enable integration with Google Maps API to display real-time locations of Cupids. **(C)**
- Cupid Code shall enable integration with Google Maps API to display real-time locations of Daters. **(C)**
- Cupid Code shall allow Cupids to disable their location sharing, with the default set to enabled. **(C)**
- Cupid Code shall allow Daters to disable their location sharing, with the default set to enabled. **(C)**

## User Stories
### Cupid Stories
- As a Cupid, I want to filter job listings by distance, difficulty, or time required so that I can accept jobs that match my preferences and availability.
- As a Cupid, I want to see jobs prioritized by their expiration time so that I fulfill the most urgent requests first.
- As a Cupid, I want to view details about each job—including instructions, location, and payout—before accepting so that I can make informed decisions about which jobs to take.
- As a Cupid, I want to accept or decline available jobs directly through my app interface so that I can efficiently manage my workload.
- As a Cupid, I want to track my active, pending, and completed jobs in an organized dashboard so that I remain on top of my assignments.
- As a Cupid, I want to get notified when a Dater cancels a request before I make a purchase or start the job so that I do not waste time or resources.
- As a Cupid, I want to see an estimated arrival time for pickup or delivery tasks so that I can plan my route and meet deadlines.
- As a Cupid, I want to have access to my earnings and be able to transfer them to my bank account seamlessly so that I am paid promptly for my work.
- As a Cupid, I want my personal location to only be shared when necessary for active jobs so that my privacy is protected.
- As a Cupid, I want clear confirmation when my job actions (accept, complete, transfer earnings) have been processed successfully so that I trust the platform's reliability.
- As a Cupid, I want to see the location and instructions for each job assignment so that I can plan my route and understand the tasks required.
- As a Cupid, I want to get notifications for changes to active jobs, such as updated instructions or deadlines, so I can adjust quickly if plans change.
- As a Cupid, I want to receive reminders about upcoming jobs I’ve accepted so I never miss a pickup or delivery.
- As a Cupid, I want to decline jobs I’m unable to complete without penalty, so I can maintain a positive gig history while managing my workload.
- As a Cupid, I want the ability to report abusive or inappropriate behavior by Daters so that I feel safe while working.
- As a Cupid, I want the ability to report abusive or inappropriate behavior between Daters so that I can alert local authorities before problems arise.
- As a Cupid, I want app notifications to arrive in real time and be reliably delivered so I never miss an urgent update or Dater message.
- As a Cupid, I want to see which jobs offer higher payouts based on urgency or complexity so I can prioritize high-value work.
- As a Cupid, I want to add and verify multiple bank accounts so I can transfer earnings flexibly and securely.