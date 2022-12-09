.. _galaxy:

Galaxy
======

.. image::path/galaxyLogo.jpeg

`Galaxy <https://usegalaxy.org/>`_ is an open-source web application built for scientific analyses featuring a public server located within teh cloud, accessible open-source software packages, custom Galaxy tools (Galaxy ToolShed), and a user-friendly drop-and-drop interface. The platform is easy to learn, requiring no programming experience, and used to build reproducible bioinformatics workflows. Galaxy's community also serves as one of the few active forums for bioinformaticians to collaborate, with over 150 active members monthly. 

Multiple tools are available to the user, including popular ones such as FastQC (quality control), Bowtie2 (aligner), featureCounts (read counter). Galaxy's built-in drag-and-drop workflow also serves as a transparent way to quickly communicate analyses to other researchers and collaborators. 

As of current, Galaxy is best for simple genomic analyses, as there are some drawbacks to the platform. 

.. image::path/galaxyBulkRNASeqWorkflow

Fig1: The Galaxy UI. The lefthand sidebar shows the tools available to the user. The center features a workflow for Bulk RNASeq. The righthand sidebar shows additional information. 


Galaxy is a great introductory tool for bioinformaticians and the Galaxy community is only getting stronger - with over 124,000 registered users since its inception in 2007 and over 2000 Galaxy Help members total. 

Getting Started with Galaxy 
----
Utilize the Galaxy Training pages to understand what workflows are possible for Galaxy: `Click Here <https://training.galaxyproject.org/training-material/>`_ 

Bulk RNA Seq Analysis in Galaxy tutorial: `Click Here <https://training.galaxyproject.org/training-material/topics/transcriptomics/tutorials/ref-based/tutorial.html#data-upload>`_

Drawbacks 
----
1. **Some tools have additional options that are not always available to the user, causing first-time users might be confused on what tool exactly to use.** Ex. Operate on Genomic Intervals:Intersect and BED:bedtools Intersect intervals are the same tool yet bedtools offers more options for the user to set. 

2. **Many of Galaxy's tools only provide links to the original code's documentation.** This is unhelpful as there is a skill required in understanding the docs as well as the fact that Galaxy UI has purposefully changed the options names/descriptions.

3. **Some of Galaxy's tools do not have properly formatted documentation at the bottom.** This is the other extreme of Drawback #3. An example tool of this is the UpSet diagram tool. The figure in the tool is way too big. 

4. **Searching for tools can be difficult and overwhelming.** The naming of the tools splits between Galaxy-programmed tools and Galaxy-adapted tools created by other pre-existing packages. Ex. In the "Get Data" tab, there are two options to get data from NCBI SRA that look very similar: "Faster Download and Extract Reads in FASTQ" and "Download and Extract Reads in FASTA/Q". How is someone supposed to know which tool to use and remember one over the other? What is the difference between the two? What is "faster"? 

A great example of a well documented tool is "Download and Extract reads in FASTA/Q". It is a simple tool with understandable documentation. It also has flags for what Galaxy is internally doing and how Galaxy will output these files to the user. 

A not-so-great example is the Filter FASTA. While simple, the tool's options are weirdly worded and confusing. The option: Match IDs by has two options: (1) Default: ID is expected at the beginning: >ID (2) Custom regex pattern. "Regex" refers to regular expression. What is a regular expression to a non-programmer? Where is regex defined? What can that entail? Maybe some documentation at the bottom could help. There is no documentation or examples below. The option "Criteria for filtering on sequences" includes: (1) No filtering (2) Sequence Length and (3) Regular expression pattern that the sequence should match. First of all, why do we have a "No filtering" option of the Filter Fasta tool, is filtering not the sole purpose of this tool? Secondly, Regex is now fully defined as regular expression, and an unlinked URL is supplied. 

Papers
----
`The Galaxy platform for accessible, reproducible and collaborative biomedical analyses: 2018 update (Afghan, et al. 2018) <https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6030816/>`_ 


.. todo::

    Add info and links for galaxy!
