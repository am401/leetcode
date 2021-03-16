## Valid Parenthesis
Link: https://leetcode.com/problems/valid-parentheses/

## Problem

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.

----

To solve this problem I utilized a `stack` to build out a list of parenthesis we are iterating over. The idea here is to use a process of elimination to ensure that the open parentehsis have a matching closing parenthesis. At the end of the program, we check the length of `stack`, which is our stack to ensure we have matched all the parenthesis provided. If it returns 0, we have been able to close each found open parenthesis and the challenge is solved. Otherwise `false` is returned.
