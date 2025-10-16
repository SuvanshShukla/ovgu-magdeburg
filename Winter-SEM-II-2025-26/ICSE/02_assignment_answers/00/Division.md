# ICSE Exercise 0 - Assignment 3

Author: Suvansh Shukla  
Matriculation Number: 256245    

## Task 1

**Program code**: Program code is the runnable and executable code written to solve a problem

**Pseudo code**: Pseudo code are the statements written to represent the different steps required to execute in an algorithm to solve a problem. Pseudo code is usually syntactically incorrect and only servers to make logic more understandable.

## Task 2

Division Algorithm:
  *Input:* dividend and divisor, where divisor cannot be 0
  *Output:* Quotient

  BEGIN
    initialize counter variable to 0
    WHILE(dividend >= divisor)
       subtract divisor from dividend
       increment counter
    ENDWHILE
    RETURN counter value
  END PROCESS


Explanation: The algorithm ends for all values the moment the dividend is smaller than the divisor.

Altered Division Algorithm (for getting Remainder):
    *Input:* dividend and divisor, where divisor cannot be 0
    *Output:* Remainder

  BEGIN
    initialize counter variable to 0
    initialize remainder variable to 0
    WHILE(dividend >= divisor)
       subtract divisor from dividend
       save result of subtraction into remainder variable
       increment counter
    ENDWHILE
    RETURN remainder value
  END PROCESS

