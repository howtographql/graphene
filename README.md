# graphene

# Install

First, is recommended to have a virtual enviroment for running our project:

```sh
# Installing virtualenv-burrito https://github.com/brainsik/virtualenv-burrito
curl -sL https://raw.githubusercontent.com/brainsik/virtualenv-burrito/master/virtualenv-burrito.sh | $SHELL

# Make a new python enviroment
mkvirtualenv howtographene
```

Then, install the dependencies and run the app:

```sh
pip install -r requirements.txt
pip install -r requirements-test.txt
# This will create the DB
python hackernews/manage.py migrate
# This will run the dev server
python hackernews/manage.py runserver
```

# Running Tests

For running the tests you can execute:
```sh
py.test hackernews
```

# Deploying on [Heroku](http://heroku.com)

To get your own Hackernews running on Heroku, click the button below:

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/syrusakbary/graphene)

Fill out the form, and you should be cooking with gas in a few seconds.


## Commands executed

This are the commands executed for creating the skeleton of this project

```
mkvirtualenv howtowgraphene

pip install Django
django-admin startproject hackernews

# Add basic app
python manage.py startapp links
python manage.py startapp users
```
