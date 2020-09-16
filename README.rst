Mijn Simpel (Python) Client
===========================

Access `mijn.simpel.nl`_ from Python.

.. _mijn.simpel.nl: https://mijn.simpel.nl


Installation
------------

Install the cli (and the Python module `mijn_simpel`):

..
    pip install .


Using CLI
---------

The cli goes with a `--help`, so try:

::
    mijn-simpel --help

    Usage: mijn-simpel [OPTIONS] COMMAND [ARGS]...
    
    Options:
      --cookie-jar TEXT  Cookie jar for session storing.  [default:
                         (~/.config/mijn-simpel-cookie)]
    
      --help             Show this message and exit.
    
    Commands:
      login          Login to service.
      subscription   Information for subscription.
      subscriptions  List subscriptions.

It also recognize these environment variables:
# `MIJN_SIMPEL_USERNAME`
# `MIJN_SIMPEL_PASSWORD`
# `MIJN_SIMPEL_SUBSCRIPTION_ID`
# `MIJN_SIMPEL_COOKIE_JAR`


Using in Python
---------------

Please check [mijn_simpel/cli.py](mijn_simpel/cli.py) for the example.


Hacking
-------

Try installing with:

::
    pip install -e .

And then you can modify the source code and use it right away.
