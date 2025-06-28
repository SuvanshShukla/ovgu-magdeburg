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

