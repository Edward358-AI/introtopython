# Output

We've already learned the print statement. Just to jog your memory, it looks like this:

```python
print()
```

The print statement will print whatever is inside its parenthesis.

However, what if we wanted to get fancy with it? Let's say you had a variable `name` which stored someone's name and you wanted to print both a string and the variable together. If the name was "Joe," you wanted to print "Hello, Joe!"

## String Interpolation

The way to do this is with something called string interpolation. That's just fancy terminology for putting variable values in strings. Still using our name example, the way we'd put the `name` variable into the string we want to print out is:

```python
print(f'Hello, {name}!')
```

If we put the letter f before our single quotes, we can then enclose our variables, in this case `name`, inside curly brackets.

There are a few other ways to do this. For example, you can add strings together:

```python
print('Hello, ' + name + '!')
```

Or you could separate everything with commas. Notice how the `print` function, if it has commas, prints spaces between each of the strings.

```python
print('Hello, ', name, '!')
```
## Escape sequences

What if I were writing some code to play hangman? I would have to print out this guy:

  o                                                                                           
/|\                                                                                           
/ \

Let's try to do that and see what happens.

It gives us an error. The reason is because the "\" character is a special character called an escape sequence. Escape sequences mark the start of special characters in strings, such as "\n" which is an end line character. A couple escape sequence examples are:

"\\\\" which gives us just a normal backslash character                                       
"\n" which gives us an end line                                                               
"\a" which makes a sound                                                                      
"\h" which gives a horizontal tab                                                             
"\v" which gives a vertical tab

Lets try some of these out in repl

## `print`'s other arguments

You may notice that the `print()` statement always prints and then puts you on a new line. This is because the default last character that is printed is the "\n" character. We can easily change this by doing

```python
print('hi', end='')
```

What the `end = ''` does is set the end of string character to ''. Lets see what this does in repl.

We can set the end to anything, as long as it's a string (including escape sequences). If you want print to put two lines after instead, you can try this:

```python
print('hi', end='\n\n')
```

By default, `print` also separates each thing it prints with a space. You can also change this by passing in the `sep` argument.

```python
print('i', 'want', 'these', 'to', 'be', 'hyphenated', sep='-')
```

Of course, you can use both of these together:

```python
print('peanut', 'butter', 'guacamole', 'salsa', sep='&', end='!!!')
```
