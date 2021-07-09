==========
Koala HTML
==========

Package containing simple tools for html page generation.


Installation
------------

Release version

.. code-block:: console

   $ pip install koala_html


From source

.. code-block:: console

   $ pip install .

Usage
-----

If you have set of png files :code:`file1.png, file2.png,..`, you can put them all in a single HTML page (default :code:`index.html` by running

.. code-block:: console

   $ koala_table -1 *png

If you want to put them in separate columns, then use

.. code-block:: console

   $ koala_table -1 *column1*png -2 *column2*png

For a full list of options, see

.. code-block:: console

   $ koala_table --help

Creating a new release
----------------------

.. code-block:: console

   $ git tag koala-html-vX.Y.Z
   $ twine upload dist/koala_html-X.Y.Z.tar.gz

