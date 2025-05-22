# ISEE Exercise 5 Task 2 - Architectural Patterns

## Learning objective

Architectural patterns provide a sensible basic framework for various problems that occur repeatedly and need to be solved. The difficulty here is to recognize when it makes sense to use a pattern.

In this task, you are to deal with this again.

## Task - Architectural patterns in the wild

The lecture has already given some examples of the use of architecture patterns in prominent applications or software systems. Find another example and present it briefly. What are the main advantages of using this architecture pattern?

Note: You can also choose a completely different architecture pattern that was not presented in the lecture. In this case, however, you must briefly explain the pattern.

Answer: 

Microservice Architecture

This type of architecture has multiple smaller fully or partially independent applications running in tandem. Together they make up the working functionality of a fully featured application. Each sub-application or microservice has its own codebase and can be separately updated without affecting any of the other running microservices. This allows for parallel development, deployment and maintenance. 

This type of architecture allows for greater scalability. Each microservice can be easily cloned and spun up on new machince whenever the demand for that microservice's functionality is escalated. This also ensures that the application is never completely out of order if any single microservice crashes. Another advantage of this type of architecture is that it can allow the use of
different tech stacks to be used in the same application.

This architecture is not completely fool-proof. Due to the large number of independent microservices, it is more complicated to integrate all the microservices with each other. This also makes testing the application more difficult as test cases would need to account for functionality or logic that depends on other services. Microservice architecture also introduces more areas of vulternability. As each separate microservice would need to be independently secured. Especially if all the microservices don't share a common network or region.

