# python docker setup
- reference
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

# save dictionary to a file 
- https://pythonspot.com/save-a-dictionary-to-a-file/
    - import pickle
    - open "wb"  , pickle.dump(f)  , pickle.load(f)
    - https://stackoverflow.com/questions/19201290/how-to-save-a-dictionary-to-a-file/32216025
    - https://www.kite.com/python/answers/how-to-save-a-dictionary-to-a-file-in-python

