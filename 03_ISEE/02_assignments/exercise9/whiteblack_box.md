# ISEE Exercise 9 - Task

## Task - WhiteBox test

A white box test is to be carried out for the following function.

```java
public static boolean isNarcissistic(int n) {
  int length = String.valueOf(n).length();
  int result = 0;
  int initial = n;
  while (n > 0) {
    int remainder = n % 10;
    result += Math.pow(remainder, length);
    n /= 10;
  }
  if (result == initial) {
    return true;
  } else {
    return false;
  }
} 
```

### Create the control flow graph of the function `isNarcissistic`.

![Control Flow Graph for the function](./whiteblack_box.svg)

### What is the minimum number of test cases required to perform the coverage tests `C0` and `C1` ?

For `C0`-test, you would need at least 2 test cases.    
For `C1`-test, you would need at least four test cases.     

For `C1` the tests would be `while` - `true` & `false`, then `if` - `true` & `false`.

### State the logical and one specific test case as well as their executed path!

The logical test case would be taking a number like 0.

The test would flow like this:
All variables would be initialized, then the code wouldn't enter the while loop because 0 is not greater than 0.
Then the code would enter the if block on line 10 because result is equal to initial (since 0 is equal to 0).   
Then finally we would return `true` and the execution of the test would end.

Path = (1, 2-4, 5, 10, 11)

## Task - BlackBox test 

You want to test the method `String qualityCheck(double weight)` with the black box test procedure. You use the following code for this:

```java
final static double TARGET_WEIGHT_IN_GRAMS = 100;
public static String qualityCheck(double weight){
	//The code of this method is unknown
}
```

In a packaging system for cheese, it must be checked whether the correct amount of cheese ends up in each pack.
The `qualityCheck` method is responsible for this. The target weight is represented by the final variable `TARGET_WEIGHT_IN_GRAMS`. 
If the actual weight only deviates by 1%, the method outputs "perfect". If the deviation is more than 1% but less than 5%, 
the pack must undergo a second manual check. The method outputs “manual check”. For all other deviations, the 
weight is not tolerable and the method outputs “reject”. The only exception is if the measured weight is more than 75%
greater than desired. This indicates a defect in the machine and should be checked. The method outputs “stop and check”.


### 1. Set up the criteria for the equivalence classes!

The criteria for the equivalence classes are as follows:

1. deviation <= 1%
2. 1% < deviation <5%
3. 5% <= deviation <= 75%
4. 75% < deviation

### 2. Think of four equivalence classes that you should test. For each of these equivalence classes, give a possible input, a description and the desired result!

Four equivalence classes, considering equivalence criteria number 2, would be as follows:

- valid: a deviation between 1% and 5%
- invalid: a deviation greater than 5%
- invalid: a deviation less than 1%
- invalid: a deviation that is a non-numeric input
- invalid: a deviation equal to 5%

### 3. What is a boundary value analysis? Which values are suitable for carrying out a limit value analysis in the given scenario?


