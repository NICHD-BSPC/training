.. _genomics-formats:

Genomics overview
=================

Overviews
---------

Recent reviews are probably the best place to get an overview of
high-throughput sequencing.The goal is not to understand everything
discussed in these reviews, rather, the goal is to get exposed to
terminology, get a big-picture overview of the process and limitations,
and prime yourself for further reading. You’ll probably get a lot more
out these by re-reading them after you gain some experience. The rest of
this page will be about the specifics, and getting more experience.

This review article from Molecular Cell
(https://www.cell.com/molecular-cell/fulltext/S1097-2765(15)00340-8)
gives a good overview of high-throughput sequencing. It’s fairly
up-to-date, comparing Illumina with Pac Bio, Nanopore, and Ion Torrent
as well as giving a brief overview of the kinds of assays that are
commonly performed.

Here are some recent reviews on specific assays:

-  Review on RNA-seq:
   https://genomebiology.biomedcentral.com/articles/10.1186/s13059-016-0881-8
-  Review on ChIP-seq:
   https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5444249/
-  Review on SNV calling:
   https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5852328/
-  2016 review of sequencing technology:
   https://www.nature.com/articles/nrg.2016.49

The site `“SequencEng” <http://education.knoweng.org/sequenceng/>`_ has
interactive flowcharts of high-throughput sequencing techniques, along with
tool suggestions. This can be useful for getting a big-picture view of the
steps of various workflows.

Genome Browsers
---------------

As with any data analysis, the first thing you should do with your data
is to visualize it. Genomic data is no different, so it makes sense that
the first thing to learn about high-throughput sequencing is how to
visualize it. When we look at file formats below, loading them in a
genome browser will help you understand them better.

You will probably always be learning new things about these browsers;
for now just install/load them and poke around to get a feel for them.
Below we’ll upload specific files to experiment with.

IGV
---

https://software.broadinstitute.org/software/igv/

IGV (Integrated Genome Viewer) is a standalone Java program. It’s best used for
local data, and excels at detailed looks at BAM and VCF files. Since it can
read files straight off disk, this is the preferred option for data that can’t
be made public.

UCSC Genome Browser
-------------------

https://genome.ucsc.edu/

The UCSC Genome Browser is a web-based browser. It looks like the design
hasn’t changed since the 90s, but it is extremely powerful and is
constantly updated. It has a tremendous amount of data already loaded,
and is best used for sharing data with others or comparing with existing
data.

Other genome browsers
---------------------

- `SeqMonk <https://www.bioinformatics.babraham.ac.uk/projects/seqmonk/>`_ has
  some interesting visualization options
- `WashU Epigenome Viewer <http://epigenomegateway.wustl.edu/browser/>`_ allows
  visualization of long-range interaction data like Hi-C

File formats
------------
The field has settled down into a reasonably small set of file formats
that are commonly used by various tools. Getting to know these file
formats and what they are used for is important for understanding how to
use various tools. Some exercises are provided below to reinforce what
you’ve learned in “Getting started on the command line”. There are some
useful hints provided as well.

For example, an RNA-seq experiment will start with FASTQ files from the
sequencer. You'll need to align these to the genome to create BAM files, and
then count reads in genes where the gene annotations are provided in a GTF
file.

For a ChIP-seq experiment, you'll start with FASTQ files, align them to the
genome to get a BAM, and then call peaks to get BED files you can view in
a genome browser.

For variant calling, you'll start with FASTQ files, align them to the genome to
get a BAM, and run variant-calling tools to get a VCF file you can view in
a genome browser.

An aside
~~~~~~~~

Some of the file formats described below are position-based. Please read the
following posts talking about 0-based and 1-based coordinate systems to figure
out what this means:

- https://standage.github.io/on-genomic-interval-notation.html
- https://www.biostars.org/p/84686/

FASTQ
~~~~~

Raw reads come off the sequencer in FASTQ format. Each read is
represented by 4 lines only one of which is the sequence itself. Note
that there is no genomic position information in a FASTQ file. It has to
be aligned to a reference sequence to figure out where each read came
from. The wikipedia page on FASTQ is probably the best resource for
learning about this format and its sometimes-frustrating idosyncracies:
https://en.wikipedia.org/wiki/FASTQ_format.

Here is an example FASTQ file, gzipped:
https://github.com/lcdb/lcdb-test-data/raw/master/data/rnaseq_samples/sample1/sample1.tiny_R1.fastq.gz

Since FASTQ files do not have coordinates, we cannot visualize these
files in a genome browser.

-  How many reads are in this FASTQ file? (command at the bottom of this
   page if you need help)
-  What quality score encoding does it use?

BAM
~~~

When FASTQ files are aligned to a reference genome, the output is
typically a BAM format file (or sometimes the uncompressed version, SAM
files). There is lots of information in each line of a BAM file. The BAM
specification https://samtools.github.io/hts-specs/SAMv1.pdf gives
excruciating detail on this format, but is worth reading through. You
will probably re-read that document many times over your career, don’t
worry if you don’t fully understand it! Important parts to grasp this
time around are the FLAG field, where and how genomic coordinates are
stored, and that chromosome information is stored in the header int the
@SQ lines. Section 1 is the most important part:

To experiment with visualization, scroll down to Example #1 on this
page: https://genome.ucsc.edu/goldenPath/help/bam.html, and view the BAM
in UCSC Genome Browser.

Then download the BAM file from that example
(https://genome.ucsc.edu/goldenPath/help/examples/bamExample.bam). You
will also need to download the index
(https://genome.ucsc.edu/goldenPath/help/examples/bamExample.bam.bai,
more on indexes later). Then load the BAM into IGV.

-  how do the browsers display the same data differently?

BAM files are compressed in a very specific way. To read them correctly,
we need to use the samtools program. See the More on installing programs
section for ways of installing it (either manually, load a module on
Biowulf, or conda install samtools). Then, use the samtools view program
to view it (hint: probably want to pipe to head or less).

Hint: the column command helps nicely print tab-delimited files, and the
-S argument to less ignores wrapping. So a convenient way of viewing BAM
files on the command line is:

.. code-block:: bash

   samtools view bamExample.bam | column -t | less -S

-  how many reads are in this BAM file?

We will do some more exercises on this BAM file in the samtools section.



BED
~~~

BED files represent blocks of coordinates in the genome. While FASTQ and
BAM are primarily used for sequences, BED files can represent anything
that can be described in terms of genomic coordinates (chromsome, start
position, stop position). This can be protein binding sites, genes,
transcripts, primers, or simply loci of interest. BED files can be
simple 3-column files or can be more complicated with 12 columns. Given
their simplicity they are probably one of the most common of the
interval formats.

BED format description:
https://genome.ucsc.edu/FAQ/FAQformat.html#format1. Be sure to try out
the examples there as well to visualize BED files. Try changing the
example files to see how the visualization changes.

Here’s another BED files to experiment with. These are ChIP-seq peaks
for a protein called CP190 in Drosophila:
https://raw.githubusercontent.com/daler/pybedtools/master/pybedtools/test/data/Cp190_Kc_Bushey_2009.bed

-  how many peaks are there?
-  how many peaks are there on each chromosome?

GTF and GFF
~~~~~~~~~~~

While BED files can represent genes, there is no good way for a BED file
to represent hierarchical relationships between features. However GTF
and GFF files do allow this. For example they can encode which exons
belong to which transcripts and which transcripts belong to which gene.
Even though each individual line is not much more complex than a BED
file, the file overall is more complicated due to the hierarchical
connections between lines. GTF and GFF files are most commonly used when
when counting reads in genes during RNA-seq analysis, though any time
you’re working with gene annotations they are likely to be found in GFF
or GTF format.

GTF format description: http://mblab.wustl.edu/GTF22.html

GFF format description:
https://useast.ensembl.org/info/website/upload/gff.html

To practice, try the GTF example on UCSC:
https://genome.ucsc.edu/FAQ/FAQformat.html#format4. Note that UCSC’s GFF
format is a really old version of the format; converting a typical GFF
to work on UCSC is outside the scope of this exercise.

Here’s another example file. This will not work directly in UCSC, but
you can look at it in the command line (note it is gzipped):
https://github.com/daler/pybedtools/raw/master/pybedtools/test/data/dm3-chr2L-5M.gff.gz

-  how many features?
-  what is the most common feature type?

Parsing the attributes field of GTF/GFF gets pretty annoying; we’ll hold
off on that for now.

VCF
~~~

VCF files are used for storing variant information and the additional
metadata that goes along with it. Typically, any kind of variant-calling
involves VCF files.

VCF format description: https://samtools.github.io/hts-specs/VCFv4.2.pdf.
Lots of details and terminology here!

To practice, scroll down to Example #1 on this page to visualize:
https://genome.ucsc.edu/goldenPath/help/vcf.html

That example has a lot samples; a smaller one that’s easier to look at
is
https://raw.githubusercontent.com/vcflib/vcflib/master/samples/sample.vcf.
In that example:

-  which line has a quality score <10?
-  which variant has the highest total depth of coverage?
-  which variant has the highest genotype quality?

Standard tools
--------------

samtools
~~~~~~~~
BAM files are compressed in a very specific way. To read them correctly,
we need to use the samtools program. See the More on installing programs
section for ways of installing it (either manually, load a module on
Biowulf, or conda install samtools). Then, use the samtools view program
to view it (hint: probably want to pipe to head or less).

Hint: the column command helps nicely print tab-delimited files, and the
-S argument to less ignores wrapping. So a convenient way of viewing BAM
files on the command line is:

.. code-block:: bash

   samtools view bamExample.bam | column -t | less -S

-  how many reads are there in this BAM file?
-  make an index for the BAM file, and then load the BAM file into IGV
-  how many unmapped reads are there in this BAM file?
-  how many reads on the plus strand, how many on the minus?
-  how many reads are there on chromsome 21, between these coordinates:
   21:33019966-33020000
-  are there sequences in the header that have no reads?

FastQC
~~~~~~

Generally the first, quick step for quality control (QC) of sequenced
files is to run FastQC on each FASTQ file. It’s pretty straightforward
to run, either through a GUI or from the command line. Try checking the
example FASTQ files from the fastq section above.

https://www.bioinformatics.babraham.ac.uk/projects/fastqc/

BEDTools
~~~~~~~~

Any time you’re working on genomic intervals, whether they’re stored in
BAM, BED, GTF, GFF, or VCF, you should be reaching for BEDTools. There
are many subprograms of BEDTools, and you’ll eventually want to
familiarize yourself with them all.

Aaron Quinlan, the author of BEDTools, has a tutorial available at
http://quinlanlab.org/tutorials/bedtools/bedtools.html. It’s well worth
your time to go through this and understand how the tools work.
Especially useful are the “puzzles” at the end which will test your
knowledge.

Hints
-----

How many reads in the fastq? ``zcat sample1.tiny_R1.fastq.gz | wc -l``
gets the line count (using zcat to uncompress on the fly), but then we
need to divide by 4 since one record takes up 4 lines. A tricky way of
doing this all in one line is the following, which takes advantage of
echo’s arithmetic expansion with the $(()) syntax:

.. code:: bash

   zcat sample1.tiny_R1.fastq.gz | echo $((`wc -l`/4))

.. todo::

    To tie everything together, add examples of figures from papers, and
    explain how all of these steps come together.

.. todo::

    For genomics, write the following:

    - Aligners (Bowtie2, HISAT2, BWA, STAR)?

    - Links to example RNA-seq and ChIP-seq workflows (possibly from
      https://hbctraining.github.io/main/)

    - bedGraph, wig, bigBed, bigWig, chromsizes

    - example RNA-seq and ChIP-seq bash scripts scale that up to Snakemake
      workflows?

