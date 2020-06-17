# If Statements

`if` statements are a very important part of programming, and you will use them in almost all of your code. A basic `if` statement block will look something like this:

```python
x = 1
if x == 2:
    print('what!')
```

Let's look at exactly what this code does

## If

Once again, the `if` portion of the code looks like this:

```python
if x == 2:
    print('what!')
```

Lets look at it part by part. In the first line, we have `if x == 2:`. What this is doing is checking if the value of x is equal to 2. The reason we use two equal signs instead of one is because one equal sign is for assigning values. If we did used `if x = 2:`, then our code would try to assign x's value equal to 2 instead of checking whether or not x's value is equal to 2.
The part after our `if x == 2:` is `print('what!')`. What this does is if x is indeed equal to 2, then it will print 'what!'. 
So essentially what the `if` statement is doing is saying 

```python
if [this is true]:
    [then do this]
```

But what if I wanted to use multiple `if` statements. What if I wanted something where if the first `if` statement is not true, then it will check a second `if` statement? This is where `elif` comes in.
## Elif

The `elif` portion of our code looked like this:

```python
elif x == 3:
    print('wot')
``` 

This is very similar to our `if` statement. In fact, it basically does the same thing with one small change. `elif` statements must come after `if` statements, because they are essentially saying "if the `if` statement is not true, then run me." Let's look at the full flow of our `if` statement including the `elif`.


```python
x = 1
if x == 2:
    print('what!')
elif x == 3:
    print('wot')
```

What will happen is first the `if` statement will run, checking if x is equal to 2. 1 is not equal to 2, so now we will go to the `elif`. The `elif` then will check if x is equal to 3. If it is,then it will print 'wot'. However, since x does not equal 3, it will not.

You can have as many `elif`'s as you want, but what if you wanted something where if every `if` statement fails, it will do something? This is what an `else` is for.

## Else

An else statement goes last in your `if` statements. What it does is if every `if` and `elif` is false and doesn't run anything, then it will always execute whatever is inside the else. Let's take a look at a full `if` statement.

```python
x = 1
if x == 2:
    print('what!')
elif x == 3:
    print('wot')
else:
    print('ok')
```

We've already seen the `if` and `elif` parts before, and we know since x is not equal to 2 or 3, neither one of those statements will execute. Thats means that the `else` statement will run because neither the `if` statement nor the `elif` statement did. 

Be careful while writing `if` statements! While you can have as many `elif`s as you want, you can only have one `if` and one `else`.  

Now, knowing all of this, what do you think this code will do once it's run?  
