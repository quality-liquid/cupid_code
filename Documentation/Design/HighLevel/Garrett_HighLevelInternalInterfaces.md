# Previous External Interfaces
### Considered API's
* AI API (Microsoft Copilot)
* Location API (Geolocation)
* Speech To Text API (pyttsx3)
* Text and Email notifications API (Twilio) 
* Nearby Shops API (yelpapi)

# Sinister 6 External Interfaces

### API's 
- AI API (**LM Studio**)
    - In the existing code, they planned to use Microsoft Copilot at a high level, then ended up using gpt2 in their low level planning and in implementation. We are going to use LM Studio as it is easier, faster, and will give us more flexibility as we continue the project. Additionally as we plan to make a reactive agent, we believe that LM Studio will provide more opportunities to grow.
- Location API (**GeoLite2**)
- Text To Speech API (pyttsx3)
- Text and Email notifications API (Twilio) 
- Nearby Shops API (yelpapi)

### How to manage these API's
- Modular Code Design
    - Each API is used for a specific purpose. We will keep each API isolated in only the file(s) where they are needed.
    - We will separate the API calls from the direct codebase where it impacts in modules so that if we need to change an API it will be simple with minimal changes.
- Document Management
    - We will keep clear instructions on how to use the API's by linking the documentation for each one in our documentation pages.
    - We will have a log of changes and our experience with each API.
    

