# Inputting

If we go back to repl.it, you will remember that big black section on the right side of your screen. That section also has other uses, such as being able to type enter input for your program to see.

## Getting input

In python, the `input()` command returns whatever was typed into the console and you can set  it to a variable. For example, if you wanted to find out your users name, you could do

```python
name = input()
```

If your user then typed in "Colin," then name would now have the value "Colin". You can also put a message inside the input function's parentheses to be displayed to the user. For example, if you wanted to make it clear that you wanted to know someone's name, you could do

```python
name = input('Please enter your name: ')
```

Let's head over to repl and see what this will do.

## Integer input

The `input()` function is useful for getting a string, not an integer. If you wanted to, for example, make a calculator, you would want to get an integer from the user. It's very simple to convert the string the program receives into an integer. We can just do:

```python
>>> foo = int(input())
3
>>> print(foo)
3
>>> print(foo+5)
8
```

Now, we've changed the `input` function to an integer by just wrapping the `int` function around it, which changes whatever is inside its parentheses to an integer. Be careful though, if `input()` has characters that aren't numbers, then it won't work!

```python
>>> foo = int(input())
cat
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'cat'
```

In this case, Python is trying to convert the string "cat" into an integer, but the string "cat" isn't a number and so Python raises an error.
