# Somethings to note regarding C0, C1 & C2 testing

> ![NOTE] 
> All this is the result of a long discussion with Google's Gemini
> [Link to conversation](https://g.co/gemini/share/49a5b7585103)

## How do you differentiate between C0 testing and C1 testing? If I try to test each individual instruction or line of code (as happens in C0), won't it also automatically cover each branch (as happens in C1)

You've hit upon a very common point of confusion when first learning about these coverage criteria\!

Here's how C0 (Statement Coverage) and C1 (Branch/Decision Coverage) differ, and why C0 does **not** automatically cover C1:

### C0 Testing (Statement Coverage)

  * **Definition:** C0 testing aims to execute **every executable line of code (statement)** in your program at least once.
  * **Focus:** It's about ensuring that no line of code is left completely untouched by your tests.
  * **Goal:** To find "dead code" (code that can never be reached) or simply confirm that every part of your program is, at least, callable.

### C1 Testing (Branch/Decision Coverage)

  * **Definition:** C1 testing aims to ensure that every **decision point** in your code has had **all of its possible outcomes (branches/paths)** executed at least once.
  * **Focus:** It's about testing the logical flow and ensuring that all possible "turns" in your code are taken.
  * **Goal:** To test the conditions that guide the program's execution, ensuring both the "true" and "false" paths of a decision are exercised.

### The Key Difference & Why C0 Doesn't Imply C1

The crucial difference lies in how they handle **decision points** (like `if`, `else`, `switch`, loops).

Let's use an example:

```java
public class GradeCalculator {
    public String getGrade(int score) {
        // Line 1: Start of method
        String grade;
        // Line 2: Decision Point (if statement)
        if (score >= 90) { // Branch 1 (True path for score >= 90)
            // Line 3: Statement
            grade = "A";
        } else { // Branch 2 (False path for score >= 90)
            // Line 4: Statement
            grade = "B";
        }
        // Line 5: Statement
        System.out.println("Score: " + score + ", Grade: " + grade);
        // Line 6: End of method
        return grade;
    }
}
```

**Scenario 1: Achieving 100% C0 (Statement Coverage)**

To get 100% C0 coverage, we need to execute every line: 1, 2, 3, 4, 5, 6.
Let's use **one test case**:

  * **Test Case:** `getGrade(95)`
      * **Execution Path:** Line 1 -\> Line 2 (`score >= 90` is TRUE) -\> **Line 3** -\> Line 5 -\> Line 6.
      * **Lines Covered:** 1, 2, 3, 5, 6.
      * **Line NOT Covered:** Line 4 (the `else` block).

**Result for C0:** Our single test case `getGrade(95)` **did NOT achieve 100% C0 coverage** because Line 4 was never executed. To get 100% C0, we'd need another test case that makes `score >= 90` false.

Let's fix C0:

  * **Test Case 1:** `getGrade(95)` (Covers Line 1, 2, **3**, 5, 6)
  * **Test Case 2:** `getGrade(80)` (Covers Line 1, 2, **4**, 5, 6)

Now, we have 100% C0 (all lines 1, 2, 3, 4, 5, 6 are covered).

**Scenario 2: Does 100% C0 (from Scenario 1) automatically cover C1 (Branch Coverage)?**

Now that we have 100% C0 using `getGrade(95)` and `getGrade(80)`, let's check C1:

  * **Decision Point:** `if (score >= 90)` (Line 2)
  * **Branches:**
      * **True Branch:** Executes Line 3 (`grade = "A"`)
      * **False Branch:** Executes Line 4 (`grade = "B"`)

Our test cases:

  * `getGrade(95)`: Exercises the **True Branch** (executes Line 3).
  * `getGrade(80)`: Exercises the **False Branch** (executes Line 4).

**Result for C1:** Yes\! In this specific, simple example, achieving 100% C0 also **happened to achieve 100% C1**.

### When C0 Does NOT Imply C1

However, this is not always the case, especially with **`if` statements without an `else` block**, or **loops**.

Consider this code:

```java
public class DiscountCalculator {
    public double calculateDiscount(double amount, boolean isPremiumMember) {
        // Line 1
        double discount = 0.0;
        // Line 2: Decision Point (if statement)
        if (isPremiumMember) { // Branch 1 (True path)
            // Line 3: Statement
            discount = amount * 0.10; // 10% discount for premium
        }
        // Line 4: Statement (always executed)
        System.out.println("Calculated discount: " + discount);
        // Line 5: Statement
        return discount;
    }
}
```

**Testing for 100% C0 (Statement Coverage):**

  * **Test Case:** `calculateDiscount(100.0, true)`
      * **Execution Path:** Line 1 -\> Line 2 (`isPremiumMember` is TRUE) -\> **Line 3** -\> Line 4 -\> Line 5.
      * **Lines Covered:** 1, 2, 3, 4, 5. **(100% C0 achieved\!)**

**Now, let's check C1 (Branch Coverage) with this single test case:**

  * **Decision Point:** `if (isPremiumMember)` (Line 2)
  * **Branches:**
      * **True Branch:** (When `isPremiumMember` is `true`) - **Executed by our test case.**
      * **False Branch:** (When `isPremiumMember` is `false`) - **NOT executed by our test case.**

**Result for C1:** Even though we have 100% C0 coverage, we **do NOT have 100% C1 coverage**. We've only tested one outcome (the `true` outcome) of the `if` statement's decision. We haven't tested what happens when `isPremiumMember` is `false` (the implicit `else` branch).

To achieve 100% C1, you'd need another test case:

  * **Test Case 2:** `calculateDiscount(100.0, false)`
      * This would execute Line 1 -\> Line 2 (`isPremiumMember` is FALSE) -\> Line 4 -\> Line 5. (Line 3 is skipped).
      * This covers the False Branch.

### In a Nutshell:

  * **C0 (Statement Coverage)** just asks: "Has every line of code been *touched*?"
  * **C1 (Branch Coverage)** asks: "For every 'fork in the road' (decision), have we *gone down every possible path* coming out of that fork?"

C1 is a **stronger criterion** than C0 because it forces you to test both outcomes of a decision, even if one of those outcomes doesn't lead to unique new lines of code (as in an `if` without an `else`). If you achieve 100% C1, you will always achieve 100% C0. But, as shown above, 100% C0 does not guarantee 100% C1.

---

## That was a good example. Similarly, explain the difference between C1 and C2. 

Okay, building on the previous example, let's differentiate between **C1 (Branch/Decision Coverage)** and **C2 (Condition Coverage)**.

### C1 Testing (Branch/Decision Coverage) - Recap

  * **Focus:** Ensures that every **decision point** (like an `if` statement, `else`, `switch`, loop condition) has had **all of its possible outcomes (branches)** executed.
  * **What it cares about:** Did the `if` condition evaluate to `true` at least once, and `false` at least once (thus covering both the `if` block and the `else` block, or the `if` block and the implicit path around it)?

### C2 Testing (Condition Coverage)

  * **Focus:** Ensures that every **individual boolean sub-expression** within a compound decision has been evaluated to both `true` and `false` at least once.
  * **What it cares about:** If you have `if (A && B)`, did `A` evaluate to `true` and `false` independently? And did `B` evaluate to `true` and `false` independently?
  * **Goal:** To uncover errors related to the individual parts of complex boolean expressions, even if those individual parts don't necessarily change the overall outcome of the entire decision.

-----

### The Key Difference & Why C1 Doesn't Imply C2

The difference becomes clear when you have **compound conditions** (conditions combined with `&&` (AND), `||` (OR), `!` (NOT)).

Let's use an example:
Imagine a system that gives a bonus based on performance and tenure.

```java
public class BonusCalculator {
    public String calculateBonus(int performanceScore, int yearsOfService) {
        // Line 1
        String bonusStatus = "No Bonus";

        // Line 2: Decision Point with a COMPOUND CONDITION
        // Condition 1: performanceScore > 80 (let's call this 'P')
        // Condition 2: yearsOfService >= 5 (let's call this 'Y')
        if (performanceScore > 80 && yearsOfService >= 5) { // if (P && Y)
            // Line 3: Statement
            bonusStatus = "Full Bonus";
        } else {
            // Line 4: Statement
            bonusStatus = "Partial Bonus"; // Or could still be "No Bonus" for simplicity in example
        }
        // Line 5: Statement
        System.out.println("Bonus Status: " + bonusStatus);
        // Line 6: End of method
        return bonusStatus;
    }
}
```

-----

**Scenario 1: Achieving 100% C1 (Branch Coverage)**

To get 100% C1, we need to make the `if` condition (`performanceScore > 80 && yearsOfService >= 5`) evaluate to `true` at least once, and `false` at least once.

  * **Test Case 1 (for TRUE branch):**

      * `calculateBonus(90, 7)`
      * (`P` is True, `Y` is True) -\> `P && Y` is **TRUE**
      * Executes: Line 1 -\> Line 2 -\> **Line 3** -\> Line 5 -\> Line 6.
      * (Covers the `if` block / TRUE branch of the decision)

  * **Test Case 2 (for FALSE branch):**

      * `calculateBonus(70, 3)`
      * (`P` is False, `Y` is False) -\> `P && Y` is **FALSE**
      * Executes: Line 1 -\> Line 2 -\> **Line 4** -\> Line 5 -\> Line 6.
      * (Covers the `else` block / FALSE branch of the decision)

With these two test cases, we have **100% C1 (Branch Coverage)**. Both branches of the `if/else` statement (Line 3 and Line 4) have been executed.

-----

**Scenario 2: Does 100% C1 (from Scenario 1) automatically cover C2 (Condition Coverage)?**

Now let's check C2. We need to ensure each *individual sub-expression* (`P` and `Y`) evaluates to both `true` and `false`.

Our current test cases are:

1.  `calculateBonus(90, 7)`: `P` is `true`, `Y` is `true`.
2.  `calculateBonus(70, 3)`: `P` is `false`, `Y` is `false`.

Let's look at the individual conditions:

  * **Condition P (`performanceScore > 80`):**

      * Evaluated `true` in Test Case 1.
      * Evaluated `false` in Test Case 2.
      * **P is fully covered (True & False).**

  * **Condition Y (`yearsOfService >= 5`):**

      * Evaluated `true` in Test Case 1.
      * Evaluated `false` in Test Case 2.
      * **Y is fully covered (True & False).**

In this *specific* example, our C1 test cases also happened to achieve 100% C2.
But this is **not always guaranteed for C1 to achieve C2**, especially with short-circuiting or more complex combinations.

-----

### A Clearer Example of C1 NOT Implying C2

Let's modify the `calculateBonus` slightly to make `P && Y` behave differently:

```java
public class BonusCalculatorV2 {
    public String calculateBonus(int performanceScore, int intelliScore) {
        // Line 1
        String bonusStatus = "No Bonus";

        // Condition 1: performanceScore > 80 (P)
        // Condition 2: intelliScore > 70 (I)
        if (performanceScore > 80 && intelliScore > 70) { // if (P && I)
            // Line 2
            bonusStatus = "Full Bonus";
        } else {
            // Line 3
            bonusStatus = "No Bonus";
        }
        // Line 4
        return bonusStatus;
    }
}
```

**Testing for 100% C1 (Branch Coverage):**

To get 100% C1, we need `P && I` to be True once, and False once.

  * **Test Case 1 (for TRUE branch):**

      * `calculateBonus(90, 80)` -\> `P` is True, `I` is True. `P && I` is **TRUE**. (Covers Line 2)

  * **Test Case 2 (for FALSE branch):**

      * `calculateBonus(90, 50)` -\> `P` is True, `I` is False. `P && I` is **FALSE**. (Covers Line 3)

With these two test cases, we have **100% C1 (Branch Coverage)**.

**Now, let's check C2 (Condition Coverage) with these two test cases:**

  * **Condition P (`performanceScore > 80`):**

      * In Test Case 1 (`90, 80`): P is `true`.
      * In Test Case 2 (`90, 50`): P is `true`.
      * **P has only been `true`. It has NOT been `false`.**

  * **Condition I (`intelliScore > 70`):**

      * In Test Case 1 (`90, 80`): I is `true`.
      * In Test Case 2 (`90, 50`): I is `false`.
      * **I is fully covered (True & False).**

**Result:** Even with 100% C1, we **do NOT have 100% C2** because condition `P` (`performanceScore > 80`) never evaluated to `false`.

To get 100% C2, we'd need another test case where `P` is false, for example:

  * **Test Case 3:** `calculateBonus(70, 80)` -\> `P` is False, `I` is True. `P && I` is FALSE.
      * This case would make `P` evaluate to `false`, completing C2 coverage for `P`.

-----

### In a Nutshell:

  * **C1 (Branch Coverage):** Focuses on the **overall outcome** of a decision (`if/else`, loops). Did the `if` block run? Did the `else` block run? (Just true/false for the entire condition).
  * **C2 (Condition Coverage):** Digs deeper into **compound conditions** (`&&`, `||`). Did *each individual part* (`A`, `B`, `C` in `A && B || C`) evaluate to `true` at some point and `false` at another?

**C2 is a stronger criterion than C1** because it forces you to design tests that specifically make each sub-condition flip its value, potentially uncovering bugs that C1 might miss (where the overall decision outcome is the same, but a specific sub-condition isn't fully explored).
If you have 100% C2, you will always have 100% C1 (and 100% C0).

--

## Could you also give an example comparing C0, C1 or C2 coverages don't imply each other using a loop? 

You're asking for a fantastic example that really highlights the nuances of C0, C1, and C2, especially with loops and compound conditions.

Let's use a function that processes an array of numbers, with both a loop and an inner conditional statement that has a compound condition.

```java
public class CoverageExample {
    public int processNumbers(int[] numbers, int lowerBound, int upperBound) {
        // Line 1: Initialize sum
        int sum = 0;
        // Line 2: Loop counter
        int i = 0;

        // Line 3: Loop condition (Decision Point 1)
        while (i < numbers.length) {
            // Line 4: Get current number
            int currentNumber = numbers[i];

            // Line 5: Inner 'if' condition (Decision Point 2) - COMPOUND
            // Condition A: currentNumber >= lowerBound
            // Condition B: currentNumber <= upperBound
            if (currentNumber >= lowerBound && currentNumber <= upperBound) { // if (A && B)
                // Line 6: Statement inside if block
                sum += currentNumber;
            }
            // Line 7: Increment loop counter
            i++;
        }
        // Line 8: Return total sum
        return sum;
    }
}
```

Now let's analyze the coverage types:

-----

### 1\. C0 (Statement Coverage) Does NOT Imply C1 or C2

**Goal for C0:** Execute every executable line (Lines 1, 2, 3, 4, 5, 6, 7, 8).

**Test Case 1 for C0:** `processNumbers(new int[]{15, 25}, 10, 30)`

  * **Execution Flow:**

      * `i=0`: Line 1, 2, 3 (true), 4, 5 (`15 >= 10 && 15 <= 30` is **TRUE**), 6, 7.
      * `i=1`: Line 3 (true), 4, 5 (`25 >= 10 && 25 <= 30` is **TRUE**), 6, 7.
      * `i=2`: Line 3 (false).
      * Line 8.

  * **C0 Result:** All lines (1-8) are executed. **100% C0 Achieved\!** (Sum will be 40)

**Now, let's see if this single test case achieved C1 or C2:**

  * **C1 (Branch Coverage):**

      * **Decision Point 1 (`while` loop - Line 3):**
          * True branch (`i < numbers.length` is true): **Covered** (loop ran multiple times).
          * False branch (`i < numbers.length` is false): **Covered** (loop exited).
          * **Loop C1 is 100%.**
      * **Decision Point 2 (`if` condition - Line 5):**
          * True branch (`currentNumber >= lowerBound && currentNumber <= upperBound` is true): **Covered** (Line 6 executed for 15 and 25).
          * False branch: **NOT Covered**. We never had an item that made the condition false, so Line 6 was never *skipped*.
          * **If C1 is NOT 100%.**

  * **C2 (Condition Coverage):**

      * **Decision Point 1 (`while` condition `i < numbers.length`):**
          * `i < numbers.length` (T): Covered.
          * `i < numbers.length` (F): Covered.
          * **Loop Condition C2 is 100%.**
      * **Decision Point 2 (`if` condition `currentNumber >= lowerBound && currentNumber <= upperBound`):**
          * Condition A (`currentNumber >= lowerBound`):
              * `true`: Covered (for 15 and 25).
              * `false`: **NOT Covered**.
          * Condition B (`currentNumber <= upperBound`):
              * `true`: Covered (for 15 and 25).
              * `false`: **NOT Covered**.
          * **If C2 is NOT 100%.**

**Conclusion:** 100% C0 **does NOT guarantee** 100% C1 or 100% C2. Our single test case achieved 100% C0, but only partial C1 and C2.

-----

### 2\. C1 (Branch Coverage) Does NOT Imply C2

Let's add a test case to achieve 100% C1 (Branch Coverage).

**Test Cases for 100% C1:**

1.  `processNumbers(new int[]{15}, 10, 30)`
      * Makes `if` condition **TRUE** (15 is within bounds).
      * Covers `while` True/False and `if` True branches.
2.  `processNumbers(new int[]{50}, 10, 30)`
      * Makes `if` condition **FALSE** (50 is outside bounds).
      * Covers `while` True/False and `if` False branches.

Now, with these two test cases, we have **100% C1 Achieved\!** (All branches of both the `while` and `if` are covered).

**Now, let's see if these two test cases achieved C2:**

  * **Decision Point 2 (`if` condition `currentNumber >= lowerBound && currentNumber <= upperBound`):**
      * **Condition A (`currentNumber >= lowerBound`):**
          * `true`: Covered (from 15 and 50).
          * `false`: **NOT Covered**. We never had a number less than `lowerBound` (e.g., 5).
      * **Condition B (`currentNumber <= upperBound`):**
          * `true`: Covered (from 15).
          * `false`: Covered (from 50).
          * **Condition B is 100% covered (True & False).**

**Conclusion:** Even with 100% C1, we **do NOT have 100% C2** because Condition A (`currentNumber >= lowerBound`) never evaluated to `false`.

-----

### 3\. C2 (Condition Coverage) DOES Imply C1 and C0

To achieve 100% C2, we need to make sure:

  * `i < numbers.length` is True and False.
  * `currentNumber >= lowerBound` is True and False.
  * `currentNumber <= upperBound` is True and False.

**Test Cases for 100% C2 (and thus 100% C1 and C0):**

1.  **`processNumbers(new int[]{15}, 10, 30)`** (A=T, B=T -\> `if` is TRUE)
      * Covers: `i < length` (T), `A` (T), `B` (T), `while` true branch, `if` true branch.
2.  **`processNumbers(new int[]{5}, 10, 30)`** (A=F, B=T -\> `if` is FALSE)
      * Covers: `i < length` (T), `A` (F).
      * (Note: `B` is still True here, so we need one more to get B=F)
3.  **`processNumbers(new int[]{40}, 10, 30)`** (A=T, B=F -\> `if` is FALSE)
      * Covers: `i < length` (T), `B` (F).
4.  (An empty array `processNumbers(new int[]{}, 10, 30)` would ensure the `while` condition immediately goes false on the first check, covering `i < numbers.length` (F), if not already covered by previous tests causing loop exit).

With these specific test cases (or a minimal set like it), you would achieve 100% C2. And once you have 100% C2, you inherently have 100% C1 (because all branches were covered to satisfy the conditions) and 100% C0 (because all lines were covered as a result of executing all branches).

-----

### Summary of Implications:

  * **C0 (Statement Coverage) $\\not\\implies$ C1 (Branch Coverage)**
  * **C1 (Branch Coverage) $\\not\\implies$ C2 (Condition Coverage)**
  * **C2 (Condition Coverage) $\\implies$ C1 (Branch Coverage) $\\implies$ C0 (Statement Coverage)**

The hierarchy means C2 is the strongest, requiring the most granular level of testing for conditions within your code.
