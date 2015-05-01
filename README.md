# fancyprint_py
Python convenience package for pretty formatting of ascii console output

## Installing
TODO: fill this section

##Loading Package
```py
from fancyprint import *
```

##Using Package Functions
```py
name = "Joe Blogs"
printkv("name", name)
```
```
"name: Joe Blogs""
```

```py
mu = 36.32348572837228473
sd = 2.953421344345134454
printkv("Mean", mu, fill=25, fill_char=".", rounding=2)
printkv("Standard Deviation", sd, fill=25, fill_char=".", rounding=2)
```
```
"Mean.....................: 36.32"
"Standard Deviation.......: 2.95"
```
