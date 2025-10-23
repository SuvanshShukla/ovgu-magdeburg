# ICSE Exercise 1 - Task 4 - Error message

Authored by: Suvansh Shukla  
Matriculation Number: 256245

## Script 1

After running the first script we get the following error message:

```console
  File "C:\Users\HP\Documents\OVGU_Magdeburg\Winter-SEM-II-2025-26\ICSE\01_assignment_questions\01\assignment-4-scripts-a014-templates\script_1.py", line 1
    print("This is a simple test"
         ^
SyntaxError: '(' was never closed
```

**FIX**: close the bracket of the print statment on line 1

## Script 2

After running the first script we get the following error message:

```console
Traceback (most recent call last):
  File "C:\Users\HP\Documents\OVGU_Magdeburg\Winter-SEM-II-2025-26\ICSE\01_assignment_questions\01\assignment-4-scripts-a014-templates\script_2.py", line 3, in <module>
    force = mass_in_kg * gravitational_acceleration
NameError: name 'gravitational_acceleration' is not defined
```

**FIX**: define a `gravitational_acceleration` variable with a valid value for earth's gravity like 9.8.  
This new variable should also be placed above line 3 and not after it.

## Script 3

After running the first script we get the following error message:

```console
Traceback (most recent call last):
  File "C:\Users\HP\Documents\OVGU_Magdeburg\Winter-SEM-II-2025-26\ICSE\01_assignment_questions\01\assignment-4-scripts-a014-templates\script_3.py", line 1, in <module>
    from Math import sqrt
ModuleNotFoundError: No module named 'Math'
```

**FIX**: install the `Math` package or move your code to some place where this module is already present

## Script 4

After running the first script we get the following error message:

```console
  File "C:\Users\HP\Documents\OVGU_Magdeburg\Winter-SEM-II-2025-26\ICSE\01_assignment_questions\01\assignment-4-scripts-a014-templates\script_4.py", line 1
    print "Let's run some legacy code..."
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
```

**FIX**: Simply add opening & closing parenthese around the string we want to print.

## Script 5

After running the first script we get the following error message:

```console
Traceback (most recent call last):
  File "C:\Users\HP\Documents\OVGU_Magdeburg\Winter-SEM-II-2025-26\ICSE\01_assignment_questions\01\assignment-4-scripts-a014-templates\script_5.py", line 1, in <module>
    print("Let's repeat this" * 3.)
TypeError: can't multiply sequence by non-int of type 'float'
```

**FIX**: Simply remove `.` (the dot) after three to properly print the string three times.

## Script 6

After running the first script we get the following error message:

```console
  File "C:\Users\HP\Documents\OVGU_Magdeburg\Winter-SEM-II-2025-26\ICSE\01_assignment_questions\01\assignment-4-scripts-a014-templates\script_6.py", line 5
    else:
         ^
IndentationError: unindent does not match any outer indentation level
```

**FIX**: Simply reduce the indent of `else:` by two spaces to make it inline with the `if` statement.

## Script 7

After running the first script we get the following error message:

```console

```

**FIX**:
