# ISEE Exercise 9 - Task - Structural Tests

Written By: Suvansh Shukla (matriculation number: 256245)

## Task - Control flow orientated test procedures

### explain the terms `C0`-test, `C1`-test and `C2`-test and differentiate between them!

`C0`-tests: these test are written and calculated according to percentage of executed instructions.     
`C1`-tests: these tests are written and calculated according to percentage of executed commands and branches.   
`C2`-tests: these tests are written and calculated according to percentage of executed program flow paths.  

### why are `C2`-tests less relevant in practice?

`C2`-test are less relevant in practice because it is not always possible to traverse each and every program path in its entirety.      
This also means that under certain conditions testing may get stuck, especially when trying to cover loops.

### name and briefly explain the variants of `C2`-tests presented in the lecture!

There are Four main variants of `C2`-tests. 

`C2a`: All possible execution paths are traversed.  
`C2b`: All possible execution paths are traversed but loops are traversed according to special rules.   
`C2c`: All possible execution paths are traversed but loops are only traversed a preset number of times.    

