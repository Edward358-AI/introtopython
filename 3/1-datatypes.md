# Data types

In the first class, we learned about variables and some of the values they can store; including integers and strings. This section will give more detail on some of these data types.

## Integers

An integer is any number without values after the decimal point. -3, -2, 0, 3, and 201 are all examples of integers.

## Floats

Floats are numbers with values after the decimal point. This includes numbers such as pi, 1.5, 1.1, etc. Notice that numbers like 1.0, 2.0, 3.0, -1.0, ... are all considered floats. Python does not automatically convert them into integers. However, Python will still consider 1.0 to be equal to 1.

When you divide numbers, you will always get a float back. There is a separate operator if you wish to receive an integer; the `//` operator.

```python
>>> 3/4
0.75
>>> 3//4
0
>>> 10/4
2.5
>>> 10//4
2
>>> 11/4
2.75
>>> 11//4
2
```

## Strings

Strings are sequences of characters. Python strings, by default, use something called
Unicode. Essentially, it means that certain numbers are mapped to certain characters. Let's try out a few of these examples, by using the `chr` and `ord` functions.

```
>>> ord('A')
65
>>> ord('a')
97
>>> ord('B')
66
>>> chr(65)
'A'
>>> chr(66)
'B'
```
