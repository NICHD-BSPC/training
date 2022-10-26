.. _conda:

Conda
=====

Conda is a means of installing software packages in a separate environment that
is isolated from the rest of the system. You install conda once, and from there
you use use conda to install lots of other software, without needing root
access. Typically, you will be creating an environment for each project. That
environment has everything in it that you need for that project (for example,
maybe Python and R and various packages for those languages). Importantly, that
version of R and that version of Python are *completely independent* of any
other environments you might have.

Another major advantage is that you can generate a list of packages and send
that list to someone else, allowing them to install the same exact packages on
their machine. Since different versions of tools often give different results,
this aspect is very important for reproducibility.

.. note::

    For NIH users, see the NIH HPC `Python documentation
    <https://hpc.nih.gov/apps/python.html>`_ for specific points about
    installing and using conda on Biowulf. One of the main points is that on
    Biowulf, each person should have their own miniconda installation in their
    ``/data/$USER`` directory. Don't use your home directory because the quota
    of 16 GB can actually be too small after installing a lot of packages.

First, `install conda
<https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html>`_.
See the note above if you are working on NIH's Biowulf cluster.

Then set up the channels like this, which follows the
`bioconda docs <https://bioconda.github.io/user/install.html>`_:

.. code-block:: bash

   conda config --add channels defaults
   conda config --add channels bioconda
   conda config --add channels conda-forge
   conda config --set channel_priority strict

Much of the bioinformatics community is moving to ``mamba``, which is a faster
drop-in replacement for ``conda`` which is `quite a bit faster
<https://pythonspeed.com/articles/faster-conda-install/>`_. So typically the
next step is to install ``mamba`` into your base environment. You only have to
do this once:

.. code-block:: bash

    conda install -n base mamba

From now on, instead of ``conda install`` you can use ``mamba install`` to make
it go faster. Instead of ``conda create`` use ``mamba create``. And so on. There
are also some nice troubleshooting tools that come with ``mamba`` that can come
in handy.

What is an environment?
-----------------------

Briefly: an activated environment is a directory containing executables that has
been prepended to the ``$PATH``.

What does that mean?

If you're on a Mac or Linux machine, you have access to the command ``ls`` that
lists the contents of directories. ``ls`` is an executable program. When you
type ``ls`` on the command line, the command line interpreter needs to figure
out what you mean. It will look through its list of possible locations to try
and find an executable called ``ls``. The first one it finds, it runs.

How does it know where to look?

By convention, the shell uses the ``$PATH`` variable. This is a variable that,
again by convention, is separated by colon (``:``) characters. Here is
a typical ``PATH`` from a fresh Linux machine, which I can see by running ``echo
$PATH``::

    /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

So with this ``PATH``, typing ``ls`` (and then Enter) means that the shell will
first look in ``/usr/local/sbin`` for the executable program ``ls``. If the file
``/usr/local/sbin/ls`` does not exist, then it will next check for
``/usr/local/bin/ls``. If that doesn't work, it keeps going. On this machine,
eventually ``/bin/ls`` is found (it happens to be the last place it looked) and
it is **that** ``ls`` that runs.

If ``ls`` can't be found at any of those locations, you'll get a ``ls: command
not found`` error.

You can edit your ``PATH`` variable to add new locations. This is how you
"install" programs on Linux. For example, imagine I made a new amazing version
of ``ls`` that I wanted to be called any time I typed ``ls`` on the command
line. I don't have root access to this machine, so I can't put my new ``ls`` in
any of the paths in my ``PATH`` variable (they are all system-wide and owned by
root). Instead, I modify the ``PATH`` variable. Say I was keeping my new ``ls``
in my home directory, ``~/tools/ls``. Then I would modify my ``PATH`` like
this::

    export PATH="~/tools:$PATH"

Here is an annotated version of that::

    export PATH="~/tools:$PATH"
    ^      ^     ^       ^
    |      |     |       |
    |      |     |       |__ expand out the existing contents of PATH
    |      |     |           and insert the results here
    |      |     |
    |      |     |__ Add the directory with the program I made 
    |      |     |   to the beginning of the new PATH
    |      |
    |      |__ Overwrite the existing PATH
    |
    |__ Make the new PATH available to child processes,
        not just this one

After running this:

.. code-block:: bash

    echo $PATH

    ~/tools:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

If I wanted that to be permanent so I had that every time I started a new shell,
then I would put that ``export`` line in my ``.bashrc`` file, which is executed
every time bash starts up.

So now hopefully the following statment makes more sense: "an activated
environment is a directory containing executables that has been prepended to the
``$PATH``.


Difference between named environment and a path environment
-----------------------------------------------------------

If I create a new environment like this::

    conda create -n proj python

then it will create the environment directory wherever I have installed my
version of conda. Others might not have access to that directory. I need to
remember the name of the environment, or otherwise run ``conda env list`` and
study the list to remember which one I should use. I would activate it like
this::

    conda activate proj

If I instead create a new environment like this, say, after changing to my
project directory::

    conda create -p ./env python

then it will create the environment in a directory called ``env`` in the current
directory, and I would instead activate it like this::

    conda activate ./env

The ``./`` is important. You can alternatively use ``env/``. The point is that
conda needs to see that ``/`` indicating that it's a *directory* not an
*environment name* that should be activated. If I used ``conda
activate env`` then it would look for an environment named ``env`` which I might
not have created.

A path environment is very helpful when working in a shared directory. Anyone
with access to the directory can activate the environment and be using the exact
same set of packages as anyone else. This makes it easier, for example, for
someone else to jump in and help troubleshoot immediately rather than have to
worry about matching dependencies and do lots of installation work before they
can even start to reproduce the thing they're trying to troubleshoot. If you
maintain a consistent naming convention, then it's very clear which environment
should be used for the project.

Conventions for project-specific environments
---------------------------------------------
In BSPC, we have the convention that each project directory should have at least
an ``env`` directory, at the top level of the project, containing the conda
environment to be used by that project. Some projects may have a separate
``env-r`` directory, or may have multiple environments either for historical
reasons (like keeping a copy of an env from a previous version of the analysis)
or for logistical reasons (like splitting R and non-R packages into separate
envs to save time). But in general, having an obvious environment directory name
makes it easy for others to find.

Creating an environment
-----------------------

There are three ways to specify what should go into an environment:

1. Directly on the command line. Not advisable because it's harder to track
   what's in there.
2. Plain text file, one package per line (by convention called
   ``requirements.txt``)
3. An environment file in YAML format (by convention called ``env.yml``)

Directly on the command line::

    mamba create ./env python

Using a plain text file called ``requirements.txt`` with the following contents
(one line per requirement)::

    python

would be::

    mamba create -p ./env --file requirements.txt


Using an environment file in YAML format called ``env.yml`` with the following
contents:

.. code-block:: yaml

    channels:
      - conda-forge
      - bioconda
    dependencies:
      - python

would be::

    mamba env create -p ./env --file env.yml

That is, use ``create`` for a text file, and ``env create`` for a YAML file.

Updating and managing environments
----------------------------------
In BSPC, we have the policy that *anything added to the environment should be
recorded in a file* which is then used to update the environment. That way, the
environment file is the authoritative source of what was put into the
environment.

If you need to add something to the environment, **add it to the requirements
first** (either requirements.txt or env.yaml) and then with the environment
activated, install the entire requirements file. For example:

.. code-block:: bash

    conda activate ./env
    mamba install --file requirements.txt

This will only install packages (and dependencies) that have not already been
installed, and in this case ``requirements.txt`` contains the packages that were
installed.

Conda envs cannot be moved
--------------------------
Due to the way that libraries (typically C and C++) are handled in conda, the
absolute path to an environment is written into many of the executable files at
install time. This means that if the environment is moved to another location,
those absolute paths will no longer be pointing to the paths where the libraries
are, which breaks the environment.



Recording installed packages
----------------------------

If you have been rigorous about maintaining the contents of the requirements,
that should be sufficient for someone else to build the new environment.
Otherwise, or if you want to be sure, you can *export* the environment.

.. code-block:: bash

    conda env export --no-builds > env_export.yaml

This will include all dependencies in a YAML format file ready to be used by
``conda env create --file``. This will also included depencencies that you
didn't explicitly install. For example, building an evironment with just Python
in it will also install lots of other things that Python needs (like pip,
setuptools, sqlite, tk, wheel, ca-certificates, and more). These will also be
included in the export.

The ``--no-builds`` part is helpful for maintaining the reproducibility -- see
below for more on this.

Least reproducible (but may still be perfectly fine!)::

    python
    pandas

Or, assuming you know that you need features from pandas that
were added in version 1.5.1::

    python
    pandas>=1.5.1

Those files must be hand-written based on what you know your codebase requires.

Using ``conda env export`` allows you to report *everything* that got installed
(dependencies of dependencies of depencencies of....) in the environment.


Installing a previously-exported env.yaml and dealing with version conflicts
----------------------------------------------------------------------------

If you re-create an environment from an env.yaml within a short amount of time
(say a few months) then it is likely that it will work with no problems.
However, over time, packages may get fixed which could cause issues.

This primarily happens when there are *build numbers* included in the env.yml.
To understand this, first take a look at a typical conda package name::

    zlib-1.2.12-h5eee18b_3

Here, ``zlib`` is the package name (it's used by MANY other packages to handle
file compression, so there's a good chance it's in your environments). The
``1.1.12`` is the version of zlib. The ``h5eee18b_3`` is called the *build
number* or sometimes the *build string*. Technically, that ``h5eee18b`` part is
the hash of all of the pinned packages and versions used by this package that
are also pinned to a specific version by the build infrastructure (that is,
conda-forge or bioconda). In other words, it's a string that will change if
a version changes in *any* of the packages it depends on. The ``_3`` part means
that this is the fourth time (the number is zero-indexed) that zlib version
1.1.12 has been rebuilt using this same collection of underlying packages.

**Do not expect build numbers to be stable over time.** For example, a packager
might realize that they forgot to copy over a file, and this issue wasn't caught
until later. Or a packager included large amounts of supplementary data into
a package and was asked to remove it to avoid very long download times. In both
cases, the package version doesn't change -- it's just other parts around it
that change. This is reflected in changes to the build number. 

