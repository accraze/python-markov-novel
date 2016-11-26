========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |appveyor| |requires|
        | |coveralls| |codecov|
    * - package
      - |version| |downloads| |wheel| |supported-versions| |supported-implementations|

.. |docs| image:: https://readthedocs.org/projects/python-markov-novel/badge/?style=flat
    :target: https://readthedocs.org/projects/python-markov-novel
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/accraze/python-markov-novel.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/accraze/python-markov-novel

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/accraze/python-markov-novel?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/accraze/python-markov-novel

.. |requires| image:: https://requires.io/github/accraze/python-markov-novel/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/accraze/python-markov-novel/requirements/?branch=master

.. |coveralls| image:: https://coveralls.io/repos/accraze/python-markov-novel/badge.svg?branch=master&service=github
    :alt: Coverage Status
    :target: https://coveralls.io/r/accraze/python-markov-novel

.. |codecov| image:: https://codecov.io/github/accraze/python-markov-novel/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/accraze/python-markov-novel

.. |version| image:: https://img.shields.io/pypi/v/markov-novel.svg?style=flat
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/markov-novel

.. |downloads| image:: https://img.shields.io/pypi/dm/markov-novel.svg?style=flat
    :alt: PyPI Package monthly downloads
    :target: https://pypi.python.org/pypi/markov-novel

.. |wheel| image:: https://img.shields.io/pypi/wheel/markov-novel.svg?style=flat
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/markov-novel

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/markov-novel.svg?style=flat
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/markov-novel

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/markov-novel.svg?style=flat
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/markov-novel


.. end-badges

Write a random novel using markov chains.

* Free software: BSD license

Installation
============

::

    pip install markov-novel

Documentation
=============

https://python-markov-novel.readthedocs.io/

Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
