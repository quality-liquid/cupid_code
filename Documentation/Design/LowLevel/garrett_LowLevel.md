[Backend Summary]
[Resources for the Backend]
[Performance]
[Django Project Structure]
[Django Admin]

# Backend Summary (Revisit this after everything else is done)
    The backend will be built using Django and the Django REST Framework. As a result much of the needed security is already implemented. A majority of the work will be in the models, views, and serializers. The models will be the database, the views will be the API, and the serializers will be the conversion of the models to JSON and vice versa. The frontend will communicate with the backend using HTTP GET and POST requests. The backend will respond with JSON data. This will be made easy by the Django Rest Framework. Mapping what endpoints the frontend needs is helpful for the backend to know what to build. This will be done in the URL Mapping section.
        Additionally, the data will be stored in Azure Cloud to make it more scalable, accessible, and secure.
        One more thing to note is that the Agentic AI will have access to communicate with both the back end and the front end. It will be expected to pull data from the database, and then transport it and use it automatically.

# Resources for the Backend 
We added additional links to the Azure Cloud Documentation, LM studio documentation and the LangChain Documentation.

[Django Rest Framework Quickstart](https://www.django-rest-framework.org/tutorial/quickstart/)   
[Django Rest Framework API Reference](https://docs.djangoproject.com/en/5.0/ref/)  
[Django Rest Framework Serializers](https://www.django-rest-framework.org/api-guide/serializers/)  
[Django Rest Framework Views](https://www.django-rest-framework.org/api-guide/views/)  
[Django Rest Framework Permissions](https://www.django-rest-framework.org/api-guide/permissions/)  
[Django Rest Framework Authentication](https://www.django-rest-framework.org/api-guide/authentication/)  
[Azure Cloud Documentation](https://learn.microsoft.com/en-us/azure/?product=popular)  
[LM Studio Documentation](https://lmstudio.ai/docs/app)  
[LangChain Agentic AI documentation](https://python.langchain.com/docs/tutorials/agents/)


# Performance
The following will determine the performance of the backend:
### Largest Changes from the Previous Team
The majority of the changes in this section have to do with updating the document to show that we are using Azure Cloud instead of SQL lite and that we are going to be using an agentic AI instead of a regular AI model.


- Django
    - Provides a lot of performance optimizations out of the box.
    - Mature framework that has been optimized for performance over many years.
    - Used by many large websites and can handle a lot of traffic.
    - Synchronous framework, which means it can handle a lot of requests at once.
    - Built-in caching system that can help improve performance.
    - Built-in ORM that can help optimize database queries.
    - Built-in middleware system that can help optimize requests.
- Django Rest Framework
    - Built on top of Django and inherits many of its performance optimizations.
    - Designed to be fast and efficient.
    - Used by many large websites and can handle a lot of traffic.
    - Built-in caching and throttling systems that can help improve performance.
    - Built-in serializers that can help optimize data serialization.
    - Built-in viewsets and routers that can help optimize request handling.
- Hardware
    - We plan to run the backend on the cloud. This will allow us to have a more accessible dataset and also more resources on our personal hardware.
    - We will need to monitor the hardware to ensure that it is running optimally and make any necessary changes to improve performance.
    - We will be running our AI agent locally from LM Studio and using frameworks such as LangChain. This will allow us more control over the AI, but we will need to be cognizant of how this might affect performance and how we will scale this as the product grows toward deployment.
- Network
    - The internet service provider will need to be able to handle the traffic that we are generating.
    - We will need to monitor the network to ensure that it is running optimally and make any necessary changes to improve performance.
    - Ideally, we will have servers in multiple locations to reduce latency and improve performance.
- Database
    - The default database is Azure Cloud. This will allow us to offload some work and improve performance.
    - Additionally, little data is being stored about each user. This will help keep the database small and fast.
- Code
    - How we write the backend will also affect performance.
    - We will need to write efficient code optimized for performance.
    - We won't be using recursion to avoid stack overflow errors.
    - We will make sure not to use nested loops to avoid performance issues.
    - Luckily, this type of application is not very performance intensive. We are not doing any heavy calculations or processing large amounts of data.
- Testing
    - Our tests will help us identify performance issues. If testing a feature is slow, we will need to optimize it.
    - We will use tools like Django Debug Toolbar to help identify performance issues.
- Security
    - Security is important, but sometimes it comes at a cost to performance.
    - We will need to balance security with performance.




# Django Project Structure
This is what our project structure will look like:

- _server/
    - _server/ - Main project settings.
        - settings.py - Main settings file.
        - urls.py - Main url file.
        - wsgi.py - Web server gateway interface.
    - api/ - App for the api.
        - admin.py - Admin configuration.
        - apps.py - App configuration.
        - geodata/ - Used by GeoLite to look up location by IP (NOT THIS)
        - migrations/ - Migrations for the api app.
        - models.py - Define the models.
        - serializers.py - Define the serializers.
        - tests.py - Write unit tests.
        - urls.py - Map the urls to the views.
        - views.py - Define and implement the views.
    - core/
        - admin.py - Admin configuration.
        - apps.py - App configuration.
        - middleware.py - Captures requests for static files and redirects to Vue server
        - static/ - Contains some images
        - templates/ - Contains the base template
    - manage.py - Command line utility for managing the project.
    - Azure cloud (Database)


# Django Admin
The Django admin site adds the possibility to have admin accounts with levels of management and control. The main functions this account can provide are the following:

    - Easy creation, management, and deletion of user accounts
    - Easy creation, management, and deletion of data
    - Easy adjustment to permissions on user accounts
    - Ability to export data (if needed)
    - Logging and history of changes made to data
There are some concerns with the admin site and admin accounts:

    - Security concerns
        - Admin accounts are a prime target for hackers
        - Admin accounts could be used to access sensitive data
        - Admin accounts could be used to modify data in a way that could be harmful
        - Admin accounts could be used to delete data
        - Admin accounts could be used improperly or maliciously
    - Resource usage
        - Admin accounts take a lot of resources to maintain
        - Admin accounts could be used to do intensive work that could slow down the software
The Django admin site will be used to create the initial Manager accounts to manage the site.

While the admin site is a powerful tool, it is not the best tool for day-to-day operations. While the server is in production, the admin site will be disabled. Instead, the API will be used to manage the data.