===========
Bib Cleaner
===========


.. image:: https://img.shields.io/pypi/v/bib_cleaner.svg
        :target: https://pypi.python.org/pypi/bib_cleaner

.. image:: https://img.shields.io/travis/sriki18/bib_cleaner.svg
        :target: https://travis-ci.org/sriki18/bib_cleaner

.. image:: https://readthedocs.org/projects/bib-cleaner/badge/?version=latest
        :target: https://bib-cleaner.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://img.shields.io/badge/license-BSD-brightgreen.svg
        :target: https://img.shields.io/badge/license-BSD-brightgreen


Bib Cleaner removes unnecessary entries from your bib files. Documentation @ https://bib-cleaner.readthedocs.io.

Use case
--------

1. You have been writing a TeX document for a while, and adding citation entries to your ``.bib`` file. Suppose it is called ``master.bib`` and contains the following::

    % master.bib

    @article{citation1
    author = {Lastname1, Firstname1 and Lastname2, Firstname2},
    title = {{Title of Paper 1}},
    year = {2018}
    }
    @article{citation2
    author = {Lastname1, Firstname1 and Lastname2, Firstname2 and Lastname3, Firstname3},
    title = {{Title of Paper 2}},
    year = {2012}
    }
    @article{citation3
    author = {Lastname1, Firstname1 and Lastname2, Firstname2},
    title = {{Title of Paper 3}},
    year = {1953}
    }
    @article{citation4
    author = {Lastname1, Firstname1 and Lastname2, Firstname2},
    title = {{Title of Paper 4}},
    year = {1959}
    }

2. In the course of writing, some entries in your ``master.bib`` have become obsolete. You don't use them in your TeX document anymore, which looks like this::

    % contents.tex

    \documentclass{article}
    \begin{document}

    I wished them the so long \cite{citation1}
    and thanked them for all the fish \cite{citation3}.

    \end{document}


  Here ``citation2`` and ``citation4`` have become obsolete.

3. Of course, LaTeX compiles quite happily with these extra entries (``citation2`` and ``citation4``) and excludes them from the typeset bibliography... but you *know* they are there.
4. You take a step back, sip some coffee, go for a walk, all the while pondering "Man, I wish I could just `remove` those extra bib entries". You yearn for a world where all ``.bib`` files everywhere carry only what they have to, and no more.

I gotchu. Enter ``bib_cleaner``.


Quick install
--------------
This should work::

    $ pip install bib_cleaner

For detailed instructions, see :ref:`detailed_install`

Verify if it installed by typing the following in the command-line::

    $ bib_cleaner -h

You should see the help::

    usage: bib_cleaner [-h] [-t TEXFILES [TEXFILES ...]] [-o OUTPUTBIB] masterfile

    Produce a minimal bib file with only the entries found in your .tex file(s)

    positional arguments:
    masterfile            master bib file with used and unused citations (.bib)

    optional arguments:
    -h, --help            show this help message and exit
    -t TEXFILES [TEXFILES ...], --texfiles TEXFILES [TEXFILES ...]
                            content files to select entries from (.tex)
    -o OUTPUTBIB, --outputbib OUTPUTBIB
                            output file name with extension

How to use `bib_cleaner`
------------------------

After installation, navigate to your TeX directory try::

    $ bib_cleaner master.bib

Of course, replace ``master.bib`` with the name of your bib file with obsolete bib entries. ``bib_cleaner`` will

1. automatically detect all the TeX files (``.tex``) in that directory and use them to determine which bib entries are obsolete.

2. create ``new.bib`` which does not have the obsolete citations.

After you run ``bib_cleaner`` for the first time, you can

1. update your TeX files to use ``new.bib`` instead of ``master.bib``. Thereafter, any new citations added to your TeX files or addition/removal of entries from ``master.bib`` should be followed by a call to ``bib_cleaner``. Of course, you can add it to your LaTeX makefile should you have one.

2. marvel at how much smaller ``new.bib``. When the writing project is completed, run ``bib_cleaner`` again,once and for all and update your TeX files to use ``new.bib`` instead of ``master.bib``.

Specify TeX files
~~~~~~~~~~~~~~~~~

If you only want to keep the entries used in some TeX files, specify them with::

    $ bib_cleaner master.bib --texfiles chapter1.tex chapter2.tex

or::

    $ bib_cleaner master.bib -t chapter1.tex chapter2.tex

Specify output file name
~~~~~~~~~~~~~~~~~~~~~~~~

If you want to change the output bib file name from the default ``new.bib``, do::

    $ bib_cleaner master.bib -t chapter1.tex --outputbib chapter1.bib

or::

    $ bib_cleaner master.bib -t chapter1.tex -o chapter1.bib

TODO
----

* Remove typically unused lines from ``.bib`` files (like ``file = {...}`` or ``abstract = {...}``)
* Detect and remove bib entries with identical tags / raise conflict
* Add tests for the command-line interface

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
