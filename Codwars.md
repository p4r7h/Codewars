## Revered Words
`Complete the solution so that it reverses all of the words within the string passed in. `
```
def reverse_words(s):
    a = s.split(' ')
    return ' '.join(a[::-1])
    ```
