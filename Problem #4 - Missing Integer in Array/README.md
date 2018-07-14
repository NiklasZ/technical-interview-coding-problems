# Question
This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input `[3, 4, -1, 1]` should give `2`. The input `[1, 2, 0]` should give `3`.

You can modify the input array in-place.


# Solution
This can be simplified by noting the following:
* As `0` or `-1` are optional and are not positive integers to consider, they are not necessary to solving the problem.
* The memory constraint requires that we use the array's own capacity.

After ignoring the unnecessary elements, it's possible to do a sweep and for each positive integer `a`, we assign it to be in position `a` in the `array` (or actually `a-1`, given we have 0-indexing). This allows us to check on another sweep, whether `a` exists, simply by visiting `array[a-1]`. If we do this for every element, we will arrive at a partially ordered list, where the first gap in the order (where `array[a-1] != a`), gives us the first missing positive integer.

This appears to be enough on a first glance, but there are a few additional special cases to watch for:
* Make sure `a < len(array)` or you will get out of bounds exceptions.
* If the end of the array is reached, whilst checking for gaps, take the `max(array)+1`. This will only happen in situations where every unique positive integer is present. E.g `[1,2,3,4,5]`
* If you swap an element forwards, you need to do 1 additional sweep (to total of 2 for the entire algorithm). Otherwise the swapped element will be out of place.

Complexity: `O(n)` time, `O(1)` space (excluding input array).

## Example
1st sweep:
`[3, 4, -1, 1]` => `[1, 4, -1, 3]` => `[1, 3, -1, 4]`

2nd sweep:
`[1, 3, -1, 4]` => `[1, -1, 3, 4]`

Gap search:
* `[1, -1, 3, 4]`, `array[1-1] == 1`

* `[1, -1, 3, 4]`, `array[2-1] != 2` so the next positive integer is 2.

14-07-2018
