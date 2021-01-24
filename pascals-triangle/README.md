### Pascals Triangle
Link: https://leetcode.com/problems/pascals-triangle

#### Problem
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

----

This was quite tricky for me to solve but working with a friend I got there in the end. The solution I have submitted pre-defines the first two rows - `0th` and `1st` rows which are `[1]` and `[1][1]` respectively. The 0th element in each row is always going to be `[1]`.

In this case `n` is the number of rows we are pritning. Since the first two rows are already known, we want a range from `2` to `n` to loop through, this will be `for i in range(2, n):`

The results are stored in a nested list `result = [[1],[1.1]]`. We are going to be appending list with the results of the loops in order to get the results.

We set the first element as `[1]` in a variable, in this case `row_list`

We then kick start the next loop, which will loop through the elements of that specific row: `for j in range(1, i)` again, we already know the `0th` and `1st` rows

While looping through the elements, we are summing the elements from the previous row (`i - 1`) and using the current element's position to get the relevant elements (`j - 1`) and `j`. The elements are appended to `row_list`, which is then appended to the `result` variable.
