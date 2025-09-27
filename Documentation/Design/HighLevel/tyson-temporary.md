# TODO put this section below under risk analysis
## Summary of Old Teams Risk Analysis
They talk about the risks of data interception or manipulation during transit in their [Client Section](./high_level_docs.md#client). The previous team also wrote a bit about the potential risk of using a Cloud-Provided server in the [Server Section](./high_level_docs.md#server) underneath [Hardware Platform Considerations](./high_level_docs.md#hardware-platform-considerations).

Otherwise the previous team's risk analysis is more implied than directly stated, through what they covered in terms of security measures they wanted to implement.

## Current Risk Analysis
### Giving AI more control
Our changes to the application will be giving more power to the AI which will enhance the user experience greatly, however this can also come with risks to the integrity of the system should we not be careful.
* AI can be unpredictable at times, it could misunderstand instructions given by a Dater and potentially reveal private data or spend unauthorized funds.   
### Dating Life Information
The information we will be holding is extremely private
* Private life details of Daters;
    * Likes
    * Dislikes
    * Dating history
    * Recorded conversations on dates
    * Chats with the AI assistant
* This is information people will want kept secure, meaning there will also be greater incentive for bad actors to target our system as they could use this information for convincing phishing scams, identity fraud, and possibly other malicious attacks.   


# TODO put this section below under Security
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

## Sinister Six Security Measures
Much of our decided security measures are the same or similar to those of the previous team as our proposed changes and features still bring about many of the same  security risks to be mitigated.

### Encryption of Sensitive Information
### Secure Handling of Chat Logs
### Location Privacy
* Dater location will only be able to be accessed when necessary, necessary defined below as:
    * When a Dater creates a job for a Cupid, the Dater can pick for their location to be shared, or they can pick a location where the Cupid will meet them/drop off the item or perform the requested action. 
    * A Dater cancelling the job will revoke the live location permission for the Cupid who had accepted the job.
### Financial Transactions
All applicable [PCI Standards](https://www.pcisecuritystandards.org/standards/) will be followed for the handling of User financial information.
* Point-to-Point Encryption with HTTPS for sending and recieving financial information.
* Encryption of all user's financial payment information stored in our database.
    * Credit Card number, expiration date, CVV code.

### Frameworks and APIs
### Account Protection
* A password with at least 10 characters; containing at least one number, at least one special character, and at least one capital letter.
### Data Flow
* HTTPS will be used to encrypt all traffic incoming and outgoing.
* CSRF tokens with session IDs faciliated by the Django framework will be used to ensure proper authentication and authorization.
* Daters will only have access to their personal information and the name and photo of Cupids who accept their jobs.
* Cupids will be able to see only the information the Daters give to them and permissions for said information will be revoked upon job completion, Cupid dropping the job, or job timeout. 
* Management will retain broader access to data for statistics and management of users (banning bad users).
### Database Security
* Passwords will be stored as hashes.
* All access to database will go through security middleware for authentication.
### AI Security
We will make a summary card that appears to the Dater, showing everything the AI intends to do after the User asked it to do something. This will allow the Dater to confirm the AI understood them correctly before the AI immediately acts buying tickets, sending messages, hiring cupids, etc...to ensure Dater privacy, security, and satisfaction with the application.