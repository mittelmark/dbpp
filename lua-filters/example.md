---
title: "Long Title"
author: Detlef Groth
date: Wed Feb 1 16:45:41 2023
abstract: >
    Some abstract ...
    on several lines...
py:
    cache: true
    eval: true
---

## Introduction

Here today's date calculated in Python:  `py import datetime;print(datetime.date.today())`

test is *this*.

```{.py}
z = 0
print(z)
```

Next chunk!

```{.py}
x = 1
print(x)
```


```{.py}
y = 2
print(y)
print(dir())
print(z)
```

```{.py cache=false}
k=1
print(dir())
```

## EOF
