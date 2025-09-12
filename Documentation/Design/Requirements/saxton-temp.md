# CS3450 Fall 2025 Team 3 Requirements Document
## Summary of Previous Teams Requirements

## Functionality Requirements

### Rebranding Requirements
- Cupid Code shall provide a dark mode and light mode theme as part of the refreshed branding.

### Push Notification Requirements
- Cupid Code shall send push notifications to service users with reminders about planned dates.
- Cupid Code shall send push notifications to service users with conversation suggestions.
- Cupid Code shall send push notifications to service users with weather alerts.
- Cupid Code shall send push notifications to service users with date tips prior to a planned date.
- Cupid Code shall send push notifications to service users with date tips during a planned date.
- Cupid Code shall send push notifications to service users with date tips after a planned date.
- Cupid Code shall send push notifications to service users with encouragement to set up more dates.
- Cupid Code shall send push notifications to service users when an external service is successfully ordered for a planned date.
- Cupid Code shall send push notifications to gig workers with new job appearances.
- Cupid Code shall integrate with a texting service to send messages to users.
- Cupid Code shall integrate with an email service to send messages to users.
- Cupid Code shall allow the user to opt-in or opt-out of receiving specific types of push notifications.
- Cupid Code shall aggregate related notifications to avoid notification fatigue.
- Cupid Code shall allow the user to set preferences for notification timing and frequency.
- Cupid Code shall use multi-channel delivery for notifications, supporting push, SMS, and email.
- Cupid Code shall provide a notification center within the app for users to view all past notifications.
- Cupid Code shall prevent sending redundant notifications by deduplicating similar events.

### Agentic AI
- Cupid Code shall allow the service user to customize the autonomy of the AI in their preferences.
- Cupid Code shall allow the AI to edit a date's activity.
- Cupid Code shall allow the AI to edit a date's estimated cost.
- Cupid Code shall allow the AI to edit a date's address.
- Cupid Code shall allow the AI to edit a date's partner.
- Cupid Code shall allow the AI to edit a date's start time.
- Cupid Code shall allow the AI to edit a date's date.
- Cupid Code shall allow the AI to edit a date's estimated end time.
- Cupid Code shall allow the AI to delete a date.
- Cupid Code shall allow the AI to create a date.
- Cupid Code shall implement a jobs queue for managing third-party service requests and user-specific errands.
- Cupid Code shall allow the AI to place food orders via [x] API.
- Cupid Code shall allow the AI to arrange rides via [x] API.
- Cupid Code shall allow the AI to purchase event tickets via [x] API.
- Cupid Code shall allow the AI to fetch and recall user-specific preferences and history from the user database to personalize decisions and recommendations.
- Cupid Code shall allow the AI to adapt plans.

### Cloud Deployment
- Cupid Code shall be deployed using Azure

### Payment Processer APIs
- Cupid Code shall integrate with Stripe APIs to process payments.
- Cupid Code shall integrate with PayPal APIs to process payments.
- Cupid Code shall allow a service user to connect a bank account to their Cupid Code CupidCash funds using Stripe APIs.
- Cupid Code shall allow a service user to connect a bank account to their Cupid Code CupidCash funds using PayPal APIs.
- Cupid Code shall allow a service user to make a request to withdraw funds from a bank account to their CupidCash funds using Stripe APIs.
- Cupid Code shall allow a service user to make a request to withdraw funds from a bank account to their CupidCash funds using PayPal APIs.
- Cupid Code shall allow a service user to make a request to deposit funds to a bank account from their CupidCash funds using Stripe APIs.
- Cupid Code shall allow a service user to make a request to deposit funds to a bank account from their CupidCash funds using PayPal APIs.
- Cupid Code shall not allow a service user to make a request to deposit funds to a bank account from their CupidCash funds if the amount exceeds their current balance of CupidCash.
- Cupid Code shall not make use of microtransactions.

### Plan-A-Date Feature
- Cupid Code shall implement a Plan-A-Date service
- Cupid Code's Plan-A-Date service shall allow the service user to make a request to the AI to build a date based on past interests.
- Cupid Code's Plan-A-Date service date interface shall allow the service user to edit the date's activity.
- Cupid Code's Plan-A-Date service date interface shall allow the service user to edit the date's estimated cost.
- Cupid Code's Plan-A-Date service date interface shall allow the service user to edit the date's address.
- Cupid Code's Plan-A-Date service date interface shall allow the service user to edit the date's partner.
- Cupid Code's Plan-A-Date service date interface shall allow the service user to edit the date's start time.
- Cupid Code's Plan-A-Date service date interface shall allow the service user to edit the date's date.
- Cupid Code's Plan-A-Date service date interface shall allow the service user to edit the date's estimated end time.
- Cupid Code's Plan-A-Date service date interface shall allow the service user to edit the date's prior notification with the default set to thirty minutes.
- Cupid Code's Plan-A-Date service date interface shall allow the service user to disable the date's prior notification with the default set to enabled.
- Cupid Code's Plan-A-Date service date interface shall allow the service user to delete a date.
- Cupid Code's Plan-A-Date service date interface shall allow the service user to create a date.

## User Stories
