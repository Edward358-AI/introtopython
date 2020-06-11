##Fancy Outputting

We've already learned the print statement. Just to jog your memory, it looks like this:

`print()`

The print statement will print whatever is inside its parenthesis.

However, what if we wanted to get fancy with it? Lets say you have a variable `name` which stores someones name. What if I wanted to print out 'Hello [value stored in `name`]. My name is pythonman.' For example, if `name` stored 'Chris', you'd print out 'Hello Chris. My name is pythonman.'

# String Interpolation

The way we do this is with something called string interpolation. That's just fancy terminology for putting variable values in strings. Still using our name example, the way we'd put the `name` variable into the string we want to print out is:

print(f'Hello {name}. My name is pythonman')

If we put the letter f before our single quotes, we can then enclose our variables, in this case `name` inside curly brackets (these things {}). That allows us to put the value stored in our variable directly into the string.

Lets go to repl and try some things out.

# Escape sequences

What if I were writing some code to play hangman? I would have to print out this guy:

 o
/|\
/ \

Let's try to do that and see what happens.

It gives us an error. The reason is because the '\' character is a special character called an escape sequence. Escape sequences mark the start of special characters in strings, such as '\n' which is an end line character. A couple escape sequence examples are:

'\\\' which gives us just a normal backslash character
'\n' which gives us an end line
'\a' which makes a sound
'\h' which gives a horizontal tab
'\v' which gives a vertical tab

Lets try some of these out in repl

#End of String Character

Lastly, you may notice that the `print()` statement always gives prints and then puts you on a new line. This is because the default last character that is printed is the '\n' character. We can easily change this by doing 

`print('hi', end = '')`

What the `end = ''` does is set the end of string character to ''. Lets see what this does in repl.

We can set the end to anything, as long as it's a string (including escape sequences). Lets try that out too.
