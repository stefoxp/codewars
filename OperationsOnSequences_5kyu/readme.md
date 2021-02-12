# Operation On Sequences 5 kyu

Let an array or a list

```python
arr = [x(1), x(2), x(3), x(4), ..., x(i), x(i+1), ..., x(m), x(m+1)]
```

where all x(i) are positive integers. The length lg of this array will be a positive multiple of 4.

Let

```python
P = (x(1) ** 2 + x(2) ** 2) * (x(3) ** 2 + x(4) ** 2) * ... * (x(m) ** 2 + x(m+1) ** 2),
```

x ** y means x raised to the power y.

## Task

Given an array or list arr the task is to find:

- two non-negative integers A and B such as P = A ** 2 + B ** 2 (1).

The function solve(arr) returns an array or a list [A, B] where A and B verify (1).

## Examples

```python
solve([2, 1, 3, 4]) returns [2, 11] :
(2*2 + 1*1) * (3*3 + 4*4) = 5 * 25 = 125
and 2 * 2 + 11 * 11 = 125

solve([2, 1, 3, 4, 2, 2, 1, 5, 2, 3, 4, 5]) returns [2344, 2892] :
(2*2 + 1*1) * (3*3 + 4*4) * (2*2 + 2*2) * (1*1 + 5*5) * (2*2 + 3*3) * (4*4 + 5*5) = 13858000
and 2344 * 2344 + 2892 * 2892 = 13858000
```

## Notes

- The decomposition into A ** 2 + B ** 2 is not unique: the testing function checks if (1) is verified.

```python
solve([21, 24, 15, 22, 1, 2]) can return [639, 1788] or [1431, 1248]; both return are correct.
    P is     3605265
    A*A+B*B  3605265
```

- Lengths of lists are less than 100 and elements of lists less than 25
- Please ask before translating

