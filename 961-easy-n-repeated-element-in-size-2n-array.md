

## Solution

The solution is pretty easy, create a hashmap (set) and for each element of the array check if it is already in the set, if it is return the number (element), if not add to the set.

```py
numbers_set = set()

for i in nums:
    if i in numbers_set:
        return i

    numbers_set.add(i)
```


