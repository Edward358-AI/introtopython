## Inputting

If we go back to repl, you will remember that big black section on the right side of your     screen being where you printed stuff out last week (We'll refer to that as the console from   now on). That section also has other uses, such as being able to type stuff in there for your program to see. For example, in calculators, your  calculator needs the user to give it some input to know what numbers it needs to add together.

# How Do We Get Input?

In python, the `input()` command returns whatever was typed into the console and you can set  it to a variable. For example, if you wanted to find out your users name, you could do

`name = input()`

If your user then typed in Colin, then name would now have the value 'Colin'. You can also puta message inside the input function's parenthesis to be displayed to the user. For example, ifyou wanted to really make it clear that you wanted to know someone's name, you could do

`name = input('Please enter your name')`

Lets head over to repl and see what this will do.

# What About Integer Input?

Back to our calculator example. the `input()` function is all good and well, however it gives us a string, not an integer. If we wanted to make a calculator, this wouldn't work because    you can't add strings together. Luckily, there is a very simple fix. We can just do:

`foo = int(input())`

Now, we've changed the `input()` function to an integer by just wrapping the `int()` function around it, which changes whatever is inside it's parenthesis to an integer. Be careful though,if `input()` has characters that aren't numbers, like 'hi' or 'hi5', then it won't work!


