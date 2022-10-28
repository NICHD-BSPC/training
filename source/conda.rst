.. _conda:

Conda
=====

Conda helps install and manage software packages in a separate environment that
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
`bioconda docs <https://bioconda.github.io/>`_:

.. code-block:: bash

   conda config --add channels defaults
   conda config --add channels bioconda
   conda config --add channels conda-forge
   conda config --set channel_priority strict

**Optional:** Much of the bioinformatics community is moving to `mamba
<https://mamba.readthedocs.io/en/latest/index.html>`_, which is a faster
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

.. warning::

    If you have a new Mac that uses the M1 chip, **this is not yet supported by
    Bioconda**. All packages need to be re-built for ARM64 architecture, which
    is a rather large task. There are plans to do this but the packages are not
    available yet.


What is an environment?
-----------------------
The purpose of conda is to create environments. We create environments and then
*activate* them to use them.

What is an environment?

Briefly: an environment is a directory containing executables and supporting
files for those executables, and environment activated when its directory of
executables is been prepended to the ``$PATH``.

What does that mean?

First, let's understand the ``$PATH`` variable. For example, if you're on a Mac
or Linux machine, you have access to the command ``ls`` that lists the contents
of directories. ``ls`` is an executable program. When you type ``ls`` on the
command line, the command line interpreter needs to figure out what you mean.
It will look through its list of possible locations to try and find an
executable called ``ls``. The first one it finds, it runs.

How does it know where to look?

By convention, the shell uses the ``$PATH`` variable. This is a variable that,
again by convention, is separated by colon (``:``) characters. Here is
a typical ``PATH`` from a fresh Linux machine, which we can see by running ``echo
$PATH``::

    /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

So with this ``PATH``, typing ``ls`` (and then Enter) means that the shell will
first look in ``/usr/local/sbin`` for the executable program ``ls``. If the file
``/usr/local/sbin/ls`` does not exist, then it will next check for
``/usr/local/bin/ls``. If that doesn't work, it keeps going. On this machine,
eventually ``/bin/ls`` is found (it happens to be the last place it looked) and
it is **that** ``ls`` that runs.

If ``ls`` can't be found at any of those locations, we'll get a ``ls: command
not found`` error.

We can edit your ``PATH`` variable to add new locations. This is how we
"install" programs on Linux. For example, imagine we made a new amazing version
of ``ls`` that we wanted to be called any time we typed ``ls`` on the command
line. We don't have root access to this machine, so we can't put my new ``ls`` in
any of the paths in our ``PATH`` variable (they are all system-wide and owned by
root). Instead, we modify the ``PATH`` variable. Say we were keeping the new ``ls``
in our home directory, ``~/tools/ls``. Then we would modify ``PATH`` like
this::

    export PATH="~/tools:$PATH"

Here is an annotated version of that:

.. code-block:: text

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

After running that command, we check the new value of ``$PATH``:

.. code-block:: bash

    echo $PATH
    ~/tools:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
    # ^^^^^
    # the directory has been prepended

If we wanted that to be permanent so we had that every time we started a new shell,
then we would put that ``export`` line in the ``~/.bashrc`` file, which is executed
every time bash starts up.

So now hopefully the following statment makes more sense: "an activated
environment is a directory containing executables that has been prepended to the
``$PATH``.

Activating and deactivating environments
----------------------------------------

**Activating an environment** with ``conda activate`` will add the
environment's directory containing executables to the ``$PATH``. This is the
``bin`` directory of the evironment. For example, if we create a simple
environment with just Python:


.. code-block:: bash

    mamba create -p ./env python

and look inside it with ``ls env/``, we see this:

.. code-block:: text


    ├── bin
    ├── conda-meta
    ├── include
    ├── lib
    ├── man
    ├── share
    └── ssl

If we look inside the ``bin`` directory, we'll see lots of files. One of them
is ``python``. If we activate the environment with ``conda activate ./env``,
and check the path, **the bin directory of the environment has been prepended
to the path**. So if we use ``which python``, it should point to the Python
installation in that directory because the shell found ``python`` at the first
place it looked: the ``bin`` directory of the environment. As long as this
environment is activated, any time we call ``python`` it will use *that*
Python.

If we wanted to, we could avoid using ``conda activate`` and just manually add
things to the path. Or we could explicitly call that Python with
``./env/bin/python``. But ``conda activate`` ends up being more convenient.

**Deactivating an environment** with ``conda deactivate`` removes the path from
the ``$PATH``. So in this case, after deactivating the environment, calling
``python`` will find a different installation of Python. Typically it will find
the Python in the base environment, or, after running ``conda deactivate``
again to deactivate the base environment, a location like ``/usr/bin/python``
(in the case of MacOS).

Difference between named environment and a path environment
-----------------------------------------------------------

If we create a new environment like this::

    conda create -n proj python

then it will create the environment directory wherever we have installed my
version of conda. Others might not have access to that directory. We need to
remember the name of the environment, or otherwise run ``conda env list`` and
study the list to remember which one we should use. We would activate it like
this::

    conda activate proj

If we instead create a new environment like this, say, after changing to our
project directory::

    conda create -p ./env python

then it will create the environment in a directory called ``env`` in the current
directory, and we would instead activate it like this::

    conda activate ./env

The ``./`` is important. We can alternatively use ``env/``. The point is that
conda needs to see that ``/`` indicating that it's a *directory* not an
*environment name* that should be activated. If we used ``conda
activate env`` then it would look for an environment named ``env`` which we might
not have created.

A path environment is very helpful when working in a shared directory. Anyone
with access to the directory can activate the environment and be using the exact
same set of packages as anyone else. This makes it easier for
someone else to jump in and help troubleshoot immediately rather than have to
worry about matching dependencies and do lots of installation work before they
can even start to reproduce the thing they're trying to troubleshoot. If we
maintain a consistent naming convention, then it's very clear which environment
should be used for the project.


Conventions for project-specific environments
---------------------------------------------
In BSPC, we have the convention that each project directory should have at least
an ``env`` directory, at the top level of the project, containing the conda
environment to be used by that project.

Some projects may have a separate ``env-r`` directory, or may have multiple
environments either for historical reasons (like keeping a copy of an env from
a previous version of the analysis) or for logistical reasons (like splitting
R and non-R packages into separate envs to save time). But in general, having
an obvious environment directory name
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
    ^^^^ ^^^^^^ ^^^^^^^^^^
    |       |       |
    |       |       | build string
    |       |
    |       | package version 
    |
    | package name


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

Excluding build numbers is useful because it allows packages to "float" to the
most recent available build, while still keeping the package version the same.
There are cases where the channel (like conda-forge or bioconda) removes
a particular build because it is known to be broken. If an environment yaml
happened to contain that broken build, recreating that environment would fail
because it wouldn't be found.


Completely remove defaults channels
-----------------------------------
If you get an error like this::

    RuntimeError: Multi-download failed. Reason: Transfer finalized, status: 403 [https://repo.anaconda.com/pkgs/r/noarch/repodata.json] 4020 bytes

then you can fix it by completely removing the default channels from conda by
adding this to your ``~/.condarc``::

    default_channels: []

Then run::

    conda config --remove channels defaults

While you're at it, you may want to set strict channel priorities, as
recommended by the `bioconda docs <https://bioconda.github.io>`_.

So a working ``.condarc`` looks like the following::

    channels:
      - conda-forge
      - bioconda
    channel_priority: strict
    default_channels: []


Installation on Helix/Biowulf
-----------------------------

On NIH's Helix/Biowulf cluster, trying to install miniconda can result in the
installation directory having only a ``conda.exe`` file in it, and you also get
warnings about libraries. This appears to be an issue with how temp files are
handled on the system.

In general, the latest info is on `Biowulf docs on conda
<https://hpc.nih.gov/apps/python.html#envs>`_. Here is a summary of that
section showing how to use a new temp directory:

.. code-block:: bash

    wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
    TMPDIR=/scratch/$USER/temp bash \
      Miniconda3-latest-Linux-x86_64.sh \
      -p /data/$USER/miniconda3 \
      -b


Biowulf staff also recommend NOT activating your base environment by default. Why?

- activating an environment runs conda, which runs Python
- Python touches a lot of files when starting up
- If you run thousands of jobs on the cluster, session each job will activate
  the base environment (and therefore using Python), which will possibly touch
  hundreds of thousands of files before any computational work is done,
  potentially causing I/O lag on the cluster.

There are a few ways around this. The one I have found most convenient is to
first run ``conda init bash``, which adds lines to your ``~/.bashrc`` file that
look like this:

.. code-block:: bash

    # >>> conda initialize >>>
    # !! Contents within this block are managed by 'conda init' !!
    __conda_setup="$('/data/$USER/miniconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
    if [ $? -eq 0 ]; then
        eval "$__conda_setup"
    else
        if [ -f "/data/$USER/miniconda3/etc/profile.d/conda.sh" ]; then
            . "/data/$USER/miniconda3/etc/profile.d/conda.sh"
        else
            export PATH="/data/$USER/miniconda3/bin:$PATH"
        fi
    fi
    unset __conda_setup
    # <<< conda initialize <<<

Edit your ``.bashrc``, and wrap that newly-added-by-conda-init code in
a function. Here, the function is called ``c`` just because it's easy to type
but it can be whatever you want. Here, I also added ``conda activate $1`` to
the end of it. So I converted those lines to something that looks like this in
my ``.bashrc`` (added lines emphasized):

.. code-block:: bash
    :emphasize-lines: 1,17,18

    function c() {
        # >>> conda initialize >>>
        # !! Contents within this block are managed by 'conda init' !!
        __conda_setup="$('/data/$USER/miniconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
        if [ $? -eq 0 ]; then
            eval "$__conda_setup"
        else
            if [ -f "/data/$USER/miniconda3/etc/profile.d/conda.sh" ]; then
                . "/data/$USER/miniconda3/etc/profile.d/conda.sh"
            else
                export PATH="/data/$USER/miniconda3/bin:$PATH"
            fi
        fi
        unset __conda_setup
        # <<< conda initialize <<<

        conda activate $1
    }

Now, I can either activate my base environment with ``c``, or activate an
environment with ``c ./env``...but my base environment is not activated at the
start of every session, thus reducing the I/O burden on the cluster.

source activate vs conda activate
---------------------------------

The "old" way of activating an environment was ``source activate env``.
This should still work.

The "new" way of activating an environment is ``conda activate env``.

The new way requires to do a one-time setup, ``conda init bash``, which adds
a bunch of stuff into your ``.bashrc``.

However if you try ``conda activate`` within a script, you'll get an error
because the script does not source ``.bashrc``. The solution is to change

.. code-block:: bash

    conda activate ./env

to

.. code-block:: bash

    eval "$(conda shell.bash hook)"
    conda activate ./env

Note that if you inspect what ``conda init bash`` adds to your ``.bashrc``,
it's basically doing the same thing.


Detailed troubleshooting example
--------------------------------
Here are some notes on a recent conda troubleshooting session that may provide
some useful tools for future cases.

This issue started when cutadapt in the original env was giving CRC errors
apparently because it thought the gzipped fasta files were corrupt. I verified
the files themselves in various ways, it didn't look to be the input files that
caused the problem. So I started to suspect the tool.

I created a quick script that would perform the test to isolate the issue and
so that I would have a quick way of seeing if a possible fix worked or not, to
minimize downtime between tests.

OK, first thing to check:  maybe it's something with the env. Tried ``module
load cutadapt`` on Biowulf, to use the version installed by Biowulf staff. Ran
the test script, and it worked.

OK, maybe it's version thing? The biowulf module was using cutadapt 3.0, and
the original env was using cutadapt 3.3. So I made a new env with cutadapt 3.0
(``mamba create -p ./env-cutadapt3.0 cutadapt=3.0``). It worked. Also verified
running cutadapt 3.4 worked in another environment created similarly. So using
3.0 or 3.4 worked, that's good.

To verify that it's in fact a version thing, I created a fresh env with just
cutadapt 3.3, expecting it to fail. But it worked! Oh no. Is this some sort of
strange filesystem thing that is now magically resolved? I went back to the
original env that had 3.3, and verified that yes, it's still failing. So there
must be something in particular about that original env.

To test that idea, I created a new version of the original environment but with
cutadapt 3.4 to see what other packages are brought in. I probably should have
done this with cutadapt 3.3; this was not a properly controlled experiment!
Anyway, this new environment did work.

So the signs were pointing to the fact that something *else*, brought in as
a dependency of cutadapt in that original envirnoment, was the cause. So
I needed to figure out what was different between the original env and the new
one with cutadapt 3.4 (besides cutadapt itself of course).

To do this, I used ``conda env export`` on the original and newly-created envs,
and then studied the diff between the two files. After chasing a couple of
false leads, I eventually saw that ``python-isal`` was at version 0.8.0 in the
original environment...but 0.9.0 in the newly working one. I looked up what
``python-isal`` was, and it's a compression library. The original problem I was
trying to solve was that error with gzip, so this was a promising reasonable
lead. After checking the github page, I did find a closed issue,
https://github.com/pycompression/python-isal/issues/60, that described the
problem and showed that the problem was fixed in 0.8.1. Note that this github
issue did not come up when I was searching for the original error!

So the solution was to pin ``python-isal>0.8.0`` in the requreiments.txt in the
original environment...and that worked!
