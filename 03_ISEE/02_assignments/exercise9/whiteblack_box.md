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

### What is the minimum number of test cases required to perform the coverage tests and ?

### State the logical and one specific test case as well as their executed path!
