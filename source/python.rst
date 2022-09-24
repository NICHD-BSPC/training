.. _python:

Python
======

.. seealso::

    See :ref:`choosing-r-python` if you're trying to decide whether to learn
    R or Python

Different people have different learning styles. Below are various
well-regarded resources for learning Python, but they take different
strategies. You'll be spending a lot of time with them, so it might be a good
idea to briefly look at them all first to see what would be a good fit for you.


Setting up
----------

Install Python using either `Anaconda
<https://www.anaconda.com/distribution/>`_ (if you want "the works", including
many of the libraries described below) or `Miniconda
<https://docs.conda.io/en/latest/miniconda.html>`_ (which is much more minimal;
you'll need to install things separately using ``conda install
<packagename>``).

You may have heard about Jupyter notebooks. While they have their place in data
science-type work, I do not think this is a good way to learn Python. `Here are
some reasons why
<https://docs.google.com/presentation/d/1n2RlMdmv1p25Xy5thJUhkKGvjtV-dkAIsUXP-AL4ffI/edit#slide=id.g362da58057_0_1>`_;
they boil down to needing to mentally keep track of what cells have been run
when to avoid strange and hard-to-track-down bugs.

At first, stay away from IDEs like PyCharm or Spyder. These remove you
too much from what is really happening and add an extra layer of complexity.
Once you have the basics down then by all means see what IDEs or notebook
solutions work best for you.

To start, you should start by using just a text editor and a terminal running
Python (or IPython, see the :ref:`ipython` section). My setup happens to be
running :ref:`vim` in one terminal next to another terminal open running
IPython.

Learning Python
---------------

When learning Python, it's very important to start with the basics. Sometimes
people will start learning Python because they're interested in data science,
and those sorts of tutorials jump right in to teaching `pandas
<https://pandas.pydata.org>`_. While pandas is amazing and it's important to be
fluent in pandas, learning pandas is not learning Python.

What do I mean by that?

It's possible to get most of the way through a pandas tutorial without ever
encountering a dictionary (a fundamental data structure that is used all over
Python code). While someone might be good at pandas specifically, they don't
learn the rest of Python. So they end up having big gaps in their knowledge.
Once they start hitting those gaps (like the first time they need to use
a dictionary), ideally they should go all the way back to learning the
fundamentals. But in practice, they want to solve the problem they're working
on in pandas and don't want to take the time to learn everything. As a result
they'll learn just enough of the basics to solve that one problem, and leave
the rest of the gaps in their knowledge until they hit the next one, when the
process repeats.

It's much better in the long run to learn the fundamentals. Then you will have
a shared vocabulary with everyone else -- including Stack Overflow commenters!
-- that will help you understand more complex topics as you progress.

- **If you like learning from first principles**, `The Official Python tutorial
  <https://docs.python.org/3/tutorial/>`_ is a complete tutorial. It's a bit
  dry though.

- **If you like jumping into the deep end and working out first principles on
  your own**, `Dive Into Python <https://diveintopython3.problemsolving.io/>`_
  is another good tutorial.

- `How to Think Like a Computer Scientist
  <http://openbookproject.net/thinkcs/python/english3e/>`_ takes a different
  approach and teaches principles by controlling graphics on the screen.
  A bonus is that you can run code directly in the browser. If you are a visual
  thinker or visual learner, give this one a shot.

- `Automate the Boring Stuff with Python <https://automatetheboringstuff.com>`_
  This book brings you through the basics of Python, and comes highly
  recommended by some BSPC post-bacs.

- `Learn Python the Hard Way <https://learnpythonthehardway.org/python3/>`_ is
  regarded highly but is $30.

- **If you plan to learn bash, Python, and R**, `A Primer for Computational
  Biology <https://open.oregonstate.education/computationalbiology/>`_ is
  a single resource that teaches all of these.

.. _ipython:

Use IPython
-----------

Python comes with an interpreter (what you enter when you type ``python``
at the command line). But that interpreter is limited in a lot of ways.

**As early as possible, start using IPython.** Its tab-completion, integrated
help, and debugging are amazing and will make your life so much easier. It also
makes working with matplotlib plots (and therefore seaborn and pandas plots)
much nicer, spawning the figures as a separate window and returning you to the
prompt. You can also directly interact with the Bash shell from inside IPython
(see `this page
<https://ipython.readthedocs.io/en/stable/interactive/python-ipython-diff.html>`_
for more).

Learn more about IPython in the `IPython tutorial
<https://ipython.readthedocs.io/en/stable/interactive/tutorial.html>`_.


Debugging in Python
-------------------
Something that is often skipped over in tutorials is the utility of interactive
debugging. In IPython, when you get an error you can call `%debug` from the
IPython command line and you are dropped into a live version of your code at
the exact point where the error was caused. You can then inspect the values of
various variables to troubleshoot what went wrong. This is much more powerful
than sprinkling ``print()`` statements throughout your code!

There is a good intro to the debugging workflow at `SciPy lecture notes:
debugging
<https://scipy-lectures.org/advanced/debugging/index.html#debugging-workflow>`_,
along with what to do when you can't use IPython.

Learning pandas
---------------

The ``pandas`` package is the standard for working with tables of data (like
from a spreadsheet).

.. note::

    It's important to learn Python (see above resources) before jumping in to
    pandas. Pandas is almost its own mini-language, so learning Pandas **does
    not** mean you're learning Python!

- `Visual intro to pandas
  <https://jalammar.github.io/gentle-visual-intro-to-data-analysis-python-pandas/>`_
  is very basic but visually helps you bridge the conceptual gap between Excel
  and pandas.

- The official `pandas tutorial list
  <https://pandas.pydata.org/pandas-docs/stable/getting_started/tutorials.html>`_
  has several options you can try to see what fits your learning style best.

-  `DataCamp Pandas <https://www.datacamp.com/community/tutorials/pandas-tutorial-dataframe-python>`_
   A bit more gradual introduction to Pandas

- If you've been using pandas already, `advanced pandas tricks
  <https://realpython.com/python-pandas-tricks/>`_ has some useful tricks.

After learning pandas, you should be able to do the following (in very rough
order of beginner to advanced):

- read csv or tsv or url into dataframe
- select rows and columns
- save to file
- discuss the difference between .loc and .iloc
- apply a function to a column
- create a DataFrame from lists or dictionaries
- find row with largest value in column
- chain pandas.DataFrame methods together to build a "pipeline"
- inspect for duplicates
- work with Excel files
- remove duplicates
- get rows where column value is one of a set
- discuss ways of handling missing data
- join dataframes together (aligning by index)
- group-by and summarize (e.g., find group means)

Visualization in Python
-----------------------

There are a lot of visualization options in Python. I think it's best to learn
matplotlib and then use seaborn, but this `dramatic comparison of Python
visualization libraries
<https://dsaber.com/2016/10/02/a-dramatic-tour-through-pythons-data-visualization-landscape-including-ggplot-and-altair/>`_
is entertaining and shows the different options.

After learning matplotlib and/or seaborn, you should be able to do the
following (in very rough order of beginner to advanced):

- plot line plots, scatter plots, histograms, bar plots, heatmaps
- change the axes labels and title
- save to file
- adjust x- and y-ticks and tick labels
- use different colors
- choose appropriate colormaps for heatmaps
- make subplots


Matplotlib
~~~~~~~~~~

Matplotlib is extremely powerful, as it gives you access to every aspect of
a plot. It is well worth the time to learn the basics of matplotlib, and then
move on to seaborn, which wraps matplotlib into easier-to-use functions and
classes.

- `matplotlib quick start
  <https://matplotlib.org/stable/tutorials/introductory/quick_start.html>`_
  is the best place to start if you're new to matplotlib.

- The `matplotlib tutorials page
  <https://matplotlib.org/tutorials/index.html>`_ has beginner, intermediate,
  and advanced tutorials.

- The `matplotlib gallery
  <https://matplotlib.org/stable/gallery/index.html>`_
  shows the kinds of things you can do with matplotlib.

Seaborn
~~~~~~~

The `seaborn tutorial page <https://seaborn.pydata.org/tutorial.html>`_ lays
out everything you need to know about seaborn.


Useful built-in Python modules
------------------------------

There are many built-in Python modules, here is a list of those that I keep
coming back to. There's no need to jump in and start learning these one-by-one.
But it is important to be aware of what's available. For example, it's useful
to know that if you are going to be building command-line tools, you should
look more into the ``argparse`` module.

The `Python Module of the Week (PyMOTW) <https://pymotw.com/3/>`_ is a great
resource for learning about these as well. Here I'm just listing the ones
I most commonly use:

- `argparse <https://docs.python.org/3/library/argparse.html>`_: build
  a command-line interface to your code, with auto-generated help.
- `collections <https://docs.python.org/3/library/collections.html>`_: has the
  very useful ``defaultdict``, ``Counter``, and ``OrderedDict`` classes
- `datetime <https://docs.python.org/3/library/datetime.html>`_: work with
  dates, times, and timedeltas
- `glob <https://docs.python.org/3/library/glob.html>`_: use wildcards when
  searching for files
- `itertools <https://docs.python.org/3/library/itertools.html>`_: fast,
  memory-efficient functions especially useful for working with very large
  datasets
- `json <https://docs.python.org/3/library/json.html>`_: read in JSON-formatted
  text
- `os <https://docs.python.org/3/library/os.html>`_: useful tools for
  interacting with the operating system (env vars, usernames, file permissions,
  etc)
- `pathlib <https://docs.python.org/3/library/pathlib.html>`_: manipulate
  filenames and directories (new in Python 3.4)
- `pprint <https://docs.python.org/3/library/pprint.html>`_: pretty-print.
  Useful for printing out big objects
- `re <https://docs.python.org/3/library/re.html>`_: regular expressions
- `shutil <https://docs.python.org/3/library/shutil.html>`_: shell-related
  utilities (copy/move files directories)
- `sqlite3 <https://docs.python.org/3/library/sqlite3.html>`_: create and
  interact with SQLite3 file-based databases
- `subprocess <https://docs.python.org/3/library/subprocess.html>`_: call out
  to the shell, for when you need to call other programs from within Python
- `sys <https://docs.python.org/3/library/sys.html>`_: various system-related
  functions. Often used for ``sys.argv`` which contains the arguments a Python
  script was called with
- `tempfile <https://docs.python.org/3/library/tempfile.html>`_: create and
  manipulate temporary files
- `textwrap <https://docs.python.org/3/library/textwrap.html>`_: nicely indent
  or dedent text, or line-wrap to a fixed line length
- `zipfile <https://docs.python.org/3/library/zipfile.html>`_: interact with
  zip files

Useful Python libraries
-----------------------

Below are some useful and commonly-used Python libraries to give you a flavor
of what else is possible with Python. Like the modules above, this section is
more for being aware of what's out there, and you can look for more details on
particular ones that seem like they would be helpful for your work.

- `argh <https://pythonhosted.org/argh/>`_ is great for building more complext command-line tools
- `biopython <https://biopython.org/>`_ is the way to parse FASTA, FASTQ, and
  do various sequence manipulation (for other file formats like SAM/BAM or
  GTF/BED/VCF, see below)
- `cyvcf2 <https://github.com/brentp/cyvcf2>`_ for working with VCF files
- `flask <https://flask.palletsprojects.com/en/1.1.x/>`_ is a website development framework
- `matplotlib <https://matplotlib.org/>`_, for plotting
- `numpy <https://numpy.org/>`_ is actually the basis for matplotlib, scipy, and pandas, but is useful on its own
- pandas for tabular data manipulation
- `pybedtools <https://daler.github.io/pybedtools/>`_ wraps and greatly extends
  bedtools for manipulating BED/VCF/GTF/GFF/BAM/SAM files. Written and maintained by BSPC!
- `pysam <https://pysam.readthedocs.io/en/latest/api.html>`_ for working with
  BAM/SAM files. Also VCF.
- `requests <https://requests.readthedocs.io/en/master/>`_ for working with
  anything from the internet (downloading pages etc)
- `scikit-learn <https://scikit-learn.org/stable/>`_ for machine learning
- `scipy <https://www.scipy.org/>`_ general scientific computing (e.g., signal processing, stats, linear algebra)
- `seaborn <https://seaborn.pydata.org/>`_ wraps and extends matplotlib for plotting
- `sphinx <https://www.sphinx-doc.org/en/master/>`_ for documentation. This very site is built using Sphinx!
- `trackhub <https://daler.github.io/trackhub/index.html>`_ for building UCSC
  track hubs. Written and maintained by BSPC!
- `yaml <https://pyyaml.org/>`_ for working with YAML config files

Other links
-----------

The following links are related to Python but don't necessarily fit into the
above categories.


- `A Visual Intro to NumPy <https://jalammar.github.io/visual-numpy/>`_ is
  useful if you're just starting to learn NumPy

- `The SciPy Lectures <https://www.scipy-lectures.org/>`_
  First chapter of Scientific Python lectures includes NumPy, matplotlib, and
  scipy basics. Subsequent chapters get fairly advanced.

- `“I don’t like Jupyter Notebooks”
  <https://docs.google.com/presentation/d/1n2RlMdmv1p25Xy5thJUhkKGvjtV-dkAIsUXP-AL4ffI/mobilepresent?slide=id.g362da58057_0_639>`_
  Some good arguments on why Jupyter Notebooks are not a good idea,
  especially for beginners trying to learn Python. I think that
  notebooks have their place as a final product for showing how to
  reproduce an analysis, but agree that they shouldn’t be the first
  tool to reach for.

- `Practical business python <https://pbpython.com/>`_ has lots of useful posts
  on intermediate topics

Python skills
-------------

Some people have asked about what skills they would be expected to have when
learning Python. That's a very difficult question, as it depends on exactly
what you're using Python for.

Below, I've attempted to categorize various parts of base Python into different
levels. This is by no means exhaustive, and the items and organization likely
reflect the biases of my own path when learning and using Python. And by no
means do you have to learn everything here! You can do a lot of really
interesting things just with the "level 1" skills.

Note that many of the more advanced topics will not be found in the tutorials
linked above, so you'll need to find your own resources for learning them, or
get in touch ryan.dale@nih.gov if you would like some pointers.

There are lots of commonly-used Python modules (see sections above), each of
which have their own lists of skills. This section is just about base Python.

Level 1
~~~~~~~

- creating lists, dicts, tuples
- difference between list and tuple
- methods of string
- methods of list
- methods of dict
- importing
- functions
- for loops
- while loops
- using IPython
- `run` in IPython
- while loops
- open a file
- write to a file

Level 2
~~~~~~~

- debugging in IPython (with pdb)
- list comprehensions
- dict comprehensions
- sets
- discuss dictionary order
- `4 < 3 and 5 > 4` is False, why?
- manually parse a file line-by-line
- difference between ``*args`` and ``**kwargs`` in a function definition
- common standard modules (os, sys, argparse, pathlib, glob)
- f-strings
- docstrings

Level 3
~~~~~~~
- dealing with unicode
- building a command-line interface with ``argparse``
- object-oriented design
- string formatting mini-language
- discuss when you would use ``*args`` and ``**kwargs`` in a function definition
- write a generator function
- discuss when you would use a generator function
- making a class an iterator
- "dunder" methods
- why ``import *`` is not a great idea (discussion of namespaces)
- Zen of Python
- lambda expressions
- pep8
- using decorators
- raising errors
- catching errors
- using `if __name__ == "__main__"`
- understanding what `if __name__ == "__main__"` means
- organizing code into modules
- what those __pycache__ directories are
- doctests
- using a context manager


Level 4
~~~~~~~
- shallow vs deep copy
- function annotations
- type hints
- writing decorators
- writing a package
- unit tests
- writing a context manager and discussing why it's useful
- create and use sqlite3 databases

Level 5
~~~~~~~
- cython extensions
- asyncio
- multiprocessing
