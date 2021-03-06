# Homework

With COVID-19 shutting down schools, Mr. Lee has switched grading systems. He now has 3 categories. For any grade `x`, 0 ≤ `x` < 60 is a fail, 60 ≤ `x` < 95 is a pass, and 95 ≤ `x` ≤ 100 is a distinction. However, sometimes Mr. Lee is in a good mood and will pass a student if his grade is ≥50 and <95. Given a student's grade and if Mr. Lee is in a good mood, determine if the student passed without distinction.

## Input Format

There will be one line of input, containing two numbers. The first number is the student's grade. The second number will either be 0 or 1, 0 for Mr. Lee not being in a good mood, and 1 for Mr. Lee being in a good mood.

## Output Format

Print either 'yes' for the student passing without distinction, 'no' for the student not passing, or 'honor' for the student passing with distinction.

## Sample Input

```
82
1
```

## Sample Output

```
yes
```

## Explanation

The student's grade, 82, is ≥50 and <95, which is the passing range for Mr. Lee in a good mood.
