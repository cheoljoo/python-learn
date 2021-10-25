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
