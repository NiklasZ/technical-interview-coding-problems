# Question
This problem was recently asked by Google.

Given a list of numbers and a number `k`, return whether any two numbers from the list add up to `k`.

For example, given `[10, 15, 3, 7]` and `k` of `17`, return true since `10 + 7` is `17`.

Bonus: Can you do this in one pass?

# Solution
You can do this in one pass-through by using a set to store the checked elements. For the next element `a` you see if you can find `k-a` in the set and if so, there is such a sum from a pair of elements.

Complexity: `O(n)` time, `O(n)` space.

11-07-2018
