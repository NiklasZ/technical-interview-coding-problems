# Question
This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?

# Solution

## With division
This can be done by taking the product of the entire array and for each element you divide the product by it to get the result. E.g 120/5 = 24.

Complexity: `O(n)` time, `O(n)` space.

## Without division
There are a number of different ways to replace division or alternate ways to get the products, but I did not find any that would perform significantly better than a naïve solution. My solution reuses some products to avoid redundancy, but ultimately is not of a better complexity.

Complexity: `O(n^2)` time, `O(n)` space.
