# Alphabetical Grid
# You need to write a function grid that returns an alphabetical grid of size NxN, where a = 0, b = 1, c = 2....


```
def grid(n):
    if n > -1:
        return '\n'.join(
            (' '.join((chr(((x + y) % 26) + 97)
                for x in range(n))) 
                    for y in range(n))) 
```
