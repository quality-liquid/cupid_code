# **New Cupid Code High Level Design**
Team 3: *The Sinister Six*  
Sprint Leader: Tyson Buxton  
Team Members: Benjamin Hickenlooper, Felix Jacob, Saxton Calvert, Garrett Woodhouse, and Reece Nielson  

## Introduction
**Purpose:** TODO write out purpose of document

### Links
0. [Requirements](../Requirements/new-requirements-team3.md)
0. [Low Level Design](../LowLevel/new-low-level-team3.md)
### Table of Contents  
0. [Architecture](#0-architecture)
0. [Hardware Platform](#1-hardware-platform)
0. [User Interface](#2-user-interface)
0. [Internal Interfaces](#3-internal-interfaces)
0. [External Interfaces](#4-internal-interfaces)
0. [Risk Analysis](#5-risk-analysis)
0. [Security and Risk Mitigation](#6-security-and-risk-mitigation)
0. [Data Design](#7-data-design)
0. [Future Proofing](#8-future-proofing)


# 0. Architecture

# 1. Hardware Platform

### **Server**

Company-Owned Server
* Pros
    * Full Control
        * Owning a server provides complete control over hardware, software, and configurations, allowing for customization to meet specific needs.
    * Security
        * Companies can implement their security measures and protocols to safeguard sensitive data.
    * Cost Predictability
        * Once the server is purchased, there are no ongoing rental fees, providing cost predictability over the long term.
* Cons
    * High Initial Cost
        * Acquiring and setting up a server can involve significant upfront costs for hardware, software licenses, and infrastructure.
    * Maintenance Responsibility
        * The company is responsible for server maintenance, including updates, repairs, and hardware replacements.

Cloud-Provided Server
* Pros
    * Scalability
        * Cloud servers allow for easy scalability, enabling companies to adjust resources based on demand.
    * Cost Efficiency
        * Cloud services often operate on a pay-as-you-go model, reducing upfront costs and allowing companies to pay only for the resources they use.
    * Global Accessibility
        * Cloud servers can be accessed from anywhere with an internet connection, facilitating remote work and global collaboration.
* Cons
    * Dependency on Service Providers
        * Companies rely on the cloud service provider's infrastructure and services, which could lead to downtime or disruptions if the provider faces issues.
    * Security Concerns
        * While cloud providers implement robust security measures, there can be concerns about the security of sensitive data stored in the cloud.
    * Potential Cost Variability
        * While cloud services can be cost-efficient, usage spikes or unexpected charges may result in variable costs that are harder to predict.

**Server Decision**

Previously, there was a determination to host the server on local machines to prioritize cost-effectiveness, data security, and the ability to more easily conform to the specific requirements of the client. However, the client's objectives have now focused on attracting more customers, improving the artificial intelligence, and allowing for increased scalability as demand increases. Thus, a cloud provided server has become the option that would best be utilized. Though the local server operation came with its benefits, the abilities offered by a cloud provided server allow us to continue meeting security, customization, and cost needs while addressing new concerns and requirements the client has. To do this, the client and team decided to use Microsoft Azure for web hosting.

* Cost Considerations
    * Microsoft Azure has a free service with a pay-as-you-go model available. This allows for Cupid Code to maintain low costs as long as there is low demand. Once business and use begins to pick up speed, demand will increase but so will revenue. The costs upfront are low and the company is able to avoid immediately high overhead costs upon deployment.
* Global Access
    * Because the server will be hosted on a cloud provided server rather than a local device, more users can access and use the service. This allows for more daters, couples, and cupids. Microsoft Azure has reliable security features that ensure customer and employee data are kept confidential and protected.
* Maintenance Avoidance
    * Though this creates dependency on Microsoft as a service provider, it means the cost to run the server also includes the cost to maintain it. Developers extent of maintenance is to ensure the app runs smoothly on the server, the rest is handled by Microsoft. Microsoft's resources assure users that there will be few if any outages ever.

We conclude that the decision to host the server on Microsoft Azure is a careful result of assessing cost, access, security, and stability. This allows for developers to deliver an app that is reliable, accessible, and cost-effective while still providing excellent service for the client and a good experience for end users.

### **Client**

Our system prioritizes user flexibility by accepting requests from a wide array of Operating Systems and User-Agents. Whether users prefer iOS, Android, macOS, Windows, or various Linux Distros, and choose Chrome, Edge, Firefox, etc. as their preferred User-Agent, our platform is equipped to seamlessly accommodate their preferences.

The linchpin enabling this versatility is the implementation of HTTPS (Hypertext Transfer Protocol Secure). HTTPS plays a pivotal role in ensuring a secure and reliable connection between Cupid Code and our clients. This encryption protocol encrypts the data exchanged between the client and server, safeguarding it from potential threats or unauthorized access.

The use of HTTPS not only provides a secure communication channel, but also enhances the overall stability of connections. It establishes trust between the server and client, mitigating the risk of data interception or manipulation during transit. This commitment to security is fundamental in our approach, allowing users to engage with the Cupid code confidently, regardless of their chosen combination of Operating System and User-Agent.

It's worth noting that as long as users' chosen combination of User-Agent and Operating System supports HTTPS and JavaScript, our application will function seamlessly. This ensures a robust and reliable experience, reinforcing our dedication to providing a secure environment for all users.

The design and implementation made for the client end of the app, combined with the required features asked for by the client, lead us to believe that no design changes are needed.

# 2. User Interface

# 3. Internal Interfaces

# 4. External Interfaces

# 5. Risk Analysis
## Summary of Old Teams Risk Analysis
They talk about the risks of data interception or manipulation during transit in their [Client Section](./high_level_docs.md#client). The previous team also wrote a bit about the potential risk of using a Cloud-Provided server in the [Server Section](./high_level_docs.md#server) underneath [Hardware Platform Considerations](./high_level_docs.md#hardware-platform-considerations).

Otherwise the previous team's risk analysis is more implied than directly stated, through what they covered in terms of security measures they wanted to implement.

## Current Risk Analysis
### Giving AI more control
Our changes to the application will be giving more power to the AI which will enhance the user experience greatly, however this can also come with risks to the integrity of the system.
* The AI will be able to record conversations which will be stored in our database. This brings a new angle for Bad Actors to steal the private information of our clients, as we will have their written private information as well as their recorded converstations stored in our database.
* AI can be unpredictable at times, it could misunderstand instructions given by a Dater and potentially reveal private data or spend unauthorized funds when performing a task.   
### Dating Life Information
The information we will be holding is extremely private
* Private life details of Daters;
    * Likes
    * Dislikes
    * Dating history
    * Recorded conversations on dates
    * Chats with the AI assistant
* This is information people will want kept secure, meaning there will also be greater incentive for bad actors to target our system as they could use this information for convincing phishing scams, identity fraud, and possibly other malicious attacks.   

### Dependencies, Frameworks, and APIs
* There are already `npm` packages from the old teams project which contain critical security vulnerabilities. Without continual maintenance our application will become less secure as time goes on.  
![Terminal output for `npm install`](./images/prev-team-npm-vulnerabilities.png)

* There are many packages used for this project in its current state, each new package brings with it the bugs and vulnerabilites of said package. Having many packages creates a lot to keep track of which makes it more difficult to check used packages for vulnerabilties or to keep all packages up to date and still working with the application.
    * 180 packages currently are used for the client.  
    * 75 python packages currently are installed for the Poetry environment. 

* There is a similar risk with using APIs and Frameworks as with using other's packages.
    * There must be continual maintenance work to stay up to date on the APIs, ensuring any changes in how one interfaces are implemented to keep the application functioning, research must be done to ensure the APIs used are reputable. In addition, by relying on API's should there service go down for any reason, our applications related service will also be down.
    * For working with different Frameworks the code base must be kept up to date on a likely changing Framework interface to keep the application running and secure as time goes on. There is also a risk that the Framework could lose popularity over time, and thereby the developers stop working on it, leaving vulnerabilities unpatched and bugs unfixed.


# 6. Security and Risk Mitigation
## Summary of Previous Teams Security Measures
The previous team focused on the following items in their [Security Considerations](./high_level_docs.md#security-considerations)
* Encryption of Sensitive Information
* Secure Handling of Chat Logs
* Location Privacy
* Financial Transactions
* Frameworks and APIs
* Account Protection
* Data Flow
* Database Security
### They did not implement
* A strong password requirement
* 2 factor authentication

## Sinister Six Security Measures and Risk Mitigations
Much of our decided security measures are the same or similar to those of the previous team as our proposed changes and features still bring about many of the same  security risks to be mitigated. Though some of the sections were consolidated so as not to repeat information.

### Location Privacy
* Dater location will only be accessed in the following circumstances:
    * When a Dater creates a job for a Cupid, the Dater can pick for their location to be shared, or they can pick a location where the Cupid will meet them/drop off the item or perform the requested action. 
    * A Dater cancelling the job will revoke the live location permission for the Cupid who had accepted the job.
    * Managers will be able to see general locations for Daters, the closest city to the Dater. 

### Financial Transactions
All applicable [PCI Standards](https://www.pcisecuritystandards.org/standards/) will be followed for the handling of User financial information.
* Point-to-Point Encryption with HTTPS for sending and recieving financial information.
* Encryption of all user's financial payment information stored in our database.
    * Credit Card number, expiration date, CVV code.
    * Name and Billing address.
    * Direct bank account information (alternative to credit card).

### Dependencies, Frameworks, and APIs
* We will go through the `npm` and `python` dependencies removing any we can confidently say are not needed. Thus removing unnecessary risk, and allowing for more focus on vetting the dependencies which are truly needed. 
* Research on new vulnerabilities discoverd, or updates in general in the Frameworks we use will need to be done periodically, and then the subsequent work to update our version of the Frameworks to close said vulnerabilities and ensure we stay capable of running will be done.
* The APIs we choose will be researched and confirmed to have a strong reputation for security and reliability.

### Account Protection
* A strong password will be required for registration
    * At least 10 characters.
    * Containing at least one number.
    * At least one special character.
    * At least one capital letter.
* Session token in database will be invalidated upon logout, and will be invalidated after 14 days, requiring resigning in.
* These measures will help to safeguard User's data; chatlogs, info, history, etc...

### Data Flow
* HTTPS will be used to encrypt all traffic incoming and outgoing.
* CSRF tokens with session IDs faciliated by the Django framework will be used to ensure proper authentication and authorization.
* Daters will only have access to their personal information and the name and photo of Cupids who accept their jobs.
* Cupids will be able to see only the information the Daters give to them and permissions for said information will be revoked upon job completion, Cupid dropping the job, or job timeout. 
* Management will retain broader access to data for statistics and management of users (banning bad users).

### Database Security
* Passwords will be stored as hashes.
* All access to database will go through security middleware for authentication.
* We are going with Azure Cloud Service to host our application and database. Microsoft is very large coorporation with years of experience, large talent pools, and many resources. We are confident their services will be up to the latest security standards and will continue to be maintained by them to stay secure as the years go on.

### AI Security
* We will make a summary card that appears to the Dater, showing everything the AI intends to do after the User has requested and action. This will allow the Dater to confirm that the AI understood them correctly before the AI immediately acts (buying tickets, sending messages, hiring cupids, etc...) to ensure Dater privacy, security, and satisfaction with the application.
* All recorded information will be encrypted when stored, only accessible by the Dater and their AI.


# 7. Data Design

# 8. Future Proofing