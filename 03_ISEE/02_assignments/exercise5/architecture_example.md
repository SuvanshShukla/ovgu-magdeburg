# ISEE Exercise 5 - Task 2 - Architectural Patterns 

Written by Suvansh Shukla   
Matriculation Number: 256245

## Microservice Architecture

This type of architecture has multiple smaller fully or partially independent applications running in tandem. Together they make up the working functionality of a fully featured application. Each sub-application or microservice has its own codebase and can be separately updated without affecting any of the other running microservices. This allows for parallel development, deployment and maintenance. 

This type of architecture allows for greater scalability. Each microservice can be easily cloned and spun up on new machince whenever the demand for that microservice's functionality is escalated. This also ensures that the application is never completely out of order if any single microservice crashes. Another advantage of this type of architecture is that it can allow the use of
different tech stacks to be used in the same application.

This architecture is not completely fool-proof. Due to the large number of independent microservices, it is more complicated to integrate all the microservices with each other. This also makes testing the application more difficult as test cases would need to account for functionality or logic that depends on other services. Microservice architecture also introduces more areas of vulternability. As each separate microservice would need to be independently secured. Especially if all the microservices don't share a common network or region.

