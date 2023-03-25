.. _choosing-r-python:

Choosing R or Python
====================

R and Python are both commonly-used languages in statistics, data science,
visualization, and bioinformatics. Once you learn one, you will be able to pick
up the other one relatively quickly.

However, learning programming languages is much like learning human languages:
it takes time and practice. So you'll probably want to focus on just one to
start to avoid confusion.

But which one to choose? This question is the topic of many a `flame war
<https://en.wikipedia.org/wiki/Flaming_(Internet)>`_ on programming websites,
and you should do your own research into which one to choose. In BSPC, we use
both R and Python extensively, so here are some opinions on how they are
different and why you might want to choose one or the other depending on your
training goals, career goals, and expectations.


Choose the language used in your environment
--------------------------------------------
If your lab focuses more on Python or R, then you should learn that first.
You'll have more local resources and will be able to be more immediately
productive by learning the language used by your peers. And if your lab uses
Matlab, by all means learn Matlab first!

  If a language is already used in your lab, start with that one.


Python is a general programming language, R is a statistical programming package
--------------------------------------------------------------------------------

R is primarily for data analysis, visualization, and statistical programming.
Python is used for those as well, and in addition it is a general-purpose language.
Python is installed by default on Mac and Linux and used for various systems
programming tasks. You can build a website from scratch with Python (R does have
the wonderful Shiny package for building interactive websites, but such sites
these are constrained to a certain kind of website).

The biggest differentiator is that Python is used in many
other domains, while R tends to be focused more on biology, statistics, and
visualization. Many tools provide a Python API. With Python you can control 3D
animation in `Blender <https://blender.org>`_, operate on `Dropbox
<https://www.dropbox.com/developers/documentation/python>`_ files
interact with `GitHub <https://github.com/PyGithub/PyGithub>`_, `control
a Raspberry Pi camera
<https://projects.raspberrypi.org/en/projects/getting-started-with-picamera>`_,
`write and compose music <https://wiki.python.org/moin/PythonInMusic>`_,
`create games <https://www.pygame.org/docs/>`_, `create web apps
<https://flask.palletsprojects.com/>`_, and much more.

The statistical methods available in R are unparalleled. Python does have some
statistics, for example in the `statsmodels <https://www.statsmodels.org/stable/index.html>`_
and `scipy.stats
<https://docs.scipy.org/doc/scipy/tutorial/stats.html>`_ packages,
but these are just playing catch-up to R.

For things like differential expression in bulk RNA-seq that use sophisticated
statistical methods, the major packages for this (DESeq2, edgeR) are written in
R.

  If you are interested in general programming -- not just bioinformatics and statistics -- choose Python for its flexibility.

  If you will be using sophisticated statistics, choose R.


Visualization is good in both
-----------------------------

In R, there's pretty much just one plotting package in town: `ggplot2
<https://ggplot2.tidyverse.org/>`_. ggplot2 is a fantastic plotting library for
R. It is sort of its own mini-language though, so it takes some time to get used
to it, but that time is well worth it.

Python has excellent plotting libraries as well: `plotnine
<https://plotnine.readthedocs.io/en/stable/>`_ is inspired by ggplot2, though
`seaborn <https://seaborn.pydata.org/>`_ tends to be a more canonical Python
package. Both use the powerful `matplotlib <https://matplotlib.org/>`_ package.
There's also `bokeh <https://docs.bokeh.org/en/latest/index.html>`_ and
`holoviews <http://holoviews.org/>`_ which are geared more towards interactive
web visualization.

`plotly <https://plot.ly/graphing-libraries/>`_ has libraries for both R and
Python.

The only differentiator I see between R and Python is for custom graphics. If
you need to make non-standard figures of some kind, it tends to be easier to do
that in matplotlib which gives cleaner access to the individual components of
a plot (down to modifying each individual shape or line, if you need it).

  Visualization is good in both Python and R, and so does not help in choosing.

Manipulating data from TSV/CSV/Excel is good in both
----------------------------------------------------

R has the `tidyverse <https://www.tidyverse.org/>`_, a set of packages designed
for data science-type work that all work together (and have their own
idiosyncratic way of doing things). In particular, the `dplyr
<https://dplyr.tidyverse.org/>`_ package makes it easy to interact with tables
of data.

Python has `pandas <https://pandas.pydata.org/>`_ for interacting with tables of
data.

The authors of dplyr and pandas have collaborated on the `feather
<https://github.com/wesm/feather>`_) format, which allows for
cross-communication between R and Python.

  Data manipulation is good in both Python and R, and so does not help in choosing.

Bioconductor is only for R
--------------------------

One major reason for choosing R is the fanstastic `Bioconductor
<https://bioconductor.org/>`_ repository. This is a huge collection of
high-quality bioinformatics-related packages for R. There's nothing in Python
that comes close.

  If you are planning to rely heavily on Bioconductor packages, you should choose R.


Snakemake is a superset of Python
---------------------------------

`snakemake <https://snakemake.readthedocs.io>`_ is a workflow management system
that helps tie together complex analyses. Snakemake is a superset of Python, so
all valid Python is also valid Snakemake. Knowing Python is therefore important
for writing Snakefiles.

  If you plan to use Snakemake heavily, choose Python


Still can't choose?
-------------------

`Another Book On Data Science <https://www.anotherbookondatascience.com/>`_
teaches them both side-by-side, and `this page of comparisons
<https://gist.github.com/conormm/fd8b1980c28dd21cfaf6975c86c74d07>`_ attempts
to show operations in dplyr and pandas side-by-side.
