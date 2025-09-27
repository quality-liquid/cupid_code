# TODO put this section below under risk analysis
## Summary of Old Teams Risk Analysis
They talk about the risks of data interception or manipulation during transit in their [Client Section](./high_level_docs.md#client). The previous team also wrote a bit about the potential risk of using a Cloud-Provided server in the [Server Section](./high_level_docs.md#server) underneath [Hardware Platform Considerations](./high_level_docs.md#hardware-platform-considerations).

Otherwise the previous team's risk analysis is more implied than directly stated, through what they covered in terms of security measures they wanted to implement.

## Current Risk Analysis
### Giving AI more control
Our changes to the application will be giving more power to act to the AI which will enhance the user experience greatly, however can also come with risks to the integrity of the system should we not be careful.
* 
### Dating Life Information
The information we will be holding is extremely private
* Recorded date conversations.
* Very private life details of Daters; likes, dislikes, dating history, etc...information people will want kept very private, meaning there is a greater risk for bad actors targeting our system as they could use this information for convincing phishing scams, identity fraud, and possibly other malicious attacks.   


# TODO put this section below under Security
## Summary of Previous Teams Security Measures
### Encryption of Sensitive Information
* All sensitive information will undergo encryption before being stored in the database. Encrypted data will only be decrypted at the time of login, with implementation facilitated by Django and Node modules.
### Secure Handling of Chat Logs
* Chat logs between Daters and the AI will be safeguarded by individualized access-keys, stored via cookies.
### Location Privacy
* The location of a Dater will remain exclusively visible to them until a date crisis occurs. 
### Financial Transactions
* Credit/debit card transactions will be facilitated while adhering to PCI compliance standards.
### Frameworks and APIs
* Utilization of the latest frameworks will be prioritized, obsolete features will be addressed proactively. APIs with a strong reputation for security will be preferred.
### Account Protection
* A secure login system will be implemented, incorporating strong password requirements, favoring 12+ characters or 8+ characters with a mix of symbols, numbers, and capital letters. The exploration of a timeout system will be approached cautiously to avoid inconveniences during user activity. Consideration will be given to integrating Multi-Factor Authentication (MFA) for an additional layer of security.
### Data Flow
* Data flow will be encrypted using HTTPS. Utilization of AES for symmetric encryption and RSA for asymmetric encryption will be explored. User access to data will be restricted, providing Cupids with limited access for matchmaking purposes, while management retains broader access. Secure Session IDs and CSRF tokens will be implemented, with comprehensive data tracking.
### Database Security
* Password hashing within the database, regular data backups, and exploration of data encryption beyond passwords. 

### They did not implement
* A strong password requirement


## Current Security Measures
### Encryption of Sensitive Information
### Secure Handling of Chat Logs
### Location Privacy
* Dater location will only be accessed when necessary, necessary defined below as:
    * When a Dater creates a job for a Cupid they can pick for their location to be shared, or they can pick a location where the Cupid will meet them/drop off the item or perform the requested action. 
    * A Dater cancelling the job will revoke the live location permission for the Cupid who had accepted the job.
### Financial Transactions
* [PCI Standards Site](https://www.pcisecuritystandards.org/standards/)
* All applicable PCI Standards will be followed for the handling of User financial information.
    * Point-to-Point Encryption

### Frameworks and APIs
### Account Protection
* Forced strong password
* Forgotten password they enter secret info they gave at start
### Data Flow
### Database Security