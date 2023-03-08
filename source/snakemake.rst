.. _snakemake:

Snakemake
=========

Snakemake is a subset of Python that allows for workflow management using
"rules" to dictate input/output files. It allows for scalable workflows,
utilizing file pattern matching. Snakemake is useful for BSPC as it allows us
to quickly develop reuable code that is scalable. The abstraction of the rules
also allows us to upload these workflows and code onto github without
sacrificing privacy.


- Introductory `snakemake slides
  <https://slides.com/johanneskoester/snakemake-short>`_
- Live `demo video <https://youtu.be/hPrXcUUp70Y>`_
- `Official Snakemake tutorial
  <https://snakemake.readthedocs.io/en/stable/tutorial/tutorial.html#tutorial>`_
- Additional `tutorial from Titus Brown
  <https://hackmd.io/jXwbvOyQTqWqpuWwrpByHQ?view>`_ on Snakemake
- `Snakemake tutorial specific to NIH's Biowulf
  <https://github.com/NIH-HPC/snakemake-class>`_

Typical Setup of Snakefile
''''''''''''''''''''''''''

rule all:
    input: "finalOutput.txt"

rule one:
    input: "initFile.txt"
    output: "outputRule1.txt"
    shell:
        a bash command

rule two:
    input: "outputRule1.txt"
    output: "finalOutput.txt"
    shell:
        a bash command


Directed Acyclic Graph (DAG)
''''''''''''''''''''''''''''

A quick way to visualize the workflow and associated wildcards. Using this tool
at various parts of your snakefile development process can help you understand
where splitting/aggregation steps have occurred and the rule dependencies of
your data.

It can be accessed via the terminal:

1. load graphviz

``module load graphviz``

2. create either a dag OR a rulegraph
- a DAG will include the wildcards
- a rulegraph will **not** include the wildcards

``snakemake -dag | dot --Tpng > dag.png`` ``snakemake --rulegraph | dot --Tpng
> rulegraph.png``

Useful Hints/Features
'''''''''''''''''''''
- Expand: This helps you expand the rule all to implement established lists and
  do to splitting steps within individual rules. We use this in BSPC for our
  sampletables, usually. An example of this would be:

        states=["Colorado", "Texas", Maryland"] rule all: input:
        expand("{state}.txt", states_list=state)

    When we implement the ``expand`` function, it allows us to parallelize our
    output files. Now we can run hypothetical rule1, rule2, rule3 on an __n__
    number of states.

- Wildcards: These are used for file pattern recognition. Wildcards can be
  named anything and are not tied to any singular variable. They are text
  wrapped in { }.

    You can also "protect" these wildcards for feeding them into the next rule
    using {{ }}. For example, {{state}}_{number}.txt will be looking to fill in
    all the possible {number} combinations but will not for {{state}} until the
    next rule. So you may have an output of {{state}}_1.txt, {{state}}_2.txt,
    and {{state}}_3.txt and then later you can fill this {state} wildcard in
    another rule.

    Another way to help control the wildcard is to use
    a ``wildcard_constraint``. This can be added at the top of your Snakefile
    (acting as a global variable) or within your individual rules (local
    variable). A wildcard constraint can help minimize all the possible
    combinations that are filled in. For example in {state}_{number}.txt you
    may want to specify that {state} may only be filled in with the following
    names: "Colorado", "Texas", or "Maryland" and {number} with: "1", "2", "3".
    Why? Because maybe you have a list that pulls all the possible combinations
    so you don't want something called "1_Colorado.txt" or "2_3.txt" (total of
    18 possible unique filename combinations), you want something like
    "Colorado_1.txt", "Colorado_2.txt", "Colorado_3.txt", "Texas_1.txt",
    "Texas_2.txt", etc (total of 9 possible unique filename combinations). You
    will establish wildcard constraints using the regex "|" so it may look like
    this:

        wildcard_constraints: state="Colorado|Texas|Maryland" number="1|2|3"

- Threads: specifying the number of threads for each job will help allocate the
  appropriate amount of cpus when sending jobs to the cluster. When you do not
  have the same threads requested in your Snakefile rules as your cluster
  requests (for BSPC these are specified in clusterconfig.yaml), Biowulf will
  be constantly competing and arguing with Snakemake about cpu allocation. This
  causes your jobs to be slower. It also is best practice to have these match
  up with the cluster config.

- Snakemake -np not working? Possible solutions may include: (1) need to unlock
  the directory using ``snakemkae --unlock`` (2) needing to delete the dotfiles
  using ``rm -r .snakemake``. Both of these issues have to do with caching and
  usually occur when you've run your snakefile under ``snakemake -np`` multiple
  times.

BSPC-specific
'''''''''''''

Both ``clusterconfig.yaml`` and ``WRAPPER_SLURM`` can be added to your
directory so that you can send cluster jobs into the Biowulf HPC. You would do
this for parallelization, speed, when you need bigger nodes, etc. It will
divide each of the rules into cluster jobs, so when you check the User
Dashboard, you will have labeled (rule name) output strE and strO files.

.. todo::

    need lots more context here -- why we use snakemake in bspc and why it's
    generally useful
