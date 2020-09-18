#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(1)

b) O(n logn)
    in testing, the duration of the run time seems to go up logarithmically, with 10,000,000 not successfully completeing.

c) 0(n)

## Exercise II

We can implement a BST for this scenario.
1. Let's start at the midpoint
    a) Let the building height be expressed by f(loors)
    b) The midpoint can be express by f//2
2. If the egg  breaks from this height we will need to try again from a lower floor
    b) if the egg doesn't break we will need to drop the egg from a higher floor
3. Recalculate the new midpoint, and try the routine again.

The runtime complexity of a BST can be expressed as O(log n).