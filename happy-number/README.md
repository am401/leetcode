### Happy Number
Link: https://leetcode.com/problems/happy-number

### Problem
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

- Starting with any positive integer, replace the number by the sum of the squares of its digits.
- Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
- Those numbers for which this process ends in 1 are happy.

----

For the solution in this case, I created a `while` loop that would check whether the `squared_sum` equals `1`. If it did, True would be returned, since the number was a happy number. The checks were achieved using a couple of for loops, that would place the digits of `n` in to a list. The secoond loop would then calculate the square of each number and add it to an additional list.

The sum of that second list would be calculated and checked with the `while` loop. Once it had gotten to `1`  the happy number was identified. At the same time, to help identify unhappy numbers, ie when a loop occurs, we create a dictionary or a list to check if the number has already been seen. If it has, it would then begin to loop.

