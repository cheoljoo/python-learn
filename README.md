- [1. Python Learning](#1-python-learning)
  - [1.1. Advanced Visual Studio Code for Python Developers (2021.11.28)](#11-advanced-visual-studio-code-for-python-developers-20211128)
  - [1.2. Python Virtual Environments: A Primer (2021.11.28)](#12-python-virtual-environments-a-primer-20211128)
  - [1.3. Documenting Python Code: A Complete Guide (2021.11.28) - docstring](#13-documenting-python-code-a-complete-guide-20211128---docstring)
    - [1.3.1. Basics of Commenting Code](#131-basics-of-commenting-code)
    - [1.3.2. Documenting Your Python Code Base Using Docstrings](#132-documenting-your-python-code-base-using-docstrings)
    - [1.3.3. The Four Main Sections of the docs Folder](#133-the-four-main-sections-of-the-docs-folder)
    - [1.3.4. Documentation Tools and Resources](#134-documentation-tools-and-resources)
  - [1.4. python docker setup](#14-python-docker-setup)
  - [1.5. PyPy: Faster Python With Minimal Effort](#15-pypy-faster-python-with-minimal-effort)
    - [1.5.1. installation](#151-installation)
  - [1.6. Develop Data Visualization Interfaces in Python With Dash (later)](#16-develop-data-visualization-interfaces-in-python-with-dash-later)
  - [1.7. C for Python Programmers (easy for us : useless)](#17-c-for-python-programmers-easy-for-us--useless)
  - [1.8. Common Python Data Structures (Guide)](#18-common-python-data-structures-guide)
  - [1.9. Learn IP Address Concepts With Python's ipaddress Module (helpful info)](#19-learn-ip-address-concepts-with-pythons-ipaddress-module-helpful-info)
  - [1.10. Regular Expressions: Regexes in Python (later)](#110-regular-expressions-regexes-in-python-later)
  - [1.11. Dockerizing Flask With Compose and Machine – From Localhost to the Cloud](#111-dockerizing-flask-with-compose-and-machine--from-localhost-to-the-cloud)
  - [1.12. Object-Oriented Programming (OOP) in Python 3](#112-object-oriented-programming-oop-in-python-3)
  - [1.13. Python Bindings: Calling C or C++ From Python](#113-python-bindings-calling-c-or-c-from-python)
  - [1.14. Functional Programming in Python: When and How to Use It](#114-functional-programming-in-python-when-and-how-to-use-it)
    - [1.14.1. What Is Functional Programming?](#1141-what-is-functional-programming)
    - [1.14.2. How Well Does Python Support Functional Programming?](#1142-how-well-does-python-support-functional-programming)
    - [1.14.3. Defining an Anonymous Function With lambda](#1143-defining-an-anonymous-function-with-lambda)
    - [1.14.4. Applying a Function to an Iterable With map()](#1144-applying-a-function-to-an-iterable-with-map)
      - [1.14.4.1. Calling map() With a Single Iterable](#11441-calling-map-with-a-single-iterable)
      - [1.14.4.2. Calling map() With Multiple Iterables](#11442-calling-map-with-multiple-iterables)
    - [1.14.5. Selecting Elements From an Iterable With filter()](#1145-selecting-elements-from-an-iterable-with-filter)
    - [1.14.6. reduce](#1146-reduce)
  - [1.15. Primer on Python Decorators](#115-primer-on-python-decorators)
    - [1.15.1. Fancy Decorators (later)](#1151-fancy-decorators-later)
  - [1.16. Python and REST APIs: Interacting With Web Services (2021.11.28)](#116-python-and-rest-apis-interacting-with-web-services-20211128)
  - [1.17. Python vs JavaScript for Pythonistas (2021.11.28)](#117-python-vs-javascript-for-pythonistas-20211128)
  - [1.18. Brython: Python in Your Browser (2021.11.25)](#118-brython-python-in-your-browser-20211125)
    - [1.18.1. install on linux](#1181-install-on-linux)
    - [1.18.2. Brython Core Components](#1182-brython-core-components)
    - [1.18.3. Brython Standard Library](#1183-brython-standard-library)
    - [1.18.4. my opinion](#1184-my-opinion)
    - [1.18.5. MISC](#1185-misc)
  - [1.19. Python Code Quality: Tools & Best Practices (2021.11.28) - linter](#119-python-code-quality-tools--best-practices-20211128---linter)
  - [1.20. Getting Started With Testing in Python (2021.11.28)](#120-getting-started-with-testing-in-python-20211128)
    - [1.20.1. Writing Your First Test](#1201-writing-your-first-test)
  - [1.21. Effective Python Testing With Pytest (2021.11.28)](#121-effective-python-testing-with-pytest-20211128)
    - [1.21.1. What Makes pytest So Useful?](#1211-what-makes-pytest-so-useful)
    - [1.21.2. Parametrization: Combining Tests](#1212-parametrization-combining-tests)
    - [1.21.3. coverage : pytest-cov](#1213-coverage--pytest-cov)
  - [1.22. Continuous Integration With Python: An Introduction (2021.11.28)](#122-continuous-integration-with-python-an-introduction-20211128)
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
    - [2.5.4. interfaces](#254-interfaces)
  - [2.6. Python 3.10: Cool New Features for You to Try](#26-python-310-cool-new-features-for-you-to-try)
    - [2.6.1. Structural Pattern Matching](#261-structural-pattern-matching)
    - [2.6.2. Type Unions, Aliases, and Guards](#262-type-unions-aliases-and-guards)
    - [2.6.3. Cool Features](#263-cool-features)


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

## 1.3. Documenting Python Code: A Complete Guide (2021.11.28) - docstring
- https://realpython.com/documenting-python-code/

> “Code is more often read than written.”
  — Guido van Rossum 

> “It doesn’t matter how good your software is, because if the documentation is not good enough, people will not use it.“
  — Daniele Procida

> “Code tells you how; Comments tell you why.”
  — Jeff Atwood (aka Coding Horror)

### 1.3.1. Basics of Commenting Code
- According to PEP 8, comments should have a maximum length of 72 characters.
- Comments to your code should be kept brief and focused. Avoid using long comments when possible. Additionally, you should use the following four essential rules as suggested by Jeff Atwood:
    - Keep comments as close to the code being described as possible. Comments that aren’t near their describing code are frustrating to the reader and easily missed when updates are made.
    - Don’t use complex formatting (such as tables or ASCII figures). Complex formatting leads to distracting content and can be difficult to maintain over time.
    - Don’t include redundant information. Assume the reader of the code has a basic understanding of programming principles and language syntax.
    - Design your code to comment itself. The easiest way to understand code is by reading it. When you design your code using clear, easy-to-understand concepts, the reader will be able to quickly conceptualize your intent.
- Commenting Code via Type Hinting (Python 3.5+)
  - ```python
    def hello_name(name: str) -> str:
        return(f"Hello {name}")
    ```

### 1.3.2. Documenting Your Python Code Base Using Docstrings
- Docstrings Background
  - Python also has the built-in function help() that prints out the objects docstring to the console.
  - ```python
    def say_hello(name):
        print(f"Hello {name}, is it me you're looking for?")

    say_hello.__doc__ = "A simple function that says hello... Richie style"

    --------------------------

    def say_hello(name):
        """A simple function that says hello... Richie style"""
        print(f"Hello {name}, is it me you're looking for?")

    --------------------------

    >>> help(say_hello)
    Help on function say_hello in module __main__:

    say_hello(name)
        A simple function that says hello... Richie style
    ```

- Docstring Types
  - Docstring conventions are described within [PEP 257](https://www.python.org/dev/peps/pep-0257/).
  - ```python
    """This is a quick summary line used as a description of the object."""

    """This is the summary line

    This is the further elaboration of the docstring. Within this section,
    you can elaborate further on details as appropriate for the situation.
    Notice that the summary and the elaboration is separated by a blank new
    line.
    """

    # Notice the blank line above. Code should continue on this line.
    ```

  - Class Docstrings: Class and class methods
    - ```python
        class SimpleClass:
            """Class docstrings go here."""

            def say_hello(self, name: str):
                """Class method docstrings go here."""

                print(f'Hello {name}')
      ```        
    - The class constructor parameters should be documented within the __init__ class method docstring. Individual methods should be documented using their individual docstrings. Class method docstrings should contain the following:
      - A brief description of what the method is and what it’s used for
      - Any arguments (both required and optional) that are passed including keyword arguments
      - Label any arguments that are considered optional or have a default value
      - Any side effects that occur when executing the method
      - Any exceptions that are raised
      - Any restrictions on when the method can be called
    - ```python
        class Animal:
            """
            A class used to represent an Animal

            ...

            Attributes
            ----------
            says_str : str
                a formatted string to print out what the animal says
            name : str
                the name of the animal
            sound : str
                the sound that the animal makes
            num_legs : int
                the number of legs the animal has (default 4)

            Methods
            -------
            says(sound=None)
                Prints the animals name and what sound it makes
            """

            says_str = "A {name} says {sound}"

            def __init__(self, name, sound, num_legs=4):
                """
                Parameters
                ----------
                name : str
                    The name of the animal
                sound : str
                    The sound the animal makes
                num_legs : int, optional
                    The number of legs the animal (default is 4)
                """

                self.name = name
                self.sound = sound
                self.num_legs = num_legs

            def says(self, sound=None):
                """Prints what the animals name is and what sound it makes.

                If the argument `sound` isn't passed in, the default Animal
                sound is used.

                Parameters
                ----------
                sound : str, optional
                    The sound the animal makes (default is None)

                Raises
                ------
                NotImplementedError
                    If no sound is set for the animal or passed in as a
                    parameter.
                """

                if self.sound is None and sound is None:
                    raise NotImplementedError("Silent Animals are not supported!")

                out_sound = self.sound if sound is None else sound
                print(self.says_str.format(name=self.name, sound=out_sound))
      ```
  - Package and Module Docstrings: Package, modules, and functions
    - Package docstrings should be placed at the top of the package’s __init__.py file. 
    - Module docstrings are similar to class docstrings.
  - Script Docstrings: Script and functions
    - Docstrings for scripts are placed at the top of the file and should be documented well enough for users to be able to have a sufficient understanding of how to use the script. 
    - If you use __argparse__, then you can omit parameter-specific documentation, assuming it’s correctly been documented within the help parameter of the argparser.parser.add_argument function.
    - ```python
        """Spreadsheet Column Printer

        This script allows the user to print to the console all columns in the
        spreadsheet. It is assumed that the first row of the spreadsheet is the
        location of the columns.

        This tool accepts comma separated value files (.csv) as well as excel
        (.xls, .xlsx) files.

        This script requires that `pandas` be installed within the Python
        environment you are running this script in.

        This file can also be imported as a module and contains the following
        functions:

            * get_spreadsheet_cols - returns the column headers of the file
            * main - the main function of the script
        """

        import argparse

        import pandas as pd


        def get_spreadsheet_cols(file_loc, print_cols=False):
            """Gets and prints the spreadsheet's header columns

            Parameters
            ----------
            file_loc : str
                The file location of the spreadsheet
            print_cols : bool, optional
                A flag used to print the columns to the console (default is
                False)

            Returns
            -------
            list
                a list of strings used that are the header columns
            """

            file_data = pd.read_excel(file_loc)
            col_headers = list(file_data.columns.values)

            if print_cols:
                print("\n".join(col_headers))

            return col_headers


        def main():
            parser = argparse.ArgumentParser(description=__doc__)
            parser.add_argument(
                'input_file',
                type=str,
                help="The spreadsheet file to pring the columns of"
            )
            args = parser.parse_args()
            get_spreadsheet_cols(args.input_file, print_cols=True)


        if __name__ == "__main__":
            main()
      ```

- Docstring Formats
  - reStructured Text : Official Python documentation standard; Not beginner friendly but feature rich
    - ```python
        """Gets and prints the spreadsheet's header columns

        :param file_loc: The file location of the spreadsheet
        :type file_loc: str
        :param print_cols: A flag used to print the columns to the console
            (default is False)
        :type print_cols: bool
        :returns: a list of strings representing the header columns
        :rtype: list
        """
      ```
  - NumPy/SciPy docstrings : NumPy’s combination of reStructured and Google Docstrings
    - ```python
        """Gets and prints the spreadsheet's header columns

        Parameters
        ----------
        file_loc : str
            The file location of the spreadsheet
        print_cols : bool, optional
            A flag used to print the columns to the console (default is False)

        Returns
        -------
        list
            a list of strings representing the header columns
        """
      ```
### 1.3.3. The Four Main Sections of the docs Folder
- Tutorials: Lessons that take the reader by the hand through a series of steps to complete a project (or meaningful exercise). Geared towards the user’s learning.
- How-To Guides: Guides that take the reader through the steps required to solve a common problem (problem-oriented recipes).
- References: Explanations that clarify and illuminate a particular topic. Geared towards understanding.
- Explanations: Technical descriptions of the machinery and how to operate it (key classes, functions, APIs, and so forth). Think Encyclopedia article.

|	| Most Useful When We’re Studying	| Most Useful When We’re Coding |
|---|----|---|
| Practical Step	| Tutorials	| How-To Guides
| Theoretical Knowledge	| Explanation	| Reference

### 1.3.4. Documentation Tools and Resources
- [MkDocs](https://www.mkdocs.org/)	: A static site generator to help build project documentation using the Markdown language


## 1.4. python docker setup
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



## 1.5. PyPy: Faster Python With Minimal Effort
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



### 1.5.1. installation
- https://www.pypy.org/download.html
    - tar -xf archive.tar.bz2



## 1.6. Develop Data Visualization Interfaces in Python With Dash (later)
- https://realpython.com/python-dash/
- Dash is an open source framework for building data visualization interfaces. Released in 2017 as a Python library, it’s grown to include implementations for R and Julia. Dash helps data scientists build analytical web applications without requiring advanced web development knowledge.
- Three technologies constitute the core of Dash: 
    1. Flask supplies the web server functionality.
    1. React.js renders the user interface of the web page.
    1. Plotly.js generates the charts used in your application.
- But you don’t have to worry about making all these technologies work together. Dash will do that for you. You just need to write Python, R, or Julia and sprinkle it with a bit of CSS.
![example](https://files.realpython.com/media/barebones_small.929570811d70.jpg)



## 1.7. C for Python Programmers (easy for us : useless)
- https://realpython.com/c-for-python-programmers/
- The purpose of this tutorial is to get an experienced Python programmer up to speed with the basics of the C language and how it’s used in the CPython source code. It assumes you already have an intermediate understanding of Python syntax.



## 1.8. Common Python Data Structures (Guide)
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



## 1.9. Learn IP Address Concepts With Python's ipaddress Module (helpful info)
- https://realpython.com/python-ipaddress-module/



## 1.10. Regular Expressions: Regexes in Python (later)
- https://realpython.com/regex-python/
- https://realpython.com/regex-python-part-2/



## 1.11. Dockerizing Flask With Compose and Machine – From Localhost to the Cloud
- https://realpython.com/dockerizing-flask-with-compose-and-machine-from-localhost-to-the-cloud/
- docker machine is deprecated.



## 1.12. Object-Oriented Programming (OOP) in Python 3
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


## 1.13. Python Bindings: Calling C or C++ From Python
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




## 1.14. Functional Programming in Python: When and How to Use It
- https://realpython.com/python-functional-programming/
- Functional programming is a programming paradigm in which the primary method of computation is evaluation of functions. In this tutorial, you’ll explore functional programming in Python.
    - What the functional programming paradigm entails
    - hat it means to say that functions are first-class citizens in Python
    - How to define anonymous functions with the lambda keyword
    - How to implement functional code using map(), filter(), and reduce()

### 1.14.1. What Is Functional Programming?
- In functional programming, a program consists entirely of evaluation of pure functions. Computation proceeds by nested or composed function calls, without changes to state or mutable data.

### 1.14.2. How Well Does Python Support Functional Programming?
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


### 1.14.3. Defining an Anonymous Function With lambda
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

### 1.14.4. Applying a Function to an Iterable With map()
#### 1.14.4.1. Calling map() With a Single Iterable
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
#### 1.14.4.2. Calling map() With Multiple Iterables
- syntax --> map(<f>, <iterable₁>, <iterable₂>, ..., <iterableₙ>)
    ```python
    >>> def f(a, b, c):
    ...     return a + b + c
    ...

    >>> list(map(f, [1, 2, 3], [10, 20, 30], [100, 200, 300]))
    [111, 222, 333]
    ```
    - ![map with multiple iterables](https://files.realpython.com/media/t.130d7baf2cca.png)

### 1.14.5. Selecting Elements From an Iterable With filter()
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
### 1.14.6. reduce
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



## 1.15. Primer on Python Decorators
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

### 1.15.1. [Fancy Decorators](https://realpython.com/primer-on-python-decorators/#fancy-decorators) (later)
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


## 1.16. Python and REST APIs: Interacting With Web Services (2021.11.28)
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


## 1.17. Python vs JavaScript for Pythonistas (2021.11.28)
- https://realpython.com/python-vs-javascript/

- skip javascript description : it emphasize advantages of python. but , it depends on your usage.  if you works on the web , javascript is good also.

- JavaScript vs Python
  - python is general purpose.  but , javascript is used on html of client.

- Memory Model
  - Both languages take advantage of automatic heap memory management to eliminate human error and to reduce cognitive load. Nevertheless, this doesn’t completely free you from the risk of getting a memory leak, and it adds some performance overhead.


## 1.18. Brython: Python in Your Browser (2021.11.25)
- https://realpython.com/brython-python-in-browser/
- Python developers using Flask or Django can also apply the principles of isomorphism to Python, provided that they can run Python in the browser.
- [Brython console](https://brython.info/tests/console.html)    ///  [interactive editor](https://brython.info/tests/editor.html)
###  1.18.1. install on linux
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

### 1.18.2. Brython Core Components
- The core of Brython is contained in brython.js or in brython.min.js, the minimized version of the Brython engine. Both include the following key components:
  - brython() is the main JavaScript function exposed in the JavaScript global namespace. You can’t execute any Python code without calling this function. This is the only JavaScript function that you should have to call explicitly.
  - `__BRYTHON__` is a JavaScript global object that holds all internal objects needed to run Python scripts. This object isn’t used directly when you write Brython applications. If you look at the Brython code, both JavaScript and Python, then you’ll see regular occurrences of `__BRYTHON__`. You don’t need to use this object, but you should be aware of it when you see an error or when you want to debug your code in the browser console.
  - Built-in types are implementations of the Python built-in types in JavaScript. For example, py_int.js, py_string.js and py_dicts.js are respective implementations of int, str and dict.
  - browser is the browser module that exposes the JavaScript objects commonly used in a front-end web application, like the DOM interfaces using document and the browser window using the window object.

### 1.18.3. Brython Standard Library
- brython_stdlib.js exposes the Python standard library. As this file is generated, Brython compiles the Python standard library into JavaScript and concatenates the result into the bundle brython_stdlib.js.

### 1.18.4. my opinion
- ok. if you try the examples , it is good.  But , this is like specific web language. because it is different from pure python.  it is brython , but not python.
  - To manipulate the DOM, Brython uses two operators:
    - <= is a new operator, specific to Brython, that adds a child to a node. You can see a few examples of this usage in display_map(), defined on line 22.
    - + is a substitute for Element.insertAdjacentHTML('afterend') and adds sibling nodes.

### 1.18.5. MISC
- Creating Google Chrome Extensions
- Testing and Debugging Brython

## 1.19. Python Code Quality: Tools & Best Practices (2021.11.28) - linter
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
  - ```$ flake8 --ignore E305 --exclude .git,__pycache__ --max-line-length=90```
  - ```$ flake8 --statistics```   : The --statistics option gives you an overview of how many times a particular error happened. 

- black
  - ```$ python -m pip install black```
  - ```$ black test.py```

## 1.20. Getting Started With Testing in Python (2021.11.28)
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
### 1.20.1. Writing Your First Test
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


## 1.21. Effective Python Testing With Pytest (2021.11.28)
- https://realpython.com/pytest-python-testing/

### 1.21.1. What Makes pytest So Useful?
- Less Boilerplate
  - Arrange, or set up, the conditions for the test
  - Act by calling some function or method
  - Assert that some end condition is true

- [pytest](https://github.com/cheoljoo/python-learn/blob/main/pytest)
  - ```C:\code\python-learn\pytest> python -m unittest discover```
    - ```
        F.
        ======================================================================
        FAIL: test_always_fails (test_with_unittest.TryTesting)
        ----------------------------------------------------------------------
        Traceback (most recent call last):
        File "C:\code\python-learn\pytest\test_with_unittest.py", line 10, in test_always_fails
            self.assertTrue(False)
        AssertionError: False is not true

        ----------------------------------------------------------------------
        Ran 2 tests in 0.002s

        FAILED (failures=1)
      ```
  - ```C:\code\python-learn\pytest> pytest```
    - ```
        ================================== test session starts ==================================
        platform win32 -- Python 3.10.0, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
        rootdir: C:\code\python-learn\pytest
        collected 2 items                                                                        

        test_with_unittest.py F.                                                           [100%]

        ======================================= FAILURES ========================================
        _____________________________ TryTesting.test_always_fails ______________________________

        self = <test_with_unittest.TryTesting testMethod=test_always_fails>

            def test_always_fails(self):
        >       self.assertTrue(False)
        E       AssertionError: False is not true

        test_with_unittest.py:10: AssertionError
        ================================ short test summary info ================================
        FAILED test_with_unittest.py::TryTesting::test_always_fails - AssertionError: False is ...
        ============================== 1 failed, 1 passed in 0.46s ==============================
      ```
    - A dot (.) means that the test passed.
    - An F means that the test has failed.
    - An E means that the test raised an unexpected exception.

### 1.21.2. Parametrization: Combining Tests 
- pytest.mark.parametrize
  - ```python
    # content of test_expectation.py
    import pytest

    # @pytest.mark.parametrize는 이거 선언한 바로 아래 test에만 적용되는 것으로 보인다.
    @pytest.mark.parametrize("x", [0, 1])
    @pytest.mark.parametrize("y", [2, 3, 4])
    def test_foo(x, y):
        #pass
        assert x*y == x*2

    @pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+4", 6), ("6*9", 42)])
    def test_eval(test_input, expected):
        assert eval(test_input) == expected
    ```
  - duration report : --durations
    - run : ```C:\code\python-learn\pytest> pytest -q .\test_expectation.py --durations=1 -vv```

### 1.21.3. coverage : pytest-cov
- [coverage.py](https://coverage.readthedocs.io/en/6.2/)
  - ```$ python -m pip install coverage```
  - ```C:\code\python-learn\pytest> coverage rum -m pytest -q .\test_expectation.py```
  - ```C:\code\python-learn\pytest> coverage report -m```
    - ```txt
      C:\code\python-learn\pytest> coverage report -m
      Name                  Stmts   Miss  Cover   Missing
      ---------------------------------------------------
      test_expectation.py       8      0   100%
      ---------------------------------------------------
      TOTAL                     8      0   100%
      ```
  - ```C:\code\python-learn\pytest> coverage html```
    - open htmlcov/index.html in your browser

- pytest-cov
  - ```C:\code\python-learn\pytest> python -m pip install pytest-cov```
  - ```C:\code\python-learn\pytest> pytest -v --cov```
    - ```txt
        ---------- coverage: platform win32, python 3.10.0-final-0 -----------
        Name                     Stmts   Miss  Cover
        --------------------------------------------
        test_expectation.py          8      0   100%
        test_lessThan5.py            8      0   100%
        test_with_unittest2.py       8      0   100%
        test_with_unittest.py        6      0   100%
        --------------------------------------------
        TOTAL                       30      0   100%
      ```


## 1.22. Continuous Integration With Python: An Introduction (2021.11.28)
- https://realpython.com/python-continuous-integration/

- Continuous integration (CI) is the practice of frequently building and testing each change done to your code automatically and as early as possible. Prolific developer and author Martin Fowler defines CI as follows
> “Continuous Integration is a software development practice where members of a team integrate their work frequently, usually each person integrates at least daily - leading to multiple integrations per day. Each integration is verified by an automated build (including test) to detect integration errors as quickly as possible.” [Source](https://martinfowler.com/articles/continuousIntegration.html)

- Conversely, you’ll spend more time:
    1. Solving interesting problems
    1. Writing awesome code with your team
    1. Co-creating amazing products that provide value to users

- On a team level, it allows for a better engineering culture, where you deliver value early and often. Collaboration is encouraged, and bugs are caught much sooner. Continuous integration will:
  - Make you and your team faster
  - Give you confidence that you’re building stable software with fewer bugs
  - Ensure that your product works on other machines, not just your laptop
  - Eliminate a lot of tedious overhead and let you focus on what matters
  - Reduce the time spent resolving conflicts (when different people modify the same code)

- to get external package dependancy
  - ```$ pip freeze > requirements.txt```

- Connect to CircleCI
  - It requires a .circleci folder within your repo and a configuration file inside it. A configuration file contains instructions for all the steps that the build server needs to execute. CircleCI expects this file to be called config.yml.
  - In a YAML file, there are three basic ways to represent data:
    - Mappings (key-value pairs)
    - Sequences (lists)
    - Scalars (strings or numbers)
  - ```yaml
    # Python CircleCI 2.0 configuration file
    version: 2
    jobs:
    build:
        docker:
        - image: circleci/python:3.7

        working_directory: ~/repo

        steps:
        # Step 1: obtain repo from GitHub
        - checkout
        # Step 2: create virtual env and install dependencies
        - run:
            name: install dependencies
            command: |
                python3 -m venv venv
                . venv/bin/activate
                pip install -r requirements.txt
        # Step 3: run linter and tests
        - run:
            name: run tests
            command: |
                . venv/bin/activate
                flake8 --exclude=venv* --statistics
                pytest -v --cov=calculator
    ```
  - CircleCI maintains [pre-built Docker images](https://circleci.com/docs/2.0/circleci-images/) for several programming languages. In the above configuration file, you have specified a Linux image that has Python already installed. That image will create a container in which everything else happens.



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

### 2.5.4. interfaces
- https://realpython.com/python-interface/


## 2.6. Python 3.10: Cool New Features for You to Try
### 2.6.1. Structural Pattern Matching
- Patterns are at the center of structural pattern matching. In this section, you’ll learn about some of the different kinds of patterns that exist:
    - Mapping patterns match mapping structures like dictionaries.
    - Sequence patterns match sequence structures like tuples and lists.
    - Capture patterns bind values to names.
      - ```python
            def sum_list(numbers):
                match numbers:
                    case []:
                        return 0
                    case [int(first) | float(first), *rest]:   # OR  (|)  
                        # sequence pattern [ first , *rest ] 
                        # class pattern int(first) :  pattern only matches if the value is an integer. 
                        return first + sum_list(rest)
                    case _:      # wildcard pattern
                        raise ValueError(f"Can only sum lists of numbers")
        ```
    - AS patterns bind the value of subpatterns to names.
    - OR patterns match one of several different subpatterns.
    - Wildcard patterns match anything.
    - Class patterns match class structures.
    - Value patterns match values stored in attributes.
    - Literal patterns match literal values.
      - ```python
            def greet(name):
                match name:
                    case "Guido":    # literal pattern
                        print("Hi, Guido!")
                    case _:
                        print("Howdy, stranger!")
        ```
- example : if elif else -> match
  - ```python
        def fizzbuzz(number):
            mod_3 = number % 3
            mod_5 = number % 5

            if mod_3 == 0 and mod_5 == 0:
                return "fizzbuzz"
            elif mod_3 == 0:
                return "fizz"
            elif mod_5 == 0:
                return "buzz"
            else:
                return str(number)
        #---------  if elif else -> match  ------------
        def fizzbuzz(number):
            mod_3 = number % 3
            mod_5 = number % 5

            match (mod_3, mod_5):
                case (0, 0):
                    return "fizzbuzz"
                case (0, _):
                    return "fizz"
                case (_, 0):
                    return "buzz"
                case _:
                    return str(number)
        ```

### 2.6.2. Type Unions, Aliases, and Guards
- static typing system
    ```python
    def mean(numbers: list[float | int]) -> float:
        return sum(numbers) / len(numbers)
    ```
- type aliases
    ```python
    from typing import TypeAlias

    Card: TypeAlias = tuple[str, str]
    Deck: TypeAlias = list[Card]
    ```

### 2.6.3. Cool Features
- Python 3.10, you can activate a warning that will tell you when a text file is opened without a specified encoding.
  - utf-8


