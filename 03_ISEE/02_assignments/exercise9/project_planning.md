# ISEE Exercise 9 - Task 3

Written By: Suvansh Shukla (matriculation number: 256245)

## Task - Project planning

The following scenario is given:

A new windscreen wiper system is to be implemented in future electric cars. In order for the system to be ready to function in time for the release date, many individual interdependent steps are necessary. You have already created a list of the required processes and listed them chronologically to enable an orderly process.

| Abbr. | Process                        | Duration | Depends on |
| ----- | ------------------------------ | -------- | ---------- |
| A     | Kick-Off                       | 1        |            | 
| B     | Employee survey                | 8        | A          |
| C     | Observation of the old system  | 7 	    | A          |
| D     | Project planning               | 5 	    | B,C        |
| E     | Risk analysis                  | 3 	    | D          |
| F     | Ordering new hardware          | 6 	    | E          |
| G     | Setting up the hardware        | 3 	    | F          |
| H     | Software development           | 14 	    | E          |
| I     | Testing the software           | 5 	    | H          |
| J     | Testing software with hardware | 7 	    | G,I        |
| K     | Introducing the system         | 3 	    | J          |
| L     | Testing in operation           | 4 	    | K          |
| M     | Project completion             | 1 	    | L          |

1. Draw a network diagram based on the processes! Label the critical path.

![network diagram](./precedence_diagram.svg)

2. Draw the corresponding Gantt diagram!

![Gantt Chart](./gantt.svg)

3. What are the main differences between the network diagram and the Gantt diagram?

Taken from this note - ![difference.md](./difference.md)

The primary difference between a network diagram and a Gantt chart is that, the Gantt chart integrates dates better than the network diagram.   
The Gantt chart also has the unfortunate side-effect of not being able to display the dependencies properly.    
The Gantt chart is also represented by bars on a calendar, while the network diagram uses blocks to denote processes.   
The Gantt chart more intuitively displays the duration of each process, while in the network diagram the duration is just written in the blocks.    

