# ps1

Homework file:
https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-1/lecture-4-machine-interpretation-of-a-program/MIT6_00SCS11_ps1.pdf

Lectures:
https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-1/lecture-2-core-elements-of-a-program/

https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-1/lecture-3-problem-solving/

Problem 3 process:

Onto Problem 3 now, implementing Bisection Search. 

Got it done pretty quickly (spent 15 minutes speaking with a colleague 
about his upcoming interview) 

However, ran into a problem when I tried Test Case 2 balance 999999
Probably a rounding error, will debug

Was a rounding error, my machine rounded the ending balance to -.13 while the example had it set to -.12 . Since I set my value to be greater than -.13 it never completed and looped forever.

I'll just leave it at -.20 < tempBalance < 0. Then it will be accurate to at least 1 cent.
