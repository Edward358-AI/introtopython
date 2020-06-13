# Functions

Well, what can you do with these variables? There's many operations you can use variables in. The basic idea of a function is to possibly take in some parameters, or arguments, and do something with these parameters. It's similar to the concept of a cooking recipe.

## Printing

One of the most simple functions is the print. If you want to see the value stored inside of your variable, you can print it out.

```python
>>> x = 5
>>> print(x)
5
>>> print(x+3)
8
```

You can also print multiple things together. If you pass multiple values, remember to separate them with a comma.

```python
>>> x = 5
>>> y = 3
>>> print(x y)
File "<stdin>", line 1
  print(x y)
          ^
SyntaxError: invalid syntax
>>> print(x, y)
5 3
```

You can also print strings, not just numbers!

```python
>>> x = 'I really like eating cake!'
>>> print(x)
```

## Defining functions

You can even make your own functions! When you call a function, you're asking the computer to follow all the steps inside of that function, like following the steps of a recipe. So you can write your own recipes. Here's an example of a function in code.

```python
def find_average():
    sum_of_one_and_three = 1+3
    average = sum_of_one_and_three/2
```

```python
instructions for finding the average of 1 and 3:
    1. add the numbers together
    2. divide by two
```

## Parameters

Right now, this function isn't very useful. There's no point in always finding the average of 1 and 3, because we already know it's two.

Luckily, you can modify this code to find the average of any two numbers.

```python
def find_average(a, b):
    sum_of_a_and_b = a+b
    average = sum_of_a_and_b/2

find_average(2, 6)
```

## Return

Right now, it's still not very helpful. The value that we found in the end is "trapped" inside of the function. We can print the average inside of the function, like below:

```python
def find_average(a, b):
    sum_of_a_and_b = a+b
    average = sum_of_a_and_b/2
    print(average)

find_average(2, 6)
```

And it gives the expected value, 4, but if we try to print average outside:

```python
def find_average(a, b):
    sum_of_a_and_b = a+b
    average = sum_of_a_and_b/2

find_average(2, 6)
print(average)
```

It gives an error. Bummer.

So, how do we get the value to the outside? We can tell the function to "return" the average at the end.

```python
def find_average(a, b):
    sum_of_a_and_b = a+b
    average = sum_of_a_and_b/2
    return average

print(find_average(2, 6))
```

Essentially, you're asking the computer to report back to you the value that it found. You can do whatever you want with this value: put it in a variable, print it, pass it into another function... But in this case, I just printed it out again.

## Math

You can also add and subtract numbers!

```python
>>> 3 + 3
6
>>> 3 - 2
1
>>> 1 - 3
-2
>>> 4 * 2
8
>>> 4 / 2
2.0
>>> 4 ** 2
16
```

The last function here is the exponent, or power function. Remember to use `**` and not `^` when squaring something or raising a number to any other power, as the `^` (caret) in Python means something else.

Of course, you can also use these on variables:

```python
>>> x = 3
>>> y = 5
>>> x + y
8
>>> x * y
15
>>> z = x + y
```

In the last statement, we are assigning the value of `x + y` to `z`, so `z` will hold the value `8`.
