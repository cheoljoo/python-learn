# time consumption
- PyPy is a very compliant Python interpreter that is a worthy alternative to CPython 2.7, 3.6, and soon 3.7.
- The Python language specification is used in a number of implementations such as CPython (written in C), Jython (written in Java), IronPython (written for .NET), and PyPy (written in Python). 
- [CPython](https://realpython.com/products/cpython-internals-book/)

- python is 40 times slower than pypy in case of below example.
    - python is twice slower than perl in case of below example. (i love twice)

- source (s.py)
```python
total = 0
for i in range(1, 10000):
    for j in range(1, 10000):
        total += i + j

print(f"The result is {total}")
```

- pypy
```txt
time ./pypy s.py
The result is 999800010000

real    0m0.253s
user    0m0.215s
sys     0m0.020s
```

- python3 (s.py)
```txt
time python3 s.py
The result is 999800010000

real    0m11.088s
user    0m11.084s
sys     0m0.004s
```

- perl (s.pl)
```txt
 time perl s.pl
The result is 1000100000000

real    0m6.772s
user    0m6.767s
sys     0m0.004s
```

### installation
- https://www.pypy.org/download.html
    - tar -xf archive.tar.bz2

