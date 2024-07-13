The project is a django REST api service using PostgreSQL with authorization and authentication using OpenIDConnect via onelogin.com.
The service features two end-points: /customers and /orders through which one can upload(POST) new records and view(GET) existing records.
Authentication and authorization is implemented using OpenIDConnect via onelogin.com. providing security to the apis.
When an order is added to the orders api, an SMS is sent to a customer's phone number using Africa's Talking gateway and sandbox.
CI + automated CD is implemented using GitHub Actions and render.com's deploy hook URL where the service is deployed.
The service is hosted on render.com with the following URL: https://render-django-assignment.onrender.com/.
The project features very minimal UI thus interaction with the service is recommended via Postman or any other API testing tools.


