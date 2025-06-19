# ISEE Exercise 8 - Testing Basics

Written By: Suvansh Shukla (matriculation number: 256245)

## Learning Objective

In the lecture, the basics and 4 possible test phases in the V-model were discussed. These are repeated here using a practical example.

## Task - Test phases

You are responsible for a large software project in which an intelligent signalling and point setting system for long-distance rail transport is being developed. The system comprises several levels from a graphical user interface to drivers for controlling the mechanical elements.

This project is based on the V-model and the implementation is largely complete. Testing of the software should now begin.

- Name the four test phases presented in the lecture and briefly explain the purpose of each phase.
- different strategies can be used in the second test phase. Which of these strategies is best suited to the software project? Briefly explain the strategy you have chosen and explain why other strategies are unsuitable.

### Four Test Phases 

1. **Unit Test**: used to determine the error state clearly. Each component is tested individually 
2. **Integration Test**: used to find errors in the interfaces and interactions between the components. Components are integrated into subsystems. This is performed by developers, testers, Integration teams.
3. **System Test**: Used to determine if the system meets the requirements. This testing is done from the user's perspective, as most functions can only be used in a fully integrated system.
4. **Acceptance Test**: This is testing is done to create trust in the product rather than finding errors. This includes the customer's view and opinion. This is the only testing phase that directly involves the customer and is carried out at the customer's premises in the new system environment.

### Integration testing strategy that best suits the project

I suggest using bottom-up integration testing for the project. I suggest this strategy due to the following reasons:

1. Issues can be identified earlier stages when things are still relatively less complicated. This is important because the high degree of complexity of a signalling and point setting system.

2. Issues can be more easily addressed, especially since we are doing the testing at relatively primitive stages with fewer variables to keep in mind.

3. Resolving smaller issues then combining modules into larger ones allows us the project to have a more stable foundation. This is helpful as we move to test complex interactions between multiple modules.

4. This strategy also allows us to test modules in parallel. We can independently test and debug modules without depending on other modules.

Other strategies aren't as versatile and suitable because of the following reasons:

- The Top-down strategy would require putting modules together earlier in the testing stage, this can lead to more errors and conflicts. It may also require replacement of low level modules with dummies not to mention it would be more expensive.
- Ad-hoc would require both dummies and drivers. It would also be harder to organize and track which modules require re-testing and which can proceed to the next stages. It may also lead to more re-working of modules at later stages.
- Big bang wouldn't be appropriate as it would lead to too many errors especially at a very late stage of the project, this bringing about delays and would also be harder to debug (not being sure which module caused the errors).

