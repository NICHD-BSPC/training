Bulk RNA-seq analysis
=====================

RNA-seq measures what genes are transcribed. We typically differentiate between
bulk RNA-seq (measuring transcripts from many cells mixed together) and
single-cell RNA-seq (keeping track of which transcript measurements came from
which cell). This page is about bulk RNA-seq.

Harvard Bioinformatics Core training materials
----------------------------------------------
These tutorials are the best way to learn RNA-seq:

- **TUTORIAL 1**: `Introduction to (bulk) RNA-seq using High-Performance Computing <https://hbctraining.github.io/Intro-to-rnaseq-hpc-salmon-flipped/schedule/links-to-lessons.html>`_. This walks you through the primary processing, mostly using command-line tools.
- **TUTORIAL 2**: `Introduction to Differential Gene Expression Analysis <https://hbctraining.github.io/DGE_workshop_salmon_online/schedule/links-to-lessons.html>`_. This walks you through differential expression analysis in R.

Note that these have prerequisites of `Introduction to shell
<https://hbctraining.github.io/Intro-to-shell-flipped/schedule/links-to-lessons.html>`_
and `Introduction to
R <https://hbctraining.github.io/Intro-to-R-flipped/schedules/links-to-lessons.html>`_
respectively.

Upon completing those two tutorials, you will be able to run arbitrary RNA-seq
analyses, and you may be ready to learn Snakemake and either write your own
workflows or use something like `lcdb-wf <https://github.com/lcdb/lcdb-wf>`_.

.. note::

    The Harvard Bioinformatics Core tutorials sometimes change locations or get
    updated or split. The above links are checked periodically for correctness,
    but if you can't find the linked tutorials, look around on their
    `main training page <https://github.com/hbctraining/main>`_.

    These tutorials make some assumptions about using Harvard's
    high-performance compute cluster, O2. There are commands related to
    installing or activating software that you will need to adapt to your local
    HPC or other computing environment.

    We have not rewritten these tutorials for NIH's Biowulf, for example.

Skills for RNA-seq
------------------
This gives a very rough sense of what beginner/intermediate RNA-seq skills
might look like:

Level 1
~~~~~~~
- Be able to describe the lines and fields of the following formats: FASTQ, FASTA, BAM, GTF
- Be able to compare and contrast the same formats (what information is
  included/missing; how are they created; when you would use them)
- Locate and prepare reference data (including aligner/pseudoaligner indexes)
- Run FastQC on FASTQ and BAM files
- Align reads with STAR, HISAT2, or other aligner and quantify reads with
  featureCounts
- Quantify reads with Kallisto or Salmon
- Import a counts table into R
- Run basic 2-condition DESeq2 differential expression analysis
- Find the most highly-changed genes
- Plot an MA plot or volcano plot
- Export results to TSV or Excel
- Do functional enrichment analysis to find pathways enriched in changed genes

Level 2
~~~~~~~
- Run QC using multiple tools (preseq, rRNA contamination, Picard, RSeQC, MultiQC)
- Interpret QC reports to make suggestions for future bench work
- Interpret raw p-value histograms
- Be able to describe what fold-change shrinkage is doing
- Be able to describe how DESeq2 handles low counts
- Work with more complex experimental designs (batch effects, interaction
  terms) in DESeq2 and explain the results
- Visualize data (bam, bigwig) in a genome browser
- Using automated reproducible workflows (Snakemake, Nextflow, etc)

Other resources
---------------
The remainder of this page goes into some more detail on various aspects of
RNA-seq analysis, to be used as supplemental material.

- The introductory paper `Hitchiker's guide to expression analysis
  <https://doi.org/10.1146/annurev-biodatasci-072018-021255>`_ is co-authored
  by many big names in the field and gives a great overview and history.

- The `DESeq2 paper
  <https://genomebiology.biomedcentral.com/articles/10.1186/s13059-014-0550-8>`_,
  while going over the details of the popular differential expression
  algorithm, is very approachable even for someone with not a lot of
  math/stats/algorithm background.

- If you've done the tutorials above, you will have seen the `experimental
  planning considerations
  <https://hbctraining.github.io/Intro-to-rnaseq-hpc-salmon-flipped/lessons/02_experimental_planning_considerations.html>`_
  section from HBC training, which is a very good discussion on how much to
  sequence (more samples or more depth?), how to avoid a confounded experiment,
  and preventing batch effects in general.

- Especially when doing `in vitro` research with cell lines, it's important to
  think about what a replicate really is. `This blog post
  <https://paasp.net/accurate-design-of-in-vitro-experiments-why-does-it-matter/>`_
  is a good discussion of the difference between technical replicates and
  biological replicates `in vitro`.

- A library may be stranded, reverse stranded, or unstranded depending on what
  kit was used for the library prep. `These figures
  <https://github.com/igordot/genomics/blob/master/notes/rna-seq-strand.md>`_
  help visualize the different strand-specific protocols. If you're unsure,
  RSeQC's `infer_experiment.py
  <http://rseqc.sourceforge.net/#infer-experiment-py>`_ can help you figure it
  out given a BAM and a BED file of genes.

- We base part of our RNA-seq template off of the `Bioconductor RNA-seq
  workflow
  <https://www.bioconductor.org/packages/devel/workflows/vignettes/rnaseqGene/inst/doc/rnaseqGene.html>`_, which shows all the steps of RNA-seq from within R.

- In BSPC, we develop and maintain `lcdb-wf
  <https://github.com/lcdb/lcdb-wf>`_, which automates much of RNA-seq, and
  provides an extensive RMarkdown file for downstream analysis. 

- The `DESeq2 vignette
  <https://bioconductor.org/packages/release/bioc/vignettes/DESeq2/inst/doc/DESeq2.html>`_
  is the authoritative source on how to use DESeq2.

- The `DESeq2 paper
  <https://genomebiology.biomedcentral.com/articles/10.1186/s13059-014-0550-8>`_
  is very well written, and describes how DESeq2 is actually working

- A nice treatment of `interaction terms
  <http://genomicsclass.github.io/book/pages/interactions_and_contrasts.html>`_,
  along with plots to help understand what's being tested.

- For complex experimental designs, this `tutorial
  <https://github.com/tavareshugo/tutorial_DESeq2_contrasts/blob/main/DESeq2_contrasts.md>`_
  shows an elegant, general method for creating the proper contrasts.

- You may have heard the terms RPKM, FPKM, RPM, and TPM. Which to use? Short
  answer: use TPM. Longer answer, with figures, is here:
  https://ro-che.info/articles/2016-11-28-rna-seq-normalization. The
  accompanying `slides <https://ro-che.info/docs/2016-11-27-rna-seq.pdf>`_ are
  useful for discussion.
