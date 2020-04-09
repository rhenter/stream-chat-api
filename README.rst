========
CHAT API
========

Stream Chat API using Django Rest Framework and Djoser


.. hint:: This project is just an example how create a chat Using Stream Chat API

Requirements
============

This project requires:
    * Python 3.6 or earlier
    * Git
    * virtualenvwrapper, pyenv virtualenv or virtualenv for local development


Installation
============

1. Create a Python environment and clone project repository:

Add you SSH Key

.. code-block:: shell

    $ git clone git@github.com:rhenter/stream-chat-api.git
    $ cd stream-chat-api
    $ mkvirtualenv -p $(which python) chat-api
    $ workon chat-api

Or using pyenv virtualenv

.. code-block:: shell

    $ git clone git@github.com:rhenter/stream-chat-api.git
    $ cd stream-chat-api
    $ pyenv virtualenv chat-api
    $ pyenv activate chat-api

2. Create your local settings file (use local.env as a template):

.. code-block:: shell

    $ cp local.env .env

    Edit .env file to use your settings

.. hint:: It's necessary to change the Stream API credentials by yours according to https://getstream.io/dashboard/


.. code-block:: shell

    STREAM_API_KEY=
    STREAM_API_SECRET=

5. Install the project requirements:

.. code-block:: shell

    $ pip install -r requirements.txt


Database migrations
===================

All migrations SHOULD have a description, so, always use the following command to apply all database migrations:

.. code-block:: shell

    $ python manage.py migrate


Sending a message to the Channel
================================

.. code-block:: shell

    $  python manage.py broadcast --message "Message Test"