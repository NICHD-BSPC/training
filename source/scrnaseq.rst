scRNA-seq
=========

Single-cell RNA-seq (scRNA-seq) gives inforamtion on the transcripts in individual cells. 

Recently, many people have been asking about R specifically so that they can
learn how to work with scRNA-seq on their own.



There are several major packages
for scRNA-seq: `Seurat <https://satijalab.org/seurat/>`_, a `suite of
Bioconductor packages <https://bioconductor.org/books/release/OSCA/>`_, and
`scanpy <https://scanpy.readthedocs.io/en/stable/>`_. Seurat and Bioconductor are
in R, scanpy is Python. They are broadly the same, but are in somewhat of an
arms race so some new features or analyses may not be immediately available in
all of them.

The book `Orchestrating Single-Cell Analysis with Bioconductor
<https://bioconductor.org/books/release/OSCA/>`_ is a fantastic, comprehensive
resource that even goes through worked examples of published data. This uses
the suite of tools in Bioconductor. Highly recommended.

`Seurat <https://satijalab.org/seurat/>`_ is another popular package for
scRNA-seq, and has a series of vignettes on the home page. There have been
recent improvments to the normalization (scTransform v1 and v2), and these use
somewhat different steps. The different vignettes therefore differ in the
steps, and it can be a bit confusing. The `PBMC3k tutorial
<https://satijalab.org/seurat/articles/pbmc3k_tutorial.html>`_ is the classic
starting point, so working through this one will at least give you the context
to work through other vignettes.

.. note::

    If you jump right in to the Seurat tutorials without knowing R, you won't know
    which commands are standard R and which are Seurat-specific. And if your data
    do not exactly match their example data, it will be unclear how to modify the
    code to suit your data if you don't know R.

    You should be fine with the "Level 1" set of R skills above to start using
    Seurat effectively. See the "Beginner" section above for learning these
    skills.

- Introduction to 10X scRNA-seq: https://www.bioinformatics.babraham.ac.uk/training/10XRNASeq/10X_Introduction.pdf
- PCA vs t-SNE vs UMAP: https://www.bioinformatics.babraham.ac.uk/training/10XRNASeq/Dimension%20Reduction.pdf

- Harvard Bioinformatics Core training on scRNA-seq: https://hbctraining.github.io/scRNA-seq_online/schedule/links-to-lessons.html
