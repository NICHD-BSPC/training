.. _variant-calling:

Variant calling
===============

Variant calling is the process of looking for differences in the genome. This
could be looking for differences between individuals (germline calling) or
between a tumor and matched normal tissue (somatic calling).


- `Koboldt 2020
  <https://genomemedicine.biomedcentral.com/articles/10.1186/s13073-020-00791-w>`_
  is a good overview of variant calling, including different technologies,
  differences between germline and somatic calling, and a sketch of the
  workflow. `Figure
  2 <https://genomemedicine.biomedcentral.com/articles/10.1186/s13073-020-00791-w/figures/2>`_
  is especially good to study as it has examples of incorrectly called variants
  and shows how to critically evaluate calls.

- Data Carpentry's "Wrangling Genomics" workshop has a `section on variant
  calling
  <https://datacarpentry.org/wrangling-genomics/04-variant_calling.html>`_
  that walks through some of the basics. Depending on which machine you're
  running it on, you may want to start at the `beginning of the workshop
  <https://datacarpentry.org/genomics-workshop/>`_ which walks you through
  installing the required software. If this is your first time working on the
  command line, then the entire workshop would be good to go through.

- The Broad's `Genome Analysis Toolkit (GATK)
  <https://gatk.broadinstitute.org/hc/en-us>`_ is the standard germline variant
  calling workflow (often called "GATK best-practices workflow") that can also
  do somatic calling and germline CNV. That site includes `extensive tutorials
  <https://gatk.broadinstitute.org/hc/en-us/sections/360007226631-Tutorials>`_
  and `blog posts
  <https://gatk.broadinstitute.org/hc/en-us/sections/360007373191-Blog>`_ that
  give a lot of detail and context.



Terminology
-----------

:SNV:
    Single-nucleotide variant, typically use GATK to call these.

:indel:
    Insertion or deletion. Typically assumed to be small-ish (<10 bp), called by GATK.

:SV:
    Structural variant. Typically assumed to be large (>1kb). Can include
    complicated inversions, translocations, and copy-number variants (which are
    often considered a separate class). SVs are best detected with long-read
    sequencing and need specialized algorithms to detect them. This is a hard
    problem, and different algorithms are able to detect different kinds of
    SVs.

:CNV:
    Copy number variants. This is a stretch of DNA that is duplicated. Often
    assayed by aCGH (array comparative genome hybridization).

:germline variant calling:
    The process of identifying places in a genome that differ from the
    reference genome. If otherwise unspecified, it usually means SNV and indel
    calling (rather than SV or CNV). 

:somatic variant calling:
    Calling variants that arose in a tumor compared to normal tissue is somatic
    varant calling. It is important to note that `somatic calling is NOT simply
    a difference between two callsets
    <https://gatk.broadinstitute.org/hc/en-us/articles/360035890491-Somatic-calling-is-NOT-simply-a-difference-between-two-callsets>`_,
    it's quite a bit more complicated than that.


Interpreting and prioritizing variants
--------------------------------------

Calling variants is just the first step. You'll probably find thousands. Which
ones are meaningful?

Variant annotation is the process of adding extra information to each variant.
For example, the location of each variant relative to genes, known clinical
relevance, and how common a variant is in the general population.

`Dashti 2018 <https://www.future-science.com/doi/10.2144/000114492>`_ provides
lots of practical advice about tools, databases, and thresholds to use and is
worth a careful read.

Example tools for this include:

- `SnpEff <http://pcingola.github.io/SnpEff/>`_
- `ANNOVAR <https://annovar.openbioinformatics.org/en/latest/>`_
- `VEP <https://useast.ensembl.org/info/docs/tools/vep/index.html>`_
- `vcfanno <https://github.com/brentp/vcfanno>`_ supports arbitrary user-specified annotations

There are many databases, each with their own uses. There is no single database
that aggregates them all, though dbNSFP comes the closest. Here is an
incomplete list:

- `dbNSFP <https://sites.google.com/site/jpopgen/dbNSFP>`_ compiles prediction
  scores for non-synonymous single-nucleotide variants for many databases (some
  of which are also listed below). For one-off queries, there is a `web
  application <http://database.liulab.science/dbNSFP>`_. This is probably the
  best one-stop-shop for variant annotation. But when digging deeper on a small
  number of variants, you may find it useful to submit those variants to the
  tools

  > Its current version is based on the Gencode release 29 / Ensembl version 94
    and includes a total of 84,013,490 nsSNVs and ssSNVs (splicing-site SNVs).
    It compiles prediction scores from 37 prediction algorithms (SIFT, SIFT4G,
    Polyphen2-HDIV, Polyphen2-HVAR, LRT, MutationTaster2, MutationAssessor,
    FATHMM, MetaSVM, MetaLR, CADD, CADD_hg19, VEST4, PROVEAN, FATHMM-MKL
    coding, FATHMM-XF coding, fitCons x 4, LINSIGHT, DANN, GenoCanyon, Eigen,
    Eigen-PC, M-CAP, REVEL, MutPred, MVP, MPC, PrimateAI, GEOGEN2,
    BayesDel_addAF, BayesDel_noAF, ClinPred, LIST-S2, ALoFT), 9 conservation
    scores (PhyloP x 3, phastCons x 3, GERP++, SiPhy and bStatistic) and other
    related information including allele frequencies observed in the 1000
    Genomes Project phase 3 data, UK10K cohorts data, ExAC consortium data,
    gnomAD data and the NHLBI Exome Sequencing Project ESP6500 data, various
    gene IDs from different databases, functional descriptions of genes, gene
    expression and gene interaction information, etc.

- `dbSNP <https://www.ncbi.nlm.nih.gov/snp/docs/entrez_help/>`_ is hosted by
  NCBI and is a collection of known SNPs corresponding with an `rsID`, a unique
  identifier. If your variant calling found variant in dbSNP, annotation tools
  will generally annotate it with the rsID.

- `dbVar <https://www.ncbi.nlm.nih.gov/dbvar/>`_ is similar to dbSNP but for structural variation

- `ClinVar <https://www.ncbi.nlm.nih.gov/clinvar/>`_ stores clinical information about variants

- `ClinGen <https://www.clinicalgenome.org/>`_ is a curated resource of
  clinically-relevant variants in genes (read more about the differences
  between ClinVar and ClinGen `here
  <https://www.ncbi.nlm.nih.gov/clinvar/docs/clingen/>`_) 

- `OMIM <https://www.omim.org/>`_ lists known genetic disorders and associated genes.

- `SIFT <https://sift.bii.a-star.edu.sg/>`_ ("Sorting Intolerant from
  Tolerant"). More sophisticated than just "amino acid
  change", SIFT predicts whether an amino acid change would affect protein
  function based on sequence homology and physical properties of amino acids.

- PolyPhen (PolyPhen2-HDIV and PolyPhen2-HVAR are included in dbNSFP). dbNSFP
  includes SIFT, but only for known cases. Unknown missense mutations can be
  run through the command-line tool to calculate predictions.

- `COSMIC <https://cancer.sanger.ac.uk/cosmic>`_ is the Catalogue of Somatic
  Mutations in Cancer which is an expert-curated database of somatic mutations.
  The website also has mutation profiles of 1000+ cell lines and other useful
  info on somatic mutations in human cancer. You will need to create an account
  to download data.

- `GERP <http://mendel.stanford.edu/SidowLab/downloads/gerp/>`_ (Genomic
  Evolutionary Rate Profiling) assesses if a mutation was likely to be neutral
  or not (precomputed scores included in dbNSFP)

- `CAAD <https://cadd.gs.washington.edu/>`_ (Combined Annotation Dependent
  Depletion) scores the deleteriousness of single-nucleotide variants and small
  indels. The scoring uses a combination of sources. Precomputed scores are
  included in dbNSFP.

Visualization
-------------

The `gnomAD browser <https://gnomad.broadinstitute.org/>`_ is a great way to
visualize your variants.

The `UCSC Genome Browser <http://genome.ucsc.edu>`_ has tracks for many of the databases noted above.

`Krusche 2019 <https://www.nature.com/articles/s41587-019-0054-x>`_ in Figure
2 show the ways in which small indels can be called in different ways.


Additional notes
----------------

.. todo::

    This section could use some better organization

Filtering on minor allele frequency: A non-synonymous SNP that is rare in the
general population might be expected to be more important for the study.
Annotation tools typically add MAF (minor allele frequency) which is taken from
large studies with healthy individuals. But that "healthy individuals"
assumption is probably not 100% correct, due to incomplete penetrance or
variable clinical phenotype. So while we might initially think of something
like 1% as a threshold for "rare in the general population", we should set that
possibly to some different value. One place to start would be to set the
threshold to the carrier frequency for a related disease.

Some notes from from MacArthur 2018:

How many samples needed:

> Gene discovery for conditions with low locus heterogeneity and sufficiently
  high-penetrance mutations is occasionally possible by sequencing a single
  family; however, most gene-discovery applications will require
  substantially larger sample sizes: multiple unrelated families for rare
  monogenic conditions, and thousands to tens of thousands of patients and
  controls for complex disorders.

If you want to say that you did *not* find an expected variant:

> Investigators should begin by examining sequence variation in genes known to
  be associated with that phenotype, and assessing sequence coverage of the
  coding sequences and splice junctions for these genes before exploring the
  possibility of new candidate genes in the affected individuals.

A tale of caution regarding gene size:

> A study found 4 independent missense mutations in TTN in a cohort of 945
  families with a child affected by autism. TTN has the largest coding sequence
  of any gene, so you'd actually expect 1.96 mutations. Need to consider gene
  size, mutation rate, number of trios, distribution of exome coverage.


- `Eilbeck 2017 <https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5935497/>`_ gives
  a good overview of variant prioritization in the context of Mendelian
  disease.

- `MacArthur 2014 <https://www.nature.com/articles/nature13127>`_ gives clear
  guidelines assessing variant pathogenicity.

- The `ACGM standards <https://pubmed.ncbi.nlm.nih.gov/25741868/>`_ describes
  standard specific terminology like "pathogenic" or "likely benign" to
  describe variants in genes causing Mendelian disorders.


Other resources
---------------
- The "Extant-knowledge-based candidate prioritization" section of `Dashti 2018
  <https://www.future-science.com/doi/10.2144/000114492>`_ gives an example of
  what the final output of many database searches for a candidate gene.

- `Monarch Initiative <https://monarchinitiative.org/>`_ integrates many
  databases and is very useful for exploring existing knowledge.

- RegulomeDB: https://www.regulomedb.org
- GTEx: https://www.gtexportal.org
- GWAVA: https://www.sanger.ac.uk/sanger/StatGen_Gwava
