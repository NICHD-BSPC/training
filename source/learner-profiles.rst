.. _profiles:

Learner profiles
================

Skill levels and training goals vary greatly across individuals. As a result,
it can be challenging to decide what to learn. This page describes
some common learner profiles we have encountered at NICHD, recommendations on
what topics each should learn, and in what order.


I want to run my own scRNA-seq analysis
---------------------------------------

If this is your goal, you'll need to decide at what point you want to jump in
to the analysis:

1. **Someone has already prepared input files for me.** In this case, someone
   has already run the command-line tools to prepare files. For 10X Genomics
   data, this is generally a directory containing counts matrix file and
   barcodes, so you don't need to learn the command line in order to generate
   that. If you like jumping into the deep end, you can start with
   :ref:`single-cell-r` or :ref:`single-cell-python`. If you get frustrated or
   confused, or prefer starting from first principles, then you should start
   with :ref:`r` or :ref:`python`. And if you need help choosing between those,
   then see :ref:`choosing-r-python`.


2. **I want to run it starting from raw data.** In this case, you have raw
   FASTQ files from the sequencer. You'll need to learn some basic
   :ref:`command-line` to be able to manipulate files and run alignment tools
   like 10X Genomics *cellranger* tool to prepare the files. You'll then need
   to learn :ref:`python` or :ref:`r`, and see :ref:`single-cell-r` or
   :ref:`single-cell-python`.

3. **My results do not match the tutorials.** It happens all the time: we
   follow a tutorial using our own data, but the plots we make look strange
   compared to the plots in the tutorial. Did we do something wrong? Is there
   some interesting biology here? Is there a bug in the software? Answering
   those questions takes a lot of effort and takes a lot of experience. Often
   it takes reading the code to understand what the software is doing, and
   possibly write new code to fix the issue. This requires learning lots of
   :ref:`r`, or you can always drop us a line, nichdbspc@nichd.nih.gov.


I want to run my own (bulk) RNA-seq analysis
--------------------------------------------

1. **Someone has already made a counts matrix for me.** In this case, someone
   has aligned reads and prepared a count matrix for you. You will need to
   learn some :ref:`r`, and you will likely want to run DESeq2. See
   :ref:`rnaseq` for more on this.

2. **I want to run it starting from raw data.** In this case, you have FASTQ
   files and want to analyze your own RNA-seq data. You'll need to learn
   :ref:`command-line`, either learn how to install tools on your own Mac or
   Linux machine (see :ref:`installing-tools`) or use :ref:`biowulf`. See
   :ref:`rnaseq` for the resources for learning these steps. It will help a lot
   if you lear :ref:`genomics-formats` as well.

I want to learn data science
----------------------------

.. todo::

    write data science learner profile

I want to become a bioinformatician
-----------------------------------

.. todo::

    write bioinformatician learner profile

I want to collaborate with BSPC
-------------------------------

When collaborating with labs, we set up a joint shared directory on Biowulf and
set up conda environments so that everyone with access to that space can use
the exact same software and versions. See :ref:`collaborating-with-bspc` for
more details, but you will at least need to know :ref:`command-line` and
:ref:`biowulf`.

I want to join BSPC 
-------------------

For new additions to our group, you'll need to know :ref:`command-line`,
:ref:`vim` or :ref:`emacs` (preferrably Vim because that's what the majority of
us use and so we can help), :ref:`r`, :ref:`python`, :ref:`reproducibility`,
:ref:`snakemake`, :ref:`genomics-formats`, :ref:`git`, :ref:`gitlab`, and
:ref:`biowulf`


.. todo::

    The learner profiles link to the following pages, many of which still need
    writing:

    - DESeq2
    - Galaxy
    - Reproducibility
    - Installation
    - Collaborating with BSPC
    - Biowulf
    - lcdb-wf
    - RNA-seq
