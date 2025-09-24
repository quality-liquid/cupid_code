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

Previously, there was a determination to utilize hosting the server on local machines to prioritize cost-effectiveness, data security, and the ability to more easily conform to the specific requirements of the client. However, the client's objectives have now focused on a more business-like model and advancing this app to be utilized by more people. Thus, a cloud provided server has become the option that would best be utilized. Though the local server operation came with its benefits, the abilities offered by a cloud provided server allow us to continue meeting security, customization, and cost needs while addressing new concerns and requirements the client has.

* Cost Considerations
    * Though recurring costs of data storage, bandwidth, and usage-related fees that could be unpredicatble, the use of a cloud server system allows for efficiency in avoiding paying for resources that aren't utilized. This is less feasible on a local server because all services must be run locally which consumes resources and does not allow for much growth in the user base. As it is an ongoing expense, it drives incentive for continued business growth by providing a need for consistent funding.
* Global Access
    * TODO: Because the server will be hosted on a cloud provided server rather than a local device, more users can be found.
* Maintenance Avoidance
    * TODO: We don't have to maintain it, someone else does. Though this means we're victim to them falling down, the service has enough other clients that any sort of outage will be more problematic than helpful.

TODO: Conclude acknowledging security and market literature pointing out that this will be fine.

# 2. User Interface

# 3. Internal Interfaces

# 4. External Interfaces

# 5. Security

# 6. Risk Analysis
## Risks
## Mitigation Strategies

# 7. Data Design

# 8. Future Proofing