# Python Learning
## python docker setup
- https://realpython.com/tutorials/docker/
- https://realpython.com/python-versions-docker/
- Dockerfile
```dockerfile
FROM python:3.7.5-slim

# Set up and activate virtual environment
ENV VIRTUAL_ENV "/venv"
RUN python -m venv $VIRTUAL_ENV
ENV PATH "$VIRTUAL_ENV/bin:$PATH"

# Python commands run inside the virtual environment
RUN pip install --upgrade pip
RUN python -m pip install \
        parse \
        jira \
        realpython-reader
# RUN python example.py
WORKDIR "/app"
```

- run
    - docker build -t rp .
    - docker run --rm -v `pwd`:/app rp python /app/example.py



## PyPy: Faster Python With Minimal Effort
- https://realpython.com/pypy-faster-python/
- PyPy is a very compliant Python interpreter that is a worthy alternative to CPython 2.7, 3.6, and soon 3.7.
- The Python language specification is used in a number of implementations such as CPython (written in C), Jython (written in Java), IronPython (written for .NET), and PyPy (written in Python). 
- [CPython](https://realpython.com/products/cpython-internals-book/)

- python is 40 times slower than pypy in case of below example

### installation
- https://www.pypy.org/download.html
    - tar -xf archive.tar.bz2



## Develop Data Visualization Interfaces in Python With Dash (later)
- https://realpython.com/python-dash/
- Dash is an open source framework for building data visualization interfaces. Released in 2017 as a Python library, it’s grown to include implementations for R and Julia. Dash helps data scientists build analytical web applications without requiring advanced web development knowledge.
- Three technologies constitute the core of Dash: 
    1. Flask supplies the web server functionality.
    1. React.js renders the user interface of the web page.
    1. Plotly.js generates the charts used in your application.
- But you don’t have to worry about making all these technologies work together. Dash will do that for you. You just need to write Python, R, or Julia and sprinkle it with a bit of CSS.
![example](https://files.realpython.com/media/barebones_small.929570811d70.jpg)



## C for Python Programmers (easy for us : useless)
- https://realpython.com/c-for-python-programmers/
- The purpose of this tutorial is to get an experienced Python programmer up to speed with the basics of the C language and how it’s used in the CPython source code. It assumes you already have an intermediate understanding of Python syntax.



## Common Python Data Structures (Guide)
- https://realpython.com/python-data-structures/
- Dictionaries, Maps, and Hash Tables
    - collections.OrderedDict: Remember the Insertion Order of Keys
        - import collections
        - d = collections.OrderedDict(one=1, two=2, three=3)
    - collections.defaultdict: Return Default Values for Missing Keys
        ```python
        from collections import defaultdict
        dd = defaultdict(list)
        >>> # Accessing a missing key creates it and
        >>> # initializes it using the default factory,
        >>> # i.e. list() in this example:
        ```
    - collections.ChainMap: Search Multiple Dictionaries as a Single Mapping (grouping in ppt)
        - The collections.ChainMap data structure groups multiple dictionaries into a single mapping.
    - types.MappingProxyType: A Wrapper for Making Read-Only Dictionaries
        - read_only = MappingProxyType(writable)
        - >>> read_only["one"] = 23    ->>  Traceback (most recent call last):
- Array Data Structures
    - list: Mutable Dynamic Arrays
    - tuple: Immutable Containers
    - array.array: Basic Typed Arrays
        - Python’s array module provides space-efficient storage of basic C-style data types like bytes, 32-bit integers, floating-point numbers, and so on.
    - str: Immutable Arrays of Unicode Characters
    - bytes: Immutable Arrays of Single Bytes
    - bytearray: Mutable Arrays of Single Bytes
- Records, Structs, and Data Transfer Objects
    - Compared to arrays, record data structures provide a fixed number of fields. Each field can have a name and may also have a different type.
    - dict: Simple Data Objects
        - Python dictionaries store an arbitrary number of objects, each identified by a unique key.
        ```python
        >>> car1 = {
        ...     "color": "red",
        ...     "mileage": 3812.4,
        ...     "automatic": True,
        ... }
        ```
    - tuple: Immutable Groups of Objects
    - Write a Custom Class: More Work, More Control
        - class : Fields stored on classes are mutable, and new fields can be added freely, which you may or may not like. It’s possible to provide more access control and to create read-only fields using the @property decorator, but once again, this requires writing more glue code.
            ```python
            >>> class Car:
            ...     def __init__(self, color, mileage, automatic):
            ...         self.color = color
            ...         self.mileage = mileage
            ...         self.automatic = automatic
            ```
        - __repr__ method : https://shoark7.github.io/programming/python/difference-between-__repr__-vs-__str__
            - change into human understandable repression
        - str is internal class.   ```help(str)```  vs __str__ is method (function).
            - >>> 3 + 5  # 내부적으로 밑 문장을 실행!
            - >>> (3).__add__(5)  # '(3)'처럼 ()로 감싸야 한다. 소수와 구별해야 하기 때문이다.
    - dataclasses.dataclass: Python 3.7+ Data Classes
        - They provide an excellent alternative to defining your own data storage classes from scratch.
        
            ```python
            >>> from dataclasses import dataclass
            >>> @dataclass
            ... class Car:
            ...     color: str
            ...     mileage: float
            ...     automatic: bool
            ```
    - collections.namedtuple: Convenient Data Objects. (Python 2.6+)
        - dictionary is better. (charles)
    - typing.NamedTuple: Improved Namedtuples
    - struct.Struct: Serialized C Structs
        - The struct.Struct class converts between Python values and C structs serialized into Python bytes objects. For example, it can be used to handle binary data stored in files or coming in from network connections.
- Sets and Multisets
    - frozenset: Immutable Sets
    - collections.Counter: Multisets
- Stacks (LIFOs)
    - push / pop
    - DFS
    - list: Simple, Built-In Stacks
    - collections.deque: Fast and Robust Stacks (doubly linked list)
    - queue.LifoQueue: Locking Semantics for Parallel Computing
        - The LifoQueue stack implementation in the Python standard library is synchronized and provides locking semantics to support multiple concurrent producers and consumers.
- Queues (FIFOs)
    - BFS
    - Scheduling algorithms often use priority queues internally. These are specialized queues. Instead of retrieving the next element by insertion time, a priority queue retrieves the highest-priority element. The priority of individual elements is decided by the queue based on the ordering applied to their keys.
    - list: Terribly Sloooow Queues
    - collections.deque: Fast and Robust Queues
    - queue.Queue: Locking Semantics for Parallel Computing
    - multiprocessing.Queue: Shared Job Queues
        - multiprocessing.Queue is a shared job queue implementation that allows queued items to be processed in parallel by multiple concurrent workers. Process-based parallelization is popular in CPython due to the global interpreter lock (GIL) that prevents some forms of parallel execution on a single interpreter process.
- Priority Queues
    - A priority queue is a container data structure that manages a set of records with totally-ordered keys to provide quick access to the record with the smallest or largest key in the set.
    - Priority queues are commonly used for dealing with scheduling problems. For example, you might use them to give precedence to tasks with higher urgency.
    - **queue.PriorityQueue stands out from the pack with a nice object-oriented interface and a name that clearly states its intent. It should be your preferred choice.**
    - **If you’d like to avoid the locking overhead of queue.PriorityQueue, then using the heapq module directly is also a good option.**



## Learn IP Address Concepts With Python's ipaddress Module (helpful info)
- https://realpython.com/python-ipaddress-module/



## Regular Expressions: Regexes in Python (later)
- https://realpython.com/regex-python/
- https://realpython.com/regex-python-part-2/



## Dockerizing Flask With Compose and Machine – From Localhost to the Cloud
- https://realpython.com/dockerizing-flask-with-compose-and-machine-from-localhost-to-the-cloud/
- docker machine is deprecated.



## Object-Oriented Programming (OOP) in Python 3
- https://realpython.com/python3-object-oriented-programming/

## Python Bindings: Calling C or C++ From Python
- https://realpython.com/python-bindings-overview/

## Functional Programming in Python: When and How to Use It
- https://realpython.com/python-functional-programming/

## Python and REST APIs: Interacting With Web Services
- https://realpython.com/api-integration-in-python/

## Brython: Python in Your Browser
- https://realpython.com/brython-python-in-browser/


# Appendix for korean

## Python virtualenv : new developing environment for me
- when we use the docker , we do not need it. 
- https://help.dreamhost.com/hc/en-us/articles/115000695551-Installing-and-using-virtualenv-with-Python-3
- (korean link) https://dgkim5360.tistory.com/entry/python-virtualenv-on-linux-ubuntu-and-windows
- (korean link) https://joonyon.tistory.com/135

## docker basic
- (korean link) https://junlab.tistory.com/216

## docker compose
- (korean link) https://junlab.tistory.com/219
- 일반적인 시스템은 단일 애플리케이션으로 구동이 되지 않습니다. 여러 개의 애플리케이션이 서로 의존성 있게 구성되어 시스템이 이뤄져 있습니다. 그렇다면 흔히 하나의 컨테이너가 하나의 애플리케이션을 담당한다고 하면 여러 개의 컨테이너가 필요로 합니다. 이때 필요한 기술이 도커 컴포즈(Docker Compose)입니다. 도커 컴포즈는 yaml 포맷으로 작성되며 여러 개의 컨테이너의 실행을 한 번에 관리를 할 수 있게 해 줍니다.
- 
