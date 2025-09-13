# CS3450 Fall 2025 Team 3 Requirements Document
## Summary of Previous Teams Requirements

## Must Have Requirements

### Rebranding Requirements
- Cupid Code shall provide a dark mode and light mode themes as part of the refreshed branding.

### Push Notification Requirements
- Cupid Code shall send push notifications to Daters with reminders about planned dates.
- Cupid Code shall send push notifications to Daters with conversation suggestions.
- Cupid Code shall send push notifications to Daters with weather alerts.
- Cupid Code shall send push notifications to Daters with date tips prior to a planned date.
- Cupid Code shall send push notifications to Daters with date tips during a planned date.
- Cupid Code shall send push notifications to Daters with date tips after a planned date.
- Cupid Code shall send push notifications to Daters with encouragement to set up more dates.
- Cupid Code shall send push notifications to Daters when a service is successfully ordered for a planned date.
- Cupid Code shall send push notifications to Cupids with new job appearances.
- Cupid Code shall integrate with a texting service to send messages to Daters.
- Cupid Code shall integrate with a texting service to send messages to Cupids.
- Cupid Code shall integrate with an email service to send messages to Daters.
- Cupid Code shall integrate with an email service to send messages to Cupids.
- Cupid Code shall allow a Dater to opt-in or opt-out of receiving specific types of push notifications.
- Cupid Code shall allow a Cupid to opt-in or opt-out of receiving specific types of push notifications.
- Cupid Code shall aggregate related notifications to avoid notification fatigue.
- Cupid Code shall allow a Dater to set preferences for notification timing and frequency.
- Cupid Code shall allow a Cupid to set preferences for notification timing and frequency.
- Cupid Code shall use multiple methods of delivery for notifications supporting push, SMS, and email.
- Cupid Code shall provide a notification center within the app for Daters to view all past notifications.
- Cupid Code shall provide a notification center within the app for Cupids to view all past notifications.
- Cupid Code shall prevent sending redundant notifications by deduplicating similar events.
- Cupid Code shall integrate with the Weather Channel API to provide weather forecast data.

### Agentic AI
- Cupid Code shall allow the Dater to customize the autonomy of the AI in their preferences.
- Cupid Code shall allow the AI to edit a date's activity.
- Cupid Code shall allow the AI to edit a date's estimated cost.
- Cupid Code shall allow the AI to edit a date's address.
- Cupid Code shall allow the AI to edit a date's partner.
- Cupid Code shall allow the AI to edit a date's start time.
- Cupid Code shall allow the AI to edit a date's date.
- Cupid Code shall allow the AI to edit a date's estimated end time.
- Cupid Code shall allow the AI to delete a date.
- Cupid Code shall allow the AI to create a date.
- Cupid Code shall implement a jobs queue for managing third-party service requests and Cupid-specific errands.
- Cupid Code shall allow the AI to place food orders via UberEats API.
- Cupid Code shall allow the AI to arrange rides via Uber API.
- Cupid Code shall allow the AI to purchase movie tickets via Megaplex API.
- Cupid Code shall allow the AI to fetch and recall Dater-specific preferences and history from the Dater database to personalize decisions and recommendations.
- Cupid Code shall allow the AI to cancel previously arranged food orders via UberEats API.
- Cupid Code shall allow the AI to cancel previously arranged rides via Uber API.
- Cupid Code shall allow the AI to cancel previously arranged movie tickets via Megaplex API.
- Cupid Code shall allow the AI to access weather forecast data.

### Cloud Deployment
- Cupid Code shall be deployed using Azure

### Payment Processer APIs
- Cupid Code shall integrate with Stripe APIs to process payments.
- Cupid Code shall integrate with PayPal APIs to process payments.
- Cupid Code shall allow a Dater to connect a bank account to their Cupid Code CupidCash funds using Stripe APIs.
- Cupid Code shall allow a Dater to connect a bank account to their Cupid Code CupidCash funds using PayPal APIs.
- Cupid Code shall allow a Dater to make a request to withdraw funds from a bank account to their CupidCash funds using Stripe APIs.
- Cupid Code shall allow a Dater to make a request to withdraw funds from a bank account to their CupidCash funds using PayPal APIs.
- Cupid Code shall allow a Dater to make a request to deposit funds to a bank account from their CupidCash funds using Stripe APIs.
- Cupid Code shall allow a Dater to make a request to deposit funds to a bank account from their CupidCash funds using PayPal APIs.
- Cupid Code shall not allow a Dater to make a request to deposit funds to a bank account from their CupidCash funds if the amount exceeds their current balance of CupidCash.
- Cupid Code shall display transaction history within the Dater's account dashboard.
- Cupid Code shall display transaction history within the Cupid's account dashboard.
- Cupid Code shall allow a Dater to set a default payment method for processing payments made by the Dater.
- Cupid Code shall allow a Dater to set a default payment method for processing payments made by the AI.
- Cupid Code shall not make use of microtransactions.

### Plan-A-Date Feature
- Cupid Code shall implement a Plan-A-Date service
- Cupid Code Plan-A-Date service shall allow the Dater to make a request to the AI to build a date based on past interests.
- Cupid Code Plan-A-Date service date interface shall allow the Dater to edit the date's activity.
- Cupid Code Plan-A-Date service date interface shall allow the Dater to edit the date's estimated cost.
- Cupid Code Plan-A-Date service date interface shall allow the Dater to edit the date's address.
- Cupid Code Plan-A-Date service date interface shall allow the Dater to edit the date's partner.
- Cupid Code Plan-A-Date service date interface shall allow the Dater to edit the date's start time.
- Cupid Code Plan-A-Date service date interface shall allow the Dater to edit the date's date.
- Cupid Code Plan-A-Date service date interface shall allow the Dater to edit the date's estimated end time.
- Cupid Code Plan-A-Date service date interface shall allow the Dater to edit the date's prior notification with the default set to thirty minutes.
- Cupid Code Plan-A-Date service date interface shall allow the Dater to disable the date's prior notification with the default set to enabled.
- Cupid Code Plan-A-Date service date interface shall allow the Dater to delete a date.
- Cupid Code Plan-A-Date service date interface shall allow the Dater to create a date.
- Cupid Code Plan-A-Date service date interface shall allow the Dater to rate previous dates.

## User Stories
