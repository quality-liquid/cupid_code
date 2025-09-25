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
* Data flow will be encrypted using HTTPS, with specific attention given to framework capabilities. Utilization of AES for symmetric encryption and RSA for asymmetric encryption will be explored. User access to data will be restricted, providing Cupids with limited access for matchmaking purposes, while management retains broader access. Secure Session IDs and CSRF tokens will be implemented, and comprehensive tracking of data flow will be logged and stored.
### Database Security
* Password hashing within the database, regular data backups, and exploration of data encryption beyond passwords, utilizing AES/RSA for optimum protection, will be priorities in maintaining the security and resilience of the database.


### What they did do
* Passwords were hashed in the database
### They did not do
* No strong password requirement implemented

## Security Measures
### Encryption of Sensitive Information
### Secure Handling of Chat Logs
### Location Privacy
### Financial Transactions
* [PCI Standards Site](https://www.pcisecuritystandards.org/standards/)
### Frameworks and APIs
### Account Protection
* Forced strong password
* Forgotten password they enter secret info they gave at start
### Data Flow
### Database Security


# TODO put this section below under risk analysis
## Summary of Old Teams Risk Analysis

## Questions TODO delete this later
* [] What is AES? Symmetric vs Asymmetric encryption?