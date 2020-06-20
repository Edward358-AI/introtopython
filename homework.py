print('What is your grade?')
grade = int(input())
print('What is Mr Lee\'s mood? 1-good 0-bad')
mood = int(input())

if mood == 0:
    if (grade <= 0) and (grade < 60):
        print('fail')
    elif (grade >= 60) and (grade < 95):
        print('pass')
    elif grade >= 95:
        print('honor')
elif mood == 1:
    if (grade >= 0) and (grade < 50):
        print('fail')
    elif (grade >= 50) and (grade < 95):
        print('pass')
    elif grade >= 95:
        print('honor')
