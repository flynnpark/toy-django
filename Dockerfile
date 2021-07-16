FROM python:3
ENV PYTHONUNBUFFERED 1
WORKDIR /app
RUN pip install pipenv
COPY Pipfile /app/
RUN pipenv install --system --skip-lock
COPY . /app/
EXPOSE 8000
