## Non-Functional Requirements:

### Security:

- Encrypting data at rest and in transit
- Only Daters, Cupids, and Managers with a valid login can enter the system. 
    - A Two-Factor authentication will allow Users and Cupids to recover their login information
    - Managers will need to use Two-Factor Authentication to login every time. 
- User data will only be available to those who are authorized to view it.
    - Cupids can only see the minimum of what they need to help the User on a date, after accepting the job.
    - Managers will see general data trends but not specific User information
 - Data Integrity
    - The system must not corrupt data, even in the event of a network outage.



### Scalability:


- The system will be scalable to accommodate a growing user base.
- The system will be built upon itself so the addition of new features will not require significant changes to existing architecture. 



### Availability:

- The system will run on all webpages, with a **webpage mobile version**
- A high level of uptime is crucial, with a target of 99.9% uptime to minimize disruptions and ensure continuous availability
to users.



### Performance:

The platform will have low latency communication between Daters, Cupids, and the AI.
- Login should take less than 3 seconds
- Once in Cupid Code, the app should run smoothly and with minimal delays
    - No response time should exceed 1 second while on the website. Ex.switching pages, buying Cupid Cash, submitting a form.




### Usability:

The user interfaces for Daters, Cupids, and Managers will be intuitive and user-friendly.
- Learnability: The website will be intuitive allowing even new users to navigate the website without training
- Efficiency: A task that is performed frequently should take a maximum of three clicks to complete.


### Compatibility:


- It will be fully functional on Google Chrome, Mozilla Firefox, and Safari.
- The website should work on most screen sizes and device options. 



### Compliance:

- Our website will comply with the General Data Protection Regulation (GDPR), and the California Consumer Privacy Act (CCPA). 
- The system will follow the Web Content Accessibility Guidelines (WCAG)

- ACM codes of ethics are applied to keep confidentiality of Daters and Cupids.

### Documentation:

Comprehensive and clear documentation will be available for Daters, Cupids, and Managers via user manuals for each individual user type.

### Maintainability
- Modularity
    - The system must be organized into separate modules by function. 
- Bug Reports
    - Bugs should be fixed within 24 hours of a bug being reported


## Non-Functional Requirements for the Server
### Performance
- The server should be able to handle at least 1,000 concurrent orders per second during peak times to meet high demand.
- API response times should be below 300 milliseconds for standard requests to ensure a fast and responsive system.
### Scalability
-  The server’s architecture should support horizontal scaling, meaning it can handle an increasing number of users by
adding more resources, such as load balancers.
- It should be able to dynamically scale up or down based on traffic surges, especially during special events or promotions.
### Availability 
- The server should have an uptime of 99.99%, with robust failover systems in place to handle any unexpected outages. 
- Regular backups and disaster recovery measures should be implemented to prevent data loss in case of a server failure.
### Security 
- Passwords must be encrypted both in transit and in the database to protect sensitive information. 
- The server must comply with industry standards when handling payment data. 
- Regular security patches and continuous monitoring should be implemented to detect and mitigate potential threats.
### Maintainability
- The server architecture should be modular, allowing for easier updates and modifications without disrupting service.
Monitoring and Logging
- Comprehensive logging must be implemented to track user activities, server performance, and order transactions for
future analysis and troubleshooting.
- Real-time monitoring tools should be in place to detect issues with server load, latency, or failures, allowing for prompt
response to any problems.
Latency 
- The system should be designed to ensure low latency for real-time order updates and status tracking, providing users
with a seamless experience.
### Compliance
- The server must comply with data protection regulations, such as GDPR, if the business serves customers in regions
with strict data privacy laws.
- Proper management of user consent should be implemented for data collection and usage, ensuring compliance with
legal requirements.