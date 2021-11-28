- [1. Python Learning](#1-python-learning)
  - [1.1. Advanced Visual Studio Code for Python Developers (2021.11.28)](#11-advanced-visual-studio-code-for-python-developers-20211128)
  - [1.2. Python Virtual Environments: A Primer (2021.11.28)](#12-python-virtual-environments-a-primer-20211128)
  - [1.3. python docker setup](#13-python-docker-setup)
  - [1.4. PyPy: Faster Python With Minimal Effort](#14-pypy-faster-python-with-minimal-effort)
    - [1.4.1. installation](#141-installation)
  - [1.5. Develop Data Visualization Interfaces in Python With Dash (later)](#15-develop-data-visualization-interfaces-in-python-with-dash-later)
  - [1.6. C for Python Programmers (easy for us : useless)](#16-c-for-python-programmers-easy-for-us--useless)
  - [1.7. Common Python Data Structures (Guide)](#17-common-python-data-structures-guide)
  - [1.8. Learn IP Address Concepts With Python's ipaddress Module (helpful info)](#18-learn-ip-address-concepts-with-pythons-ipaddress-module-helpful-info)
  - [1.9. Regular Expressions: Regexes in Python (later)](#19-regular-expressions-regexes-in-python-later)
  - [1.10. Dockerizing Flask With Compose and Machine – From Localhost to the Cloud](#110-dockerizing-flask-with-compose-and-machine--from-localhost-to-the-cloud)
  - [1.11. Object-Oriented Programming (OOP) in Python 3](#111-object-oriented-programming-oop-in-python-3)
  - [1.12. Python Bindings: Calling C or C++ From Python](#112-python-bindings-calling-c-or-c-from-python)
  - [1.13. Functional Programming in Python: When and How to Use It](#113-functional-programming-in-python-when-and-how-to-use-it)
    - [1.13.1. What Is Functional Programming?](#1131-what-is-functional-programming)
    - [1.13.2. How Well Does Python Support Functional Programming?](#1132-how-well-does-python-support-functional-programming)
    - [1.13.3. Defining an Anonymous Function With lambda](#1133-defining-an-anonymous-function-with-lambda)
    - [1.13.4. Applying a Function to an Iterable With map()](#1134-applying-a-function-to-an-iterable-with-map)
      - [1.13.4.1. Calling map() With a Single Iterable](#11341-calling-map-with-a-single-iterable)
      - [1.13.4.2. Calling map() With Multiple Iterables](#11342-calling-map-with-multiple-iterables)
    - [1.13.5. Selecting Elements From an Iterable With filter()](#1135-selecting-elements-from-an-iterable-with-filter)
    - [1.13.6. reduce](#1136-reduce)
  - [1.14. Primer on Python Decorators](#114-primer-on-python-decorators)
    - [1.14.1. Fancy Decorators (later)](#1141-fancy-decorators-later)
  - [1.15. Python and REST APIs: Interacting With Web Services (2021.11.28)](#115-python-and-rest-apis-interacting-with-web-services-20211128)
  - [1.16. Python vs JavaScript for Pythonistas (2021.11.28)](#116-python-vs-javascript-for-pythonistas-20211128)
  - [1.17. Brython: Python in Your Browser (2021.11.25)](#117-brython-python-in-your-browser-20211125)
    - [1.17.1. install on linux](#1171-install-on-linux)
    - [1.17.2. Brython Core Components](#1172-brython-core-components)
    - [1.17.3. Brython Standard Library](#1173-brython-standard-library)
    - [1.17.4. my opinion](#1174-my-opinion)
    - [1.17.5. MISC](#1175-misc)
  - [1.18. Python Code Quality: Tools & Best Practices (2021.11.28) - linter](#118-python-code-quality-tools--best-practices-20211128---linter)
  - [1.19. Getting Started With Testing in Python (2021.11.28)](#119-getting-started-with-testing-in-python-20211128)
    - [1.19.1. Writing Your First Test](#1191-writing-your-first-test)
- [2. Appendix](#2-appendix)
  - [2.1. Python virtualenv : new developing environment for me](#21-python-virtualenv--new-developing-environment-for-me)
  - [2.2. docker basic](#22-docker-basic)
  - [2.3. docker compose](#23-docker-compose)
  - [2.4. vscode](#24-vscode)
    - [2.4.1. markdown TOC](#241-markdown-toc)
    - [2.4.2. vscode updates](#242-vscode-updates)
  - [2.5. New](#25-new)
    - [2.5.1. python](#251-python)
    - [2.5.2. c++](#252-c)
    - [2.5.3. browser](#253-browser)


 -------------------


# 1. Python Learning

## 1.1. Advanced Visual Studio Code for Python Developers (2021.11.28)
- https://realpython.com/advanced-visual-studio-code-python/

- agenda
  - Customize your user interface
    Run and monitor Python tests
    Lint and format your code automatically
    Leverage type annotations and Pylance to write code faster with higher accuracy
    Configure and utilize both local and remote debugging
    Set up data science tools

- [ Python development in Visual Studio Code ](https://realpython.com/python-development-visual-studio-code/)

- Mastering the Visual Studio Code User Interface
  - Keyboard Shortcuts : (menu) File → Preferences → Keyboard Shortcuts

- Customizing the User Interface
  - Using Zen Mode for Focused Work : (menu) View → Appearance → Zen Mode to show a full-screen window
    - ![Zen Mod](https://files.realpython.com/media/vscode-zen-mode.39f6e34b9d84.png)
  - Theming
  - Installing a Better Programming Font

- Setting Up Your Terminal
  - Changing the Default Shell Provider
  - [Virtual Environment](https://realpython.com/python-virtual-environments-a-primer/) Activation in the Terminal
    - Virtual environments are very important for managing multiple dependencies across Python projects.
    - Any commands you run inside the terminal, such as python -m pip install, will be for the activated virtual environment.
  - Installing Oh My Posh : Oh My Posh is one of many libraries for customizing the command prompt of your terminal.
    - ![Terminal](https://files.realpython.com/media/vscode-ohmyposh-terminal.4484c2cdff6d.png)

- Using the Settings Sync Extension : If you use VS Code across multiple computers, you can enable the automatic synchronization of Settings, Keyboard Shortcuts, User Snippets, Extensions, and UI State. (it is not for me!)

- Linting and Formatting
  - Bandit is a linter for security bugs and Flake8 is a linter for style guide compliance.
  - Pylance is an extension that works alongside Python in Visual Studio Code to provide deeper language support and introspection of Python code.

- Testing Your Python Code in Visual Studio Code
  - Python offers plenty of tools to test your code. The Python extension for VS Code supports the most popular test frameworks, unittest and __pytest__.
  - TEST : https://realpython.com/python-testing/
  - CI : https://realpython.com/python-continuous-integration/
  - This wizard adds the configuration options to .vscode/settings.json:
    ```
        "python.testing.pytestEnabled": true,
        "python.testing.pytestArgs": [
            "tests"
        ],
    ```

- Debugging Your Python Scripts in Visual Studio Code
    - ![break point](https://files.realpython.com/media/vscode-debug-breakpoint.eafdcb77613d.png)
    - ![debug menu](https://files.realpython.com/media/vscode-debug-controls.82b8a69e3b32.png)
    - setting watches

- Configuring a Launch File
  - VS Code has a configuration file for launch profiles, .vscode/launch.json. The Python debugger for VS Code can start any launch configuration and attach the debugger to it.
  - example) For an example of working with launch profiles in VS Code, you’ll explore how to use the ASGI server uvicorn to start a FastAPI application.
    - ```$ python -m uvicorn example_app.main:app```
    - launch.json
        ```json
        {
        "configurations": [
            {
            "name": "Python: FastAPI",
            "type": "python",
            "request": "launch",
            "module": "uvicorn",
            "cwd": "${workspaceFolder}",
            "args": [
                "example_app.main:app"
            ],
            }
        ]
        }
        ```
    - If VS Code doesn’t automatically select the right Python environment for you, then you can also declare an explicit path to the appropriate Python interpreter as an option in your __.vscode/launch.json__ file:
        ```json
        {
        "configurations": [
            {
            "name": "Python: FastAPI",
            "type": "python",
            "python": "${workspaceFolder}/venv/bin/python",
            "request": "launch",
            "module": "uvicorn",
            "cwd": "${workspaceFolder}",
            "args": [
                "example_app.main:app"
            ],
            }
        ]
        }
        ```


- Mastering Remote Development
  1. docker
  1. Remote Development With SSH
    - By running Remote-SSH: Open SSH Configuration File in the Command Palette, you can open up the local SSH configuration file. This is a standard SSH config file for you to list hosts, ports, and paths to private keys. The IdentityFile option defaults to ~/.ssh/id_rsa, so the best way to authenticate is a private and public key pair.
    - ![SSH Terminal](https://files.realpython.com/media/vscode-ssh-select.c40298afd273.png)
  3. Remote Development With WSL
 

- Working With Data Science Tools
  - Jupyter Notebooks
  - Using the Rainbow CSV Extension
    - ![Rainbow CSV extension](https://robocrop.realpython.net/?url=https%3A//files.realpython.com/media/vscode-rainbow-csv.c05a3d84ba99.png&w=1060&sig=1c4e7219d705715b03b98d804f7dc72abb2a69ca)

- Adding Bonus Extensions to Visual Studio Code
  - Code Spell Checker : ![Code Spell Checker](https://files.realpython.com/media/vscode-codespell.aec631031c71.png)
  - Docker : ![Docker](https://files.realpython.com/media/vscode-docker-extension.3fea2e3a814e.png)
  - Thunder Client : Thunder Client (rangav.vscode-thunder-client) is an HTTP client and UI for VS Code designed to aid testing of REST APIs.
    - ![Thunder Client](https://files.realpython.com/media/vscode-thunder-client.a101cf598909.png)



## 1.2. Python Virtual Environments: A Primer (2021.11.28)
- https://realpython.com/python-virtual-environments-a-pri

- At its core, the main purpose of Python virtual environments is to create an isolated environment for Python projects.

- Using Virtual Environments
  - ```
    $ pip install virtualenv
    $ mkdir python-virtual-environments && cd python-virtual-environments
    # Python 3
    $ python3 -m venv env
    $ source .venv/bin/activate
    (env) $
    ...
    # do something
    ...
    (env) $ deactivate
    $
    ```
  - what is difference?
    - ```
        $ which python
        /usr/bin/python


        $ source .venv/bin/activate
        (env) $ which python
        /Users/michaelherman/python-virtual-environments/env/bin/python
      ```

- Using Different Versions of Python


## 1.3. python docker setup
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
    - ```cd docker```
    - ```docker build -t rp .```
    - ```docker run --rm -v `pwd`:/app rp python /app/example.py```



## 1.4. PyPy: Faster Python With Minimal Effort
- https://realpython.com/pypy-faster-python/
- PyPy is a very compliant Python interpreter that is a worthy alternative to CPython 2.7, 3.6, and soon 3.7.
- The Python language specification is used in a number of implementations such as CPython (written in C), Jython (written in Java), IronPython (written for .NET), and PyPy (written in Python). 
- [CPython](https://realpython.com/products/cpython-internals-book/)

- python is 40 times slower than pypy in case of below example
- run
    - ```cd pypy```
    - ```time perl s.pl```
    - ```time python3 s.py```
    - ```time pypy s.py```



### 1.4.1. installation
- https://www.pypy.org/download.html
    - tar -xf archive.tar.bz2



## 1.5. Develop Data Visualization Interfaces in Python With Dash (later)
- https://realpython.com/python-dash/
- Dash is an open source framework for building data visualization interfaces. Released in 2017 as a Python library, it’s grown to include implementations for R and Julia. Dash helps data scientists build analytical web applications without requiring advanced web development knowledge.
- Three technologies constitute the core of Dash: 
    1. Flask supplies the web server functionality.
    1. React.js renders the user interface of the web page.
    1. Plotly.js generates the charts used in your application.
- But you don’t have to worry about making all these technologies work together. Dash will do that for you. You just need to write Python, R, or Julia and sprinkle it with a bit of CSS.
![example](https://files.realpython.com/media/barebones_small.929570811d70.jpg)



## 1.6. C for Python Programmers (easy for us : useless)
- https://realpython.com/c-for-python-programmers/
- The purpose of this tutorial is to get an experienced Python programmer up to speed with the basics of the C language and how it’s used in the CPython source code. It assumes you already have an intermediate understanding of Python syntax.



## 1.7. Common Python Data Structures (Guide)
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
        - ```>>> read_only["one"] = 23```    ->>  Traceback (most recent call last):
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
        - `__repr__` method : https://shoark7.github.io/programming/python/difference-between-__repr__-vs-__str__
            - change into human understandable repression
        - str is internal class.   ```help(str)```  vs `__str__` is method (function).
            - ```>>> 3 + 5```  # 내부적으로 밑 문장을 실행!
            - ```>>> (3).__add__(5)```  # '(3)'처럼 ()로 감싸야 한다. 소수와 구별해야 하기 때문이다.
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



## 1.8. Learn IP Address Concepts With Python's ipaddress Module (helpful info)
- https://realpython.com/python-ipaddress-module/



## 1.9. Regular Expressions: Regexes in Python (later)
- https://realpython.com/regex-python/
- https://realpython.com/regex-python-part-2/



## 1.10. Dockerizing Flask With Compose and Machine – From Localhost to the Cloud
- https://realpython.com/dockerizing-flask-with-compose-and-machine-from-localhost-to-the-cloud/
- docker machine is deprecated.



## 1.11. Object-Oriented Programming (OOP) in Python 3
- https://realpython.com/python3-object-oriented-programming/
- Class
    - Conceptually, objects are like the components of a system. Think of a program as a factory assembly line of sorts. At each step of the assembly line a system component processes some material, ultimately transforming raw material into a finished product.
```python
class Dog:
    # Class attribute
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} barks {sound}"

    # Replace .description() with __str__()
    def __str__(self):
        return f"{self.name} is {self.age} years old"
```
    - an instance method’s first parameter is always self.
    - Methods like .__init__() and .__str__() are called dunder methods because they begin and end with double underscores.

- Inherit From Other Classes in Python
    - Child classes can override or extend the attributes and methods of parent classes. 
```python
class JackRussellTerrier(Dog):
    def speak(self, sound="Arf"):
        return f"{self.name} says {sound}"

class Dachshund(Dog):
    def speak(self, sound="Arf"):
        return super().speak(sound)


class Bulldog(Dog):
    pass
```
    - What if you want to determine if miles is also an instance of the Dog class? You can do this with the built-in isinstance().
    - You can access the parent class from inside a method of a child class by using super():


## 1.12. Python Bindings: Calling C or C++ From Python
- https://realpython.com/python-bindings-overview/
- Marshalling Data Types
    - marshalling : The process of transforming the memory representation of an object to a data format suitable for storage or transmission.
- Understanding Mutable and Immutable Values
- Managing Memory

- ctypes is  built into the standard library.
- [python and C binding example : from ctypes import cdll](https://hashcode.co.kr/questions/243/python%EC%97%90%EC%84%9C-cc%EB%B6%80%EB%A5%B4%EA%B8%B0)
    - cd binding ; make      <- works well
    - You’ll start with ctypes, which is a tool in the standard library for creating Python bindings. It provides a low-level toolset for loading shared libraries and marshalling data between Python and C.
- materials : https://github.com/realpython/materials/tree/master/python-bindings
    - need to export function name :  ``` extern "C" { }```
    - [ctypes](https://docs.python.org/ko/3/library/ctypes.html)

- [Test Source Code : pre-existing C and C++](https://github.com/realpython/materials/tree/master/python-bindings)




## 1.13. Functional Programming in Python: When and How to Use It
- https://realpython.com/python-functional-programming/
- Functional programming is a programming paradigm in which the primary method of computation is evaluation of functions. In this tutorial, you’ll explore functional programming in Python.
    - What the functional programming paradigm entails
    - hat it means to say that functions are first-class citizens in Python
    - How to define anonymous functions with the lambda keyword
    - How to implement functional code using map(), filter(), and reduce()

### 1.13.1. What Is Functional Programming?
- In functional programming, a program consists entirely of evaluation of pure functions. Computation proceeds by nested or composed function calls, without changes to state or mutable data.

### 1.13.2. How Well Does Python Support Functional Programming?
- two abilities:
  1. To take another function as an argument
  1. To return another function to its caller
- you can assign a function to a variable. You can then use that variable the same as you would use the function itself:
    ```python
    >>> def func():
    ...     print("I am function func()!")
    ...

    >>> func()
    I am function func()!

    >>> another_name = func
    >>> another_name()
    I am function func()!
    ```
- refer to https://realpython.com/primer-on-python-decorators/
- When you pass a function to another function, the passed-in function sometimes is referred to as a callback because a call back to the inner function can modify the outer function’s behavior.
    ```python
    >>> animals = ["ferret", "vole", "dog", "gecko"]
    >>> sorted(animals, key=len, reverse=True)
    ['ferret', 'gecko', 'vole', 'dog']

    >>> def reverse_len(s):
    ...     return -len(s)
    ...
    >>> sorted(animals, key=reverse_len)
    ['ferret', 'gecko', 'vole', 'dog']
    ```
    - You can check out [How to Use sorted() and sort() in Python](https://realpython.com/python-sort/) for more information on sorting data in Python.


### 1.13.3. Defining an Anonymous Function With lambda
- syntax --> lambda <parameter_list>: <expression>
    ```python
    >>> lambda s: s[::-1]
    <function <lambda> at 0x7fef8b452e18>

    >>> callable(lambda s: s[::-1])
    True

    >>> reverse = lambda s: s[::-1]
    >>> reverse("I am a string")
    'gnirts a ma I'

    >>> (lambda s: s[::-1])("I am a string")
    'gnirts a ma I'

    >>> (lambda x1, x2, x3: (x1 + x2 + x3) / 3)(9, 6, 6)
    7.0
    >>> (lambda x1, x2, x3: (x1 + x2 + x3) / 3)(1.4, 1.1, 0.5)
    1.0
    ```
- The return value from a lambda expression can only be one single expression. A lambda expression can’t contain statements like assignment or return, nor can it contain control structures such as for, while, if, else, or def.
- This implicit tuple packing doesn’t work with an anonymous lambda function

    ```python
    >>> (lambda x: x, x ** 2, x ** 3)(3)
    <stdin>:1: SyntaxWarning: 'tuple' object is not callable; perhaps you missed a comma?
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    NameError: name 'x' is not defined

    >>> (lambda x: (x, x ** 2, x ** 3))(3)
    (3, 9, 27)
    >>> (lambda x: [x, x ** 2, x ** 3])(3)
    [3, 9, 27]
    >>> (lambda x: {1: x, 2: x ** 2, 3: x ** 3})(3)
    {1: 3, 2: 9, 3: 27}
    ```

- [How to Use Python Lambda Functions.](https://realpython.com/python-lambda/)
- Python offers two built-in functions, map() and filter(), that fit the functional programming paradigm.

### 1.13.4. Applying a Function to an Iterable With map()
#### 1.13.4.1. Calling map() With a Single Iterable
- syntax --> map(<f>, <iterable>)
- remember, map() doesn’t return a list. It returns an iterator called a map object. To obtain the values from the iterator, you need to either iterate over it or use list():
    ```python
    >>> animals = ["cat", "dog", "hedgehog", "gecko"]
    >>> iterator = map(reverse, animals)
    >>> iterator
    <map object at 0x7fd3558cbef0>

    >>> iterator = map(reverse, animals)
    >>> for i in iterator:
    ...     print(i)
    ...
    tac
    god
    gohegdeh
    okceg

    >>> iterator = map(reverse, animals)
    >>> list(iterator)
    ['tac', 'god', 'gohegdeh', 'okceg']
    ```
- '1+2+3+4+5'
    ```python
    >>> "+".join([1, 2, 3, 4, 5])
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    TypeError: sequence item 0: expected str instance, int found

    >>> strings = []
    >>> for i in [1, 2, 3, 4, 5]:
    ...     strings.append(str(i))
    ...
    >>> strings
    ['1', '2', '3', '4', '5']
    >>> "+".join(strings)
    '1+2+3+4+5'

    >>> "+".join(map(str, [1, 2, 3, 4, 5]))
    '1+2+3+4+5'
    ```
#### 1.13.4.2. Calling map() With Multiple Iterables
- syntax --> map(<f>, <iterable₁>, <iterable₂>, ..., <iterableₙ>)
    ```python
    >>> def f(a, b, c):
    ...     return a + b + c
    ...

    >>> list(map(f, [1, 2, 3], [10, 20, 30], [100, 200, 300]))
    [111, 222, 333]
    ```
    - ![map with multiple iterables](https://files.realpython.com/media/t.130d7baf2cca.png)

### 1.13.5. Selecting Elements From an Iterable With filter()
- syntax --> filter(<f>, <iterable>)
  - filter(<f>, <iterable>) applies function <f> to each element of <iterable> and returns an iterator that yields all items for which <f> is truthy. Conversely, it filters out all items for which <f> is falsy.
    ```python
    >>> def greater_than_100(x):
    ...     return x > 100
    ...

    >>> list(filter(greater_than_100, [1, 111, 2, 222, 3, 333]))
    [111, 222, 333]

    >>> list(filter(lambda x: x > 100, [1, 111, 2, 222, 3, 333]))
    [111, 222, 333]



    >>> animals = ["cat", "Cat", "CAT", "dog", "Dog", "DOG", "emu", "Emu", "EMU"]

    >>> def all_caps(s):
    ...     return s.isupper()
    ...
    >>> list(filter(all_caps, animals))
    ['CAT', 'DOG', 'EMU']

    >>> list(filter(lambda s: s.isupper(), animals))
    ['CAT', 'DOG', 'EMU']
    ```
### 1.13.6. reduce
- syntax --> reduce(<f>, <iterable>)
    ```python
    >>> def f(x, y):
    ...     return x + y
    ...

    >>> from functools import reduce
    >>> reduce(f, [1, 2, 3, 4, 5])
    15
    ```
    - ![reduce progress](https://files.realpython.com/media/t.5446e98a36c1.png)
- implement filter() using reduce()
    ```python
    >>> numbers = list(range(10))
    >>> numbers
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    >>> def is_even(x):
    ...     return x % 2 == 0
    ...

    >>> list(filter(is_even, numbers))
    [0, 2, 4, 6, 8]

    >>> def custom_filter(function, iterable):
    ...     from functools import reduce
    ...
    ...     return reduce(
    ...         lambda items, value: items + [value] if function(value) else items,
    ...         iterable,
    ...         []
    ...     )
    ...
    >>> list(custom_filter(is_even, numbers))
    [0, 2, 4, 6, 8]
    ```



## 1.14. Primer on Python Decorators
- https://realpython.com/primer-on-python-decorators/
- a higher-order function is a function that does at least one of the following:
    - takes one or more functions as arguments (i.e. procedural parameters),
    - returns a function as its result.
- By definition, a decorator is a function that takes another function and extends the behavior of the latter function without explicitly modifying it.
- functions
  - generally functions are fist class objects.
  - inner function : function can have inner function to use it and return it.
  - return functions from functions
- simple decorators
    ```python
    def my_decorator(func):
        def wrapper():
            print("Something is happening before the function is called.")
            func()
            print("Something is happening after the function is called.")
        return wrapper

    def say_whee():
        print("Whee!")

    say_whee = my_decorator(say_whee)
    ```
    - Syntactic Sugar!
        - First of all, you end up typing the name say_whee three times.
        ```python
        def my_decorator(func):
            def wrapper():
                print("Something is happening before the function is called.")
                func()
                print("Something is happening after the function is called.")
            return wrapper

        @my_decorator
        def say_whee():
            print("Whee!")
        ```
        - So, @my_decorator is just an easier way of saying say_whee = my_decorator(say_whee). It’s how you apply a decorator to a function.
    - Reusing Decorators
        - Recall that a decorator is just a regular Python function. All the usual tools for easy reusability are available
        ```python
        def do_twice(func):
            def wrapper_do_twice():
                func()
                func()
            return wrapper_do_twice

        from decorators import do_twice
        @do_twice
        def say_whee():
            print("Whee!")

        >>> say_whee()
        Whee!
        Whee!
        ```
    - Decorating Functions With Arguments
        ```python
        def do_twice(func):
            def wrapper_do_twice(*args, **kwargs):
                func(*args, **kwargs)
                func(*args, **kwargs)
            return wrapper_do_twice

        from decorators import do_twice
        @do_twice
        def greet(name):
            print(f"Hello {name}")

        >>> greet("World")
        Hello World
        Hello World
        ```
- timing functions usingdecorator
    ```python
    import functools
    import time

    def timer(func):
        """Print the runtime of the decorated function"""
        @functools.wraps(func)
        def wrapper_timer(*args, **kwargs):
            start_time = time.perf_counter()    # 1
            value = func(*args, **kwargs)
            end_time = time.perf_counter()      # 2
            run_time = end_time - start_time    # 3
            print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
            return value
        return wrapper_timer

    @timer
    def waste_some_time(num_times):
        for _ in range(num_times):
            sum([i**2 for i in range(10000)])


    >>> waste_some_time(1)
    Finished 'waste_some_time' in 0.0010 secs

    >>> waste_some_time(999)
    Finished 'waste_some_time' in 0.3260 secs
    ```
- debugging code
    ```python
    import functools

    def debug(func):
        """Print the function signature and return value"""
        @functools.wraps(func)
        def wrapper_debug(*args, **kwargs):
            args_repr = [repr(a) for a in args]                      # 1
            kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]  # 2
            signature = ", ".join(args_repr + kwargs_repr)           # 3
            print(f"Calling {func.__name__}({signature})")
            value = func(*args, **kwargs)
            print(f"{func.__name__!r} returned {value!r}")           # 4
            return value
        return wrapper_debug

    @debug
    def make_greeting(name, age=None):
        if age is None:
            return f"Howdy {name}!"
        else:
            return f"Whoa {name}! {age} already, you are growing up!"

    >>> make_greeting("Benjamin")
    Calling make_greeting('Benjamin')
    'make_greeting' returned 'Howdy Benjamin!'
    'Howdy Benjamin!'

    >>> make_greeting("Richard", age=112)
    Calling make_greeting('Richard', age=112)
    'make_greeting' returned 'Whoa Richard! 112 already, you are growing up!'
    'Whoa Richard! 112 already, you are growing up!'
    ```
- slowing down code
- registering plugins
- is the user logged in?

### 1.14.1. [Fancy Decorators](https://realpython.com/primer-on-python-decorators/#fancy-decorators) (later)
- Decorating Classes
- Nesting Decorators
- Decorators With Arguments
- Both Please, But Never Mind the Bread
- Stateful Decorators
- Classes as Decorators
- Slowing Down Code, Revisited
- Creating Singletons
- Caching Return Values
- Adding Information About Units
- Validating JSON


## 1.15. Python and REST APIs: Interacting With Web Services (2021.11.28)
- https://realpython.com/api-integration-in-python/

- REST Architecture
  - REST stands for representational state transfer and is a software architecture style that defines a pattern for client and server communications over a network. REST provides a set of constraints for software architecture to promote performance, scalability, simplicity, and reliability in the system.
  - REST defines the following architectural constraints:
    - Stateless: The server won’t maintain any state between requests from the client.
    - Client-server: The client and server must be decoupled from each other, allowing each to develop independently.
    - Cacheable: The data retrieved from the server should be cacheable either by the client or by the server.
    - Uniform interface: The server will provide a uniform interface for accessing resources without defining their representation.
    - Layered system: The client may access the resources on the server indirectly through other layers such as a proxy or load balancer.
    - Code on demand (optional): The server may transfer code to the client that it can run, such as JavaScript for a single-page application.


- HTTP Methods
    | HTTP | method	Description |
    |---|---|
    |GET	| Retrieve an existing resource.
    |POST	| Create a new resource.
    |PUT	| Update an existing resource.
    |PATCH	| Partially update an existing resource.
    |DELETE	| Delete a resource.

- install python package
    - ```$ python -m pip install requests```

- GET : read-only
```
>>> import requests
>>> api_url = "https://jsonplaceholder.typicode.com/todos/1"
>>> response = requests.get(api_url)
>>> response.json()
{'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}
>>> response.status_code
200

>>> response.headers["Content-Type"]
'application/json; charset=utf-8'
```

- POST : 
```
>>> import requests
>>> import json
>>> api_url = "https://jsonplaceholder.typicode.com/todos"
>>> todo = {"userId": 1, "title": "Buy milk", "completed": False}
>>> headers =  {"Content-Type":"application/json"}
>>> response = requests.post(api_url, data=json.dumps(todo), headers=headers)
>>> response.json()
{'userId': 1, 'title': 'Buy milk', 'completed': False, 'id': 201}

>>> response.status_code
201
```
    > Note: json.dumps() comes from the json package in the standard library. This package provides useful methods for working with JSON in Python.

- Define Your Endpoints
    | HTTP method	| API endpoint	| Description |
    |---|---|---|
    | GET	| /events/<event_id>/guests	| Get a list of guests.
    | GET	| /events/<event_id>/guests/<guest_id>	| Get a single guest.
    | POST	| /events/<event_id>/guests	| Create a new guest.
    | PUT	| /events/<event_id>/guests/<guest_id>	| Update a guest.
    | PATCH	| /events/<event_id>/guests/<guest_id>	| Partially update a guest.
    | DELETE	| /events/<event_id>/guests/<guest_id>	| Delete a guest.

    > Note: An endpoint shouldn’t contain verbs. Instead, you should select the appropriate HTTP methods to convey the endpoint’s action. For example, the endpoint below contains an unneeded verb:
    - GET /getTransactions
        - Here, get is included in the endpoint when it isn’t needed. The HTTP method GET already provides the semantic meaning for the endpoint by indicating the action. You can remove get from the endpoint:
    - GET /transactions
        - This endpoint contains only a plural noun, and the HTTP method GET communicates the action.


- REST and Python: Tools of the Trade
  - flask
  - django
  - FastAPI


## 1.16. Python vs JavaScript for Pythonistas (2021.11.28)
- https://realpython.com/python-vs-javascript/

- skip javascript description : it emphasize advantages of python. but , it depends on your usage.  if you works on the web , javascript is good also.

- JavaScript vs Python
  - python is general purpose.  but , javascript is used on html of client.

- Memory Model
  - Both languages take advantage of automatic heap memory management to eliminate human error and to reduce cognitive load. Nevertheless, this doesn’t completely free you from the risk of getting a memory leak, and it adds some performance overhead.


## 1.17. Brython: Python in Your Browser (2021.11.25)
- https://realpython.com/brython-python-in-browser/
- Python developers using Flask or Django can also apply the principles of isomorphism to Python, provided that they can run Python in the browser.
- [Brython console](https://brython.info/tests/console.html)    ///  [interactive editor](https://brython.info/tests/editor.html)
###  1.17.1. install on linux
```txt
$ python3 -m venv .venv --prompt brython
$ source .venv/bin/activate
(brython) $ python -m pip install --upgrade pip
Collecting pip
  Downloading pip-20.2.4-py2.py3-none-any.whl (1.5 MB)
     |████████████████████████████████| 1.5 MB 1.3 MB/s
Installing collected packages: pip
  Attempting uninstall: pip
    Found existing installation: pip 20.2.3
    Uninstalling pip-20.2.3:
      Successfully uninstalled pip-20.2.3
(brython) $ python -m pip install brython
Collecting brython
  Downloading brython-3.9.0.tar.gz (1.2 MB)
     |████████████████████████████████| 1.2 MB 1.4 MB/s
Using legacy 'setup.py install' for brython, since package 'wheel'
is not installed.
Installing collected packages: brython
    Running setup.py install for brython ... done
(brython) $ mkdir web
(brython) $ cd web
(brython) $ brython-cli --install
Installing Brython 3.9.0
done
(brython) $ python -m http.server
Serving HTTP on :: port 8000 (http://[::]:8000/) ...
```

- Browser Connect to http.server  (http://lotto645.lge.com:8000/)
  ![Brower Connect to http.server](https://files.realpython.com/media/brython_index.743c41c96830.png)
    - http://lotto645.lge.com:8000/demo.html

### 1.17.2. Brython Core Components
- The core of Brython is contained in brython.js or in brython.min.js, the minimized version of the Brython engine. Both include the following key components:
  - brython() is the main JavaScript function exposed in the JavaScript global namespace. You can’t execute any Python code without calling this function. This is the only JavaScript function that you should have to call explicitly.
  - `__BRYTHON__` is a JavaScript global object that holds all internal objects needed to run Python scripts. This object isn’t used directly when you write Brython applications. If you look at the Brython code, both JavaScript and Python, then you’ll see regular occurrences of `__BRYTHON__`. You don’t need to use this object, but you should be aware of it when you see an error or when you want to debug your code in the browser console.
  - Built-in types are implementations of the Python built-in types in JavaScript. For example, py_int.js, py_string.js and py_dicts.js are respective implementations of int, str and dict.
  - browser is the browser module that exposes the JavaScript objects commonly used in a front-end web application, like the DOM interfaces using document and the browser window using the window object.

### 1.17.3. Brython Standard Library
- brython_stdlib.js exposes the Python standard library. As this file is generated, Brython compiles the Python standard library into JavaScript and concatenates the result into the bundle brython_stdlib.js.

### 1.17.4. my opinion
- ok. if you try the examples , it is good.  But , this is like specific web language. because it is different from pure python.  it is brython , but not python.
  - To manipulate the DOM, Brython uses two operators:
    - <= is a new operator, specific to Brython, that adds a child to a node. You can see a few examples of this usage in display_map(), defined on line 22.
    - + is a substitute for Element.insertAdjacentHTML('afterend') and adds sibling nodes.

### 1.17.5. MISC
- Creating Google Chrome Extensions
- Testing and Debugging Brython

## 1.18. Python Code Quality: Tools & Best Practices (2021.11.28) - linter
- https://realpython.com/python-code-quality/

- Why Does Code Quality Matter?
  - It does not do what it is supposed to do
  - It does contain defects and problems
  - It is difficult to read, maintain, or extend

- How to Improve Python Code Quality
  - Style Guides
    - __PEP 8__ provides coding conventions for Python code. It is fairly common for Python code to follow this style guide. It’s a great place to start since it’s already well-defined.
    - A sister Python Enhancement Proposal, __PEP 257__ describes conventions for Python’s docstrings, which are strings intended to document modules, classes, functions, and methods. As an added bonus, if docstrings are consistent, there are tools capable of generating documentation directly from the code.
  - Linters
    - Linters analyze code to detect various categories of lint. 
      - Logical Lint
        - Code errors
        - Code with potentially unintended results
        - Dangerous code patterns
      - Stylistic Lint
        - Code not conforming to defined conventions
    - What Are My Linter Options For Python?
      - Flake8: Capable of detecting both logical and stylistic lint.
        - PyFlakes / pycodestyle (formerly pep8) / Mccabe
      - Pylama: A code audit tool composed of a large number of linters and other tools for analyzing code.
        - pycodestyle (formerly pep8) / pydocstyle (formerly pep257) / PyFlakes / Mccabe / Pylint / Radon / gjslint

| Linter	| Category	| Description | Time |
|----|----|----|----|
| Pylint	| Logical & Stylistic	| Checks for errors, tries to enforce a coding standard, looks for code smells | 1.16s
| PyFlakes	| Logical	| Analyzes programs and detects various errors | 0.15s
| pycodestyle	| Stylistic	| Checks against some of the style conventions in PEP 8 | 0.14s
| pydocstyle	| Stylistic	| Checks compliance with Python docstring conventions | 0.21s
| Bandit	| Logical	| Analyzes code to find common security issues | 
| MyPy	| Logical	| Checks for optionally-enforced static types | 

- flake
  - ```$ python -m pip install flake8```
  - ```$ flake8 test.py```
  - ```flake8 --ignore E305 --exclude .git,__pycache__ --max-line-length=90```

- black
  - ```$ python -m pip install black```
  - ```$ black test.py```

## 1.19. Getting Started With Testing in Python (2021.11.28)
- https://realpython.com/python-testing/

- Testing Your Code
  - [./test/test_sum.py](https://github.com/cheoljoo/python-learn/blob/main/test/test_sum.py)

- Choosing a Test Runner
  - unittest
  - nose or nose2
  - pytest

- unittest
  - unittest requires that:
    - You put your tests into classes as methods
    - You use a series of special assertion methods in the unittest.TestCase class instead of the built-in assert statement
  - [./test/test_sum_unittest.py](https://github.com/cheoljoo/python-learn/blob/main/test/test_sum_unittest.py)
    1. Import unittest from the standard library
    2. Create a class called TestSum that inherits from the TestCase class
    3. Convert the test functions into methods by adding self as the first argument
    4. Change the assertions to use the self.assertEqual() method on the TestCase class
    1. Change the command-line entry point to call unittest.main()

- pytest
  - pytest supports execution of unittest test cases. The real advantage of pytest comes by writing pytest test cases. pytest test cases are a series of functions in a Python file starting with the name test_.
  - pytest has some other great features:
    - Support for the built-in assert statement instead of using special self.assert*() methods
    - Support for filtering for test cases
    - Ability to rerun from the last failing test
    - An ecosystem of hundreds of plugins to extend the functionality

- Testing in Multiple Environments
  - pip install tox
### 1.19.1. Writing Your First Test
- [project](https://github.com/cheoljoo/python-learn/blob/main/project)
  - ```
    project/
        │
        ├── my_sum/
        │   └── __init__.py
        |
        └── test.py
    ```
  1. Imports sum() from the my_sum package you created
  2. Defines a new test case class called TestSum, which inherits from unittest.TestCase
  3. Defines a test method, .test_list_int(), to test a list of integers. The method .test_list_int() will:
    - Declare a variable data with a list of numbers (1, 2, 3)
    - Assign the result of my_sum.sum(data) to a result variable
    - Assert that the value of result equals 6 by using the .assertEqual() method on the unittest.TestCase class
  4. Defines a command-line entry point, which runs the unittest test-runner .main()

- ```C:\code\python-learn> python -m unittest discover -s project```
  - start  from project with -s option.
  - discover automatically




# 2. Appendix

## 2.1. Python virtualenv : new developing environment for me
- when we use the docker , we do not need it. 
- https://help.dreamhost.com/hc/en-us/articles/115000695551-Installing-and-using-virtualenv-with-Python-3
- (korean link) https://dgkim5360.tistory.com/entry/python-virtualenv-on-linux-ubuntu-and-windows
- (korean link) https://joonyon.tistory.com/135

## 2.2. docker basic
- (korean link) https://junlab.tistory.com/216

## 2.3. docker compose
- (korean link) https://junlab.tistory.com/219
- 일반적인 시스템은 단일 애플리케이션으로 구동이 되지 않습니다. 여러 개의 애플리케이션이 서로 의존성 있게 구성되어 시스템이 이뤄져 있습니다. 그렇다면 흔히 하나의 컨테이너가 하나의 애플리케이션을 담당한다고 하면 여러 개의 컨테이너가 필요로 합니다. 이때 필요한 기술이 도커 컴포즈(Docker Compose)입니다. 도커 컴포즈는 yaml 포맷으로 작성되며 여러 개의 컨테이너의 실행을 한 번에 관리를 할 수 있게 해 줍니다.

## 2.4. vscode
### 2.4.1. markdown TOC

- vscode extension install
    - markdown TOC ->  markdown all in one
      - ^+P -> Markdown All in One : create TOC and update TOC
      - ^+P -> Markdown All in One : add/update section numners
      - ^+P -> Markdown All in One : Update Table of Contents
    - markdown preview ->  markdown preview enhanced
    - markdown lint

### 2.4.2. vscode updates
- 21.11.26 
    - Bracket pair guides can be enabled by setting editor.guides.bracketPairs to true (defaults to false). We added a third option "active" to only show a bracket pair guide for the active bracket pair.
    - Customizable bracket pairs
      - You can now configure bracket pairs for a specific programming language through settings. editor.language.brackets can be used to configure which bracket characters should be matched. If set, editor.language.colorizedBracketPairs independently configures which bracket pairs are colorized when bracket pair colorization or bracket pair guides are enabled.
      ```javascript
"[javascript]": {
    "editor.language.brackets": [
        ["[", "]"],
        ["(", ")"]
    ],
    "editor.language.colorizedBracketPairs": [
        ["[", "]"]
    ]
},
      ```

## 2.5. New
### 2.5.1. python
- https://realpython.com/python-testing/
- https://realpython.com/python-continuous-integration/
- https://realpython.com/advanced-visual-studio-code-python/
- https://realpython.com/python-code-quality/      <- linter
- someip : 
    - https://github.com/jamores/eth-scapy-someip
    - https://pypi.org/project/someip/

### 2.5.2. c++
- https://devblogs.microsoft.com/cppblog/visual-studio-code-c-extension-july-2020-update-doxygen-comments-and-logpoints/
- https://marketplace.visualstudio.com/items?itemName=aaron-bond.better-comments
    - https://github.com/cschlosser/doxdocgen       : we can find source code when we visit the URL in vscode extension.

### 2.5.3. browser
- https://realpython.com/brython-python-in-browser/
- https://realpython.com/python-vs-javascript