Preamble
========
This is a fork of `Jose D. Montoya's VCNL4010 implementation`_ ported over to VCNL4020, which is Vishay's next iteration of the same proximity sensor as VCNL4010 has reached end of life and production. This code migration was very little work - so most, if not even all, credit goes to them.


.. _Jose D. Montoya's VCNL4010 implementation: https://github.com/jposada202020/MicroPython_VCNL4010

Introduction
============

MicroPython Driver for the Vishay VCNL4020 Proximity and Ambient Light Sensor


THIS HAS NOT YET BEEN REWRITTEN
===============================

Installing with mip
====================



To install using mpremote

.. code-block:: shell

    mpremote mip install github:jposada202020/MicroPython_VCNL4010

To install directly using a WIFI capable board

.. code-block:: shell

    mip.install("github:jposada202020/MicroPython_VCNL4010")


Installing Library Examples
============================

If you want to install library examples:

.. code-block:: shell

    mpremote mip install github:jposada202020/MicroPython_VCNL4010/examples.json

To install directly using a WIFI capable board

.. code-block:: shell

    mip.install("github:jposada202020/MicroPython_VCNL4010/examples.json")


Installing from PyPI
=====================

On supported GNU/Linux systems like the Raspberry Pi, you can install the driver locally `from
PyPI <https://pypi.org/project/micropython-vcnl4010/>`_.
To install for current user:

.. code-block:: shell

    pip3 install micropython-vcnl4010

To install system-wide (this may be required in some cases):

.. code-block:: shell

    sudo pip3 install micropython-vcnl4010

To install in a virtual environment in your current project:

.. code-block:: shell

    mkdir project-name && cd project-name
    python3 -m venv .venv
    source .env/bin/activate
    pip3 install micropython-vcnl4010


Usage Example
=============

Take a look at the examples directory

Documentation
=============
API documentation for this library can be found on `Read the Docs <https://micropython-vcnl4010.readthedocs.io/en/latest/>`_.
