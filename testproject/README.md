Testing
===========

This project can be run directly with the manage.py script, provided 
that you have checked out the root of the Git repository.

It comes with a prepopulated SQLite database.

Test settings
-------------

Setup
-----

You should link your wiki folder like so

    ln -s ../wiki .

Running
-------

You should be able to immediately run it like this:

    python manage.py runserver --settings=testproject.settings.local

The settings come in a package to administer several test scenarios. For simple purposes, simply edit `local.py`.

Login
-----

Django admin:

Username: admin
Password: admin
