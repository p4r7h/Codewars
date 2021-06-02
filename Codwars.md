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
----------------
##  Multiplication table for number
`Your goal is to return multiplication table for number that is always an integer from 1 to 10.

For example, a multiplication table (string) for number == 5 looks like below:

1 * 5 = 5
2 * 5 = 10
3 * 5 = 15
4 * 5 = 20
5 * 5 = 25
6 * 5 = 30
7 * 5 = 35
8 * 5 = 40
9 * 5 = 45
10 * 5 = 50
`
```
def multi_table(number):
    a = ''
    for i in range(1,11):
        a += "{} * {} = {}\n".format(i,number,i*number)
    return a[:-1]
```
-------
## get character from ASCII Value
`Write a function which takes a number and returns the corresponding ASCII char for that value.`
```
def get_char(c):
    return chr(c) 
```

## Twice as old
`Сalculate how many years ago the father was twice as old as his son (or in how many years he will be twice as old).`

```
def twice_as_old(dad_years_old, son_years_old):
    return abs(dad_years_old - (son_years_old * 2))
    pass
```

## Area or Perimeter
`You are given the length and width of a 4-sided polygon. The polygon can either be a rectangle or a square.
If it is a square, return its area. If it is a rectangle, return its perimeter.`
```
def area_or_perimeter(l , w):
    if l == w : return l**2
    else : return (l+w)*2
```

## String repeat
`Write a function called repeatStr which repeats the given string string exactly n times.`
```
def repeat_str(repeat, string):
    return string*repeat
```


## Enumerable Magic #25 - Take the First N Elements
`Create a method take that accepts a list/array and a number n, and returns a list/array array of the first n elements from the list/array.`
```
def take(arr,n):
    return arr[:n]
    pass
```

## Remove First and Last Character
```
def remove_char(s):
    return s[1:len(s)-1]
```

## Do you speak "English"?
`Given a string of arbitrary length with any ascii characters. Write a function to determine whether the string contains the whole word "English".
The order of characters is important -- a string "abcEnglishdef" is correct but "abcnEglishsef" is not correct.
Upper or lower case letter does not matter -- "eNglisH" is also correct.
Return value as boolean values, true for the string to contains "English", false for it does not.
`
```
def sp_eng(sentence): 
    if 'english' in sentence.lower() :
        return True
    else : return False
```

## String ends with?
`Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string). `
```
def solution(s, e):
    if e == s[-len(e):] or e == '' : return True
    else : return False
    pass
```


### Swap Values
```
def swap_values(arr): 
    arr.reverse()
```
