# Question
This problem was asked by Jane Street.

`cons(a, b)` constructs a pair, and `car(pair)` and `cdr(pair)` returns the first and last element of that pair. For example, `car(cons(3, 4))` returns `3`, and `cdr(cons(3, 4))` returns `4`.

Given this implementation of `cons`:
```
def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair
Implement car and cdr.
```

# Solution
This problem is more a test of understanding than problem-solving. Note that the `cons` function defines a function `pair(f)` that it then returns. So when we run `car(pair)`, we can actually call `pair()` in our function. Next, `pair` actually takes in a parameter `f`, which is a function of our own choosing that in turn, receives `a,b` as parameters. All `f` needs to do, is return `a` for the `car` implementation and return `b` for the `cdr` implementation. After all the unravelling, this actually takes pretty short and simple code:

```
def car(pair):
    return pair(lambda a,b: a)
```

Also of interest is that the nested function declaration allows `a,b` to exist in scope within the `pair` function.

15-07-2018
