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
--------
## Opposites Attract

``
Timmy & Sarah think they are in love, but around where they live, they will only know once they pick a flower each. If one of the flowers has an even number of petals and the other has an odd number of petals it means they are in love.
Write a function that will take the number of petals of each flower and return true if they are in love and false if they aren't.
```
def lovefunc( flower1, flower2 ):
    if flower1 % 2 == 0 and flower2 % 2 == 1 :
        return True
    elif flower1 % 2 == 1 and flower2 % 2 == 0 :
        return True
    else :
        return False
```
