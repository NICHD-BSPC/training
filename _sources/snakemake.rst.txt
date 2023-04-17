.. _snakemake:

Snakemake
=========

A workflow manager like Snakemake is the next step after simple bash scripts
towards fully scalable and reproducible analyses. Another popular workflow
manager for genomics is `Nextflow <https://www.nextflow.io/>`_ and `Wratten et
al 2021 <https://www.nature.com/articles/s41592-021-01254-9>`_ is a review of
the current state. You can see how many workflow managers in general are
out there with `this list
<https://github.com/common-workflow-language/common-workflow-language/wiki/Existing-Workflow-systems>`_
(over 300 at the time of this writing).

In BSPC, we prefer Snakemake over other workflow managers because:

- Its simple combination of bash and Python make it straightforward to convert
  individual tools' command-line calls into working Snakemake code
- Any valid Python is valid Snakemake, and we write a lot of Python so we can
  leverage that knowledge in our Snakemake files
- It affords the most flexibility and customization out of all the workflows
  we've tried. This is important to us as a bioinformatics core working on
  a wide variety of projects that often need customization
- Snakemake integrates very well with conda and high-performance compute
  clusters, which we also use a lot

Snakemake is a superset of Python that allows for workflow management using
"rules" that dictate input/output files for each rule, the commands to convert
inputs to outputs, and the dependencies between rules. It can be run locally or
on a cluster with no code changes. In the context of genomics workflows, if
a new sample is added Snakemake will figure out just the rules that need to be
run on that single sample, leaving everything else untouched. It also trivially
parallelizes tasks that are run, dramatically speeding up workflow runs.

Learning Snakemake
------------------

The following resources are ordered from most basic to more advanced.

- Introductory `snakemake slides
  <https://slides.com/johanneskoester/snakemake-short>`_ give a very brief
  overview of what Snakemake is about.
- Live `demo video <https://youtu.be/hPrXcUUp70Y>`_ given by the author.
- The official `short tutorial <https://snakemake.readthedocs.io/en/stable/tutorial/short.html>`_ gives a quick overview.
- The `official Snakemake tutorial
  <https://snakemake.readthedocs.io/en/stable/tutorial/tutorial.html#tutorial>`_
  will give you a more in-depth understanding.
- Additional `tutorial from Titus Brown
  <https://hackmd.io/jXwbvOyQTqWqpuWwrpByHQ?view>`_ on Snakemake
- `Snakemake tutorial specific to NIH's Biowulf
  <https://github.com/NIH-HPC/snakemake-class>`_

Supporting information, tips and tricks
---------------------------------------

The rest of this page offers some suggestions, clarifications, and tips. The
goal is to add some additional information on topics that we typically see new
users struggling with.

Thinking like Snakemake
~~~~~~~~~~~~~~~~~~~~~~~

When teaching Snakemake, it's often useful to "think like Snakemake" to
understand how all the moving parts fit together. For this exercise, let's
create an example Snakefile.

.. code-block:: python

    samples = ["A", "B", "C"]

    rule all:
        input:
            "report.txt"

    rule sort:
        input:
            "{sample}.txt"
        output:
            "{sample}_sorted.txt"
        shell:
            "sort {input} > {output}"

    rule report:
        input:
            expand("{sample}_sorted.txt", sample=samples),
        output:
            "report.txt"
        shell:
            "cat /dev/null > {output}; "
            "for i in {input}; do head -n1 {input} >> {output}"

This file sorts each text file (the ``sort`` rule, 1 input --> 1 output) and
then the first line of each of those sorted files are added to the report (the
``report`` rule, a many input --> 1 output rule or "aggregation" rule).

- Run the first rule encountered. This is the ``all`` rule

- Check the input. Here, it's ``report.txt``. Does that file exist? If
  yes, then we're done. If no, then we need to figure out how to make it. For
  the purposes of this exercise, assume it doesn't exist yet.

- Check the rest of the rules. Are there any rules whose output files match the pattern "report.txt"?

- Yes, the ``report`` rule's output matches. It's actually an exact match and there are no wildcards to worry about.

- OK, so we at least have to run the ``report`` rule. Let's check its input.

- The ``expand()`` function just returns a list. So the input for the ``report``
  rule is ``["A_sorted.txt", "B_sorted.txt", "C_sorted.txt"]``.

- Let's take those one at a time. The first input is ``A_sorted.txt``. Does the
  file already exist? Let's assume no.

- Check the rest of the rules. Are there any rules whose output files match the pattern "A_sorted.txt"?

- Yes, the ``sort`` rule's output matches if we set the ``{sample}`` wildcard
  to be ``A`` (Snakemake does this wildcard matching internally; sometimes it
  gets things wrong, see the "wildcard constraints" section below for some
  hints if that happens)

- OK, so we have to run the ``sort`` rule with the ``{sample}`` wildcard set to
  ``A``. So let's check it's input. What's the input of the ``sort`` rule, if
  we fill in ``A`` as the value of the ``{{sample}}`` wildcard?

- Assuming ``{sample}`` is ``A``, we need ``A.txt``. Does the file already
  exist? Here we'll assume that yes it does exist because there are no other
  rules. Otherwise, the Snakefile could not run; it would complain about
  a missing input file ``A.txt`` because it can't find any rules that could
  make it, and we'd either have to make a rule to
  create it, or make sure our starting input data exists.

- That took care of the first input for the ``report`` rule. On to the next
  one!

- Does ``B_sorted.txt`` exist? Let's assume that it doesn't exist, just like
  ``A_sorted.txt``. We'll go through the same process we did for
  ``A_sorted.txt``. That is, check if any rules' output matches the pattern of
  this file; if so then create value(s) for the wildcard(s) (here,
  ``sample="B"``); fill in the input with the wildcard value; check to see if
  that input exists; if yes, nothing else to do with this "chain" of rule to
  run; if no then we need to figure out what rule will make the output. Again,
  here we're assuming that the starting file ``B.txt`` does exist.

- OK, back to the ``report`` rule, and that last output file, ``C_sorted.txt``.
  Let's now imagine it *does* exist (unlike ``A_sorted.txt`` and
  ``B_sorted.txt``).

- If the file exists, then check to see if it is older than the input. If it's
  older, then we'll need to remake it. If it's newer, it's up-to-date and
  there's nothing more we need to do with ``C_sorted.txt``.

This process of checking input to see if it exists, finding rules whose output
patterns match, filling in wildcards into input and seeing if *that* exists, is
the general process. Keeping this in mind can help when debugging.


Be careful using for-loops in rules
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When initially learning Snakemake, you may be inclined to use ``expand()`` to
get a list of files, and then iterate over them in a for-loop within the rule.

For example in a ``shell:`` block it might look something like:

.. code-block:: python


    samples = ["A", "B", "C"]

    # Don't do this.

    rule example1:
        input:
            expand("{sample}.txt", sample=samples)
        output:
            expand("{sample}.txt.sorted", sample=samples)
        shell:
            "for i in {input}; do "
            "sort $i > $i.sorted; "
            "done"

or for a ``run:`` block it might look something like:

.. code-block:: python


    samples = ["A", "B", "C"]

    # Don't do this either.

    rule example2:
        input:
            expand("{sample}.txt", sample=samples)
        output:
            expand("{sample}.txt.sorted", sample=samples)
        run:
            for fin, fout in zip(input, output):
                shell("sort {fin} > {fout}")

The reasoning for writing a rule like this is typically something like, "I
want to do this thing many times, and in R/Python/Bash I use a for-loop to do
something many times, so let's figure out how to make a for-loop work in
Snakemake".

**However, in general, you don't want to use a for-loop in a rule if the number
of inputs equals the number of outputs**. Let's explain why.

Each of these rules, ``example1`` and ``example2``,  will only run once.
Because of the for-loop, the sorting of sample ``B`` won't be run until sample
``A`` completes sorting. That is, rather than running in parallel, this runs in
serial. So even if we had 3 CPUs to run the sorting of A, B, and C on each one,
the way it is written they will all run on a single CPU, so it will take 3x the
time it would take if running in parallel.

Furthermore, if we add a new sample ``D``, it will force ``A``, ``B``, and
``C`` to run again, even if they were up to date -- wasting time and resources.

Here's what it *should* look like:

.. code-block:: python


    # Do it this way instead.

    samples = ["A", "B", "C"]

    rule all:
        input: expand("{sample}.txt.sorted", sample=samples)

    rule example3:
        input:
            "{sample}.txt"
        output:
            "{sample}.txt.sorted"
        shell:
            "sort {input} > {output}"

This last rule will **run once for each sample, in parallel**. Snakemake
will kick of one job for sample ``A``, another for sample ``B``, and a third
for sample ``C``. If multiple cores have been provided on the command line with
``--cores/-j``, then these three jobs will run in parallel.

**In general, a rule will run in parallel as many times as there are unique
combinations of output files.**

If we look at rules ``example1`` and ``example2`` above, how many unique
combinations of output are there? The answer is *one*, because the ``expand()``
fills in the ``{sample}`` wildcard, giving a single list of the three
filenames.

In contrast, for the ``example3`` rule there are 3 unique sets of output. The
rule will run one time where the single output is ``A.txt.sorted`` (where
sample=A), another time where the single output file is ``B.txt.sorted``
(sample=B) and a third time for ``C.txt.sorted`` (sample=C). Snakemake can run
each of these three rules in parallel, one per CPU as long as there are enough
CPUs to do so (most modern machines have multiple cores).

How about this example -- how many times will the ``fastqc`` rule run?

.. code-block:: python

    samples = ["A", "B", 'C"]
    read_numbers = [1, 2]

    rule all:
        input: 
            expand("{sample}_R{N}_fastqc.html", sample=samples, N=read_numbers)

    rule fastqc:
        input:
            "{sample}_R{n}.fastqc.gz"
        output:
            "{sample}_R{n}_fastqc.html"
        wrapper:
           "v1.25.0/bio/fastqc"

There are two different wildcards in the output, ``{sample}`` and ``{n}``.
There are 3 values for ``sample`` (A, B, C), and 2 values for ``n`` (1, 2) so
it will run 6 times in parallel. 

This is much more subtle than it looks though -- we have ``read_numbers``,
``N``, and ``n``. What does Snakemake actually use? The next section goes into
more detail on this.

Wildcards are NOT global variables
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Consider the following example:

.. code-block:: python

    samples = ["A", "B", 'C"]
    read_numbers = [1, 2]

    rule all:
        input: 
            expand("{sample}_R{N}_fastqc.html", sample=samples, N=read_numbers),
            expand("{sample}_R{N}_fastqc.count", sample=samples, N=read_numbers),


    rule fastqc:
        input:
            "{sample}_R{n}.fastqc.gz"
        output:
            "{sample}_R{n}_fastqc.html"
        wrapper:
           "v1.25.0/bio/fastqc"

    rule count:
        input:
            "{X}_R{Y}.fastq.gz"
        output:
            "{X}_R{Y}.fastq.count"
        shell:
            'LINES=$(wc -l {input} | cut -f1 -d " "); '
            'echo $(($LINES / 4)) > {output}'

At first, this looks pretty confusing:

- We have a list, ``read_numbers``.
- We have a wildcard placeholder ``N`` in the ``expand`` call, and we provide
  the argument ``N=read_numbers``.
- In the ``fastqc`` rule, we have an ``{n}`` wildcard.
- In the ``count`` rule, we have completely different wildcards altogether
  (``X`` and ``Y``)

**There is no variable** ``n`` or ``X`` or ``Y`` or ``sample``. So how does
Snakemake know what to use for ``{n}`` in the output pattern of the ``fastqc``
rule, or ``X`` and ``Y`` in the ``count`` rule?

.. note::

    This section assumes you understand the section above on "Thinking like
    Snakemake", so make sure to go back and read that if you need to.

Let's think like snakemake. Rule ``all`` has an ``expand()``, which results in
a list of filenames. So when Snakemake starts looking at the rules to figure
out what rules it needs to run, *the input of the "all" rule is just a list of
filenames*. That is, there is no ``{N}`` wildcard anywhere.

Let's now take the first filename resulting from that ``expand()`` call,
``A_R1_fastqc.html``. Snakemake looks for a rule whose output matches that
pattern, and identifies the ``fastqc`` rule. Snakemake internally figures out
that the output pattern of the ``fastqc`` rule will match if ``sample="A"`` and
``n=1``. So it sets the values of those wildcards for the input. **The input
wildcards must be found in the output wildcards of the same rule.** So the fact
that we have ``{n}`` in the output means that we must use ``{n}`` in the input.
And we can only use ``{n}`` in the input because it also exists in the output.
But *other* rules' wildcards are *independent*.

For example, when Snakemake looks at the input to the ``all`` rule and finds
``A_R1_fastqc.count``, it finds that ``count`` rule's output pattern will
match. In that case, Snakemake figures out that it needs to make ``X="A"`` and
``Y=1`` for the duration of this rule, and fills in the ``X`` and ``Y``
accordingly for the input.

This was a contrived example; in practice, we generally keep the wildcards
consistent across rules for clarity.


Directed Acyclic Graph (DAG)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is a quick way to visualize the workflow and associated wildcards. Using
this tool at various parts of your snakefile development process can help you
understand where splitting/aggregation steps have occurred and the rule
dependencies of your data.

.. note::

    If you don't already have it in your conda environment, on NIH's Biowulf
    you can get graphviz with ``module load graphviz`` on an interactive node.

- a DAG will include the wildcards
- a rulegraph will **not** include the wildcards

.. code-block:: bash

  snakemake -dag | dot --Tpng > dag.png
  snakemake --rulegraph | dot --Tpng > rulegraph.png

Expand
~~~~~~
The ``expand()`` function is not anything magical or special -- it is simply
a convenient way to generate a regular Python list.

.. code-block:: bash

        states=["Colorado", "Texas", Maryland"]
        rule all:
            input:
                expand("{state}.txt", states_list=state)

is exactly equivalent to:

.. code-block:: bash

        rule all:
            input:
                ["Colorado.txt", "Texas.txt", Maryland.txt"]

Sometimes, you want to "protect" wildcards for feeding them into the next rule.
In earlier versions of Snakemake, you can "escape" the ``{`` by using ``{{``.
The ``expand()`` function will fill in other wildcards, and the ``{{ }}`` will
become ``{ }`` in the resulting list. For example:

.. code-block:: bash

    states=["Colorado", "Texas", Maryland"]
    expand("{state}_{{n}}.txt", state=states)

    # returns:

    ["Colorado_{n}.txt", "Texas_{n}.txt", Maryland_{n}.txt"]

In later versions of Snakemake, you can use the ``allow_missing=True`` argument when calling ``expand()``


.. seealso::

    - Snakemake docs `FAQ on not expanding every wildcard <https://snakemake.readthedocs.io/en/stable/project_info/faq.html#i-don-t-want-expand-to-use-every-wildcard-what-can-i-do>`_
    - Snakemake docs `section on expand() <https://snakemake.readthedocs.io/en/stable/snakefiles/rules.html#the-expand-function>`_
    - `Source code for expand() <https://github.com/snakemake/snakemake/blob/bdde680f01b5d276c68ef2d7ef71536e6d976652/snakemake/io.py#L1199>`_ in a recent version (look in the `snakemake/io.py` file in any version)



Wildcard constraints
~~~~~~~~~~~~~~~~~~~~
Another way to help control the wildcard is to use a ``wildcard_constraint``.
This can be added at the top of your Snakefile (acting as a global variable) or
within your individual rules (local variable). A wildcard constraint can help
minimize all the possible combinations that are filled in. For example in
``{state}_{number}.txt`` you may want to specify that ``{state}`` may only be
filled in with the following names: "Colorado", "Texas", or "Maryland" and
``{number}`` with "1", "2", "3". Why? Because maybe you have a list that pulls
all the possible combinations so you don't want something called
"1_Colorado.txt" or "2_3.txt" (total of 18 possible unique filename
combinations), you want something like "Colorado_1.txt", "Colorado_2.txt",
"Colorado_3.txt", "Texas_1.txt", "Texas_2.txt", etc (total of 9 possible unique
filename combinations). Constraints are specified using regular expressions, so
it may look like this::

    wildcard_constraints:
        state="Colorado|Texas|Maryland",
        number="1|2|3"


.. seealso::

    - `wildcard constraint section of tutorial <https://snakemake.readthedocs.io/en/stable/tutorial/additional_features.html#constraining-wildcards>`_
    - `wildcards section <https://snakemake.readthedocs.io/en/stable/snakefiles/rules.html#snakefiles-wildcards>`_ of the Snakemake docs has some more info
    - `Python regular expression docs <https://docs.python.org/3/library/re.html>`_
    - `Pythex <https://pythex.org/>`_, a great website for interactively building/debugging regular expressions

Conda envs and ``run:`` blocks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You may find it useful to use ``conda:`` directives in rules so that the rule
runs in its own environment. Keep in mind though that you can't use this
mechanism if you have a ``run:`` block. A ``run`` block doesn't work with
a separate conda environment because the Python code is sort of interleaved
within the Snakefile, and there's no way to activate a conda environment from
within a running Python instance and somehow swap over all running code from
memory into the new environment. ``shell``, ``wrapper``, and ``script`` are all
fine to use with the ``conda:`` directive, so the solution is typically to
refactor the code into a script or wrapper.

.. seealso::

    This is also discussed in `this Snakemake FAQ
    <https://snakemake.readthedocs.io/en/stable/project_info/faq.html#why-can-t-i-use-the-conda-directive-with-a-run-block>`_.

