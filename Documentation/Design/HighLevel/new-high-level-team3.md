# **New Cupid Code High Level Design**
* Team 3, *The Sinister Six*
* Sprint Leader: Tyson Buxton
* Sprint Followers: Benjamin Hickenlooper, Felix Jacob, Saxton Calvert, Garrett Woodhouse, and Reece Nielson

## Introduction
**Purpose:** TODO write out purpose of document

### Links
0. [Low Level Design](../LowLevel/new-low-level-team3.md)

### Table of Contents  
0. [Architecture](#0-architecture)
0. [Hardware Platform](#1-hardware-platform)
0. [User Interface](#2-user-interface)
0. [Internal Interfaces](#3-internal-interfaces)
0. [External Interfaces](#4-internal-interfaces)
0. [Security](#5-security)
0. [Risk Analysis](#6-risk-analysis)
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

# 5. Security

# 6. Risk Analysis
## Risks
## Mitigation Strategies

# 7. Data Design

# 8. Future Proofing