## Revered Words
`Complete the solution so that it reverses all of the words within the string passed in. `
```
def reverse_words(s):
    a = s.split(' ')
    return ' '.join(a[::-1])
```
--------------
## Keep Hydrated!
`Nathan loves cycling.
Because Nathan knows it is important to stay hydrated, he drinks 0.5 litres of water per hour of cycling.
You get given the time in hours and you need to return the number of litres Nathan will drink, rounded to the smallest value.`

```
def litres(time):
    return time // 2
```
