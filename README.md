django-unstructured
================

Background
----------

django-unstructured provides abstract models for use with knowledge base / 
wiki-like systems. It adds versioning and access scope support.

Contributing
------------

If you have a great idea, let me know; for now I'd like to keep everything as
simple as possible.

Dependencies
------------

So far the dependencies are:

 * [django>=1.4](http://www.djangoproject.com)
 * [django-south](http://south.aeracode.org/)
 * [django-mptt>=0.5.3](https://github.com/django-mptt/django-mptt)
 * Python>=2.5<3 (Python 3 not yet supported)

Development
------------

In your Git fork, run `pip install -r requirements.txt` to install the
requirements.

Python compatibility
--------------------

It was compatible with Python 2.5 when I cloned from django-wiki repository
(Jan 2014), but I'm developing on 2.7.
Feel free to contact me/send a pull request if something has broken.

Acknowledgements
----------------

 * [Original wiki developers and maintainers](https://github.com/benjaoming/django-wiki/graphs/contributors)

<!---Illegal PyPi RST data -->
<!---Anything that isn't validly translateable to PyPi RST goes after this line -->

