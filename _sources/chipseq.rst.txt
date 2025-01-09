ChIP-seq analysis
=================

In comparison to RNA-seq analysis, ChIP-seq analysis can be a bit more
complicated. The experimental protocol itself is more complex, and has
additional variability imposed by antibody effectiveness.

Fundamentally, ChIP-seq is about finding where on chromatin a protein of
interest binds. To do this, we generally convert aligned reads into signal over
the genome, and wherever there is a large pileup of reads, we call that as
a "peak" and infer that the protein was found there.

This aspect of peak-calling can also be used with other chromatin-related
assays like ATAC-seq and CUT&RUN albeit with some minor modifications. In
general, peak-calling is more of an art than a science. Multiple peak-calling
algorithms will often give different results, so a big part of ChIP-seq
analysis is understanding which algorithms are most appropriate for your
particular experiment and making well-justified decisions about which peaks to
use as the "final" set.

**The best one-stop-shop** for learning about ChIP-seq analysis is the Harvard
Bioinformatics Core's `Introduction to ChIP-seq using high-performance
computing
<https://hbctraining.github.io/Intro-to-ChIPseq/schedule/2-day.html>`_ starts
with an overview of ChIP-seq, and continues through working with Linux, project
organization, alignment, QC, peak-calling, and comparing peaks between conditions.

`Nakato 2021
<https://www.sciencedirect.com/science/article/pii/S1046202320300591>`_ has
a high-level overview of ChIP-seq, and may be more succinct than the HBC
workshop linked above.

`Eder 2022
<https://genomebiology.biomedcentral.com/articles/10.1186/s13059-022-02686-y>`__
compares methods for differential ChIP-seq, and has helpful decision trees for
figuring out what algorithm to use under what circumstances.

Technical details
-----------------
The current ENCODE guidelines for ChIP-seq can be found `here
<https://www.encodeproject.org/documents/ceb172ef-7474-4cd6-bfd2-5e8e6e38592e/@@download/attachment/ChIP-seq_ENCODE3_v3.0.pdf>`_.
Here are some highlights:

- two or more biological replicates
- for mammalian genomes, 20 million usable fragments for narrow peaks (a
  fragment is either one read for single-end sequencing, or one pair for
  paired-end sequencing)
- for mammalian genomes, 45 million usable fragments for broad peaks

Input or H3 as a control? `Flensburg 2014
<https://www.frontiersin.org/articles/10.3389/fgene.2014.00329/full>`_ compares
the use of whole-cell extract (input) vs H3 as a control for histone
modification ChIP-seq. They found that the called peaks are mostly similar no
matter which control is used. As you might expect, when using H3 there is
a depletion of signal around the TSS due to expected nucleosome depletion.
While there may be corner cases where the particular biological questions may
cause one to be more biologically meaningful, in general using input for
histone modifications seems well-justified.
