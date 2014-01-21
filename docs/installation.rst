Installation
============

Pre-requisites
--------------

For image processing, django-wiki uses the `Pillow
library <https://github.com/python-imaging/Pillow>`_ (a fork of PIL).
The preferred method should be to get a system-wide, pre-compiled
version of Pillow, for instance by getting the binaries from your Linux
distribution repos.

Debian-based Linux Distros
~~~~~~~~~~~~~~~~~~~~~~~~~~

You may find this a bit annoying: On Ubuntu 12.04 and Debian, PIL is
satisfied by installing ``python-imaging``, however Pillow is not! On
later versions of Ubuntu (tested on 13.10), Pillow is satisfied, but PIL
is not. But since PIL no longer compiles on later releases of Ubuntu, we
have opted to use Pillow. The alternative would be that django-wiki's
requirements would be installed and silently fail (i.e. PIL from pip
compiles on Ubuntu 13+ but finds no system libraries for image
processing).

If you are on Ubuntu 13+, you may install a system-wide Pillow-adequate
library like so:

::

    sudo apt-get install python-imaging

After, you can verify that Pillow is satisfied by running
``pip show Pillow``.

::

    $ pip show Pillow
    ---
    Name: Pillow
    Version: 2.0.0
    Location: /usr/lib/python2.7/dist-packages

On Ubuntu 12.04, Debian Wheezy, Jessie etc., you should acquire a
system-wide installation of Pillow, read next section...

Pip installation
~~~~~~~~~~~~~~~~

Firstly, you need to get development libraries that PIP needs before
compiling. For instance on Debian/Ubuntu 12.04:

::

    sudo apt-get install libjpeg8 libjpeg-dev libpng libpng-dev

Later versions of Ubuntu:

::

    sudo apt-get install libjpeg8 libjpeg-dev libpng12-0 libpng12-dev

After that, install with ``sudo pip install Pillow``. You might as well
install Pillow system-wide, because there are little version-specific
dependencies in Django applications when it comes to Pillow, and having
multiple installations of the very same package is a bad practice in
this case.

Mac OS X 10.5+
~~~~~~~~~~~~~~

`Ethan
Tira-Thompson <http://ethan.tira-thompson.com/Mac_OS_X_Ports.html>`_ has
created ports for OS X and made them available as a .dmg installer.
Download and install the universal combo package
`here <http://ethan.tira-thompson.com/Mac_OS_X_Ports_files/libjpeg-libpng%20%28universal%29.dmg>`_.

Once you have the packages installed, you can proceed to the pip
installation. PIL will automatically pick up these libraries and compile
them for django use.

Install
-------

To install the latest stable release:

``pip install git+git://github.com/skakri/django-wiki-base.git``

Configure ``settings.INSTALLED_APPS``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following applications should be listed - NB! it's important to
maintain the order due to database relational constraints:

::

        'django.contrib.humanize',
        'south',
        'mptt',
        'sekizai',
        'sorl.thumbnail',
        'wiki',
        'wiki.plugins.attachments',
        'wiki.plugins.images',
        'wiki.plugins.macros',

Database
~~~~~~~~

To sync and create tables, do:

::

    python manage.py syncdb
    python manage.py migrate

