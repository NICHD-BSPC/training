UCSC Genome Browser
===================

Track hubs are directories of genomic data that can be viewed on the `UCSC
Genome Browser <https://genome.ucsc.edu/index.html>`_. Researchers to access,
view, and build their own and others' "tracks" using this tool. 

Nature Publication's Scitable resource has an  `ebook on UCSC Genome Browser
<https://www.nature.com/scitable/ebooks/cntNm-16569863/contents/>`_.

Manually Setting up a TrackHub
##############################

If you do not have much experience building tracks, have few tracks you need to
build, can use one of UCSC's pre-built genomes, and do not need much
customization - manually setting up a trackhub is a good starting point. Here
is how to establish a trackhub using NIH's Biowulf Server
(internet-accessible). 

Needs: 

1. BAM File - need to be in binary index format (*.bai*)
2. Text files - for specifying properties (configuration files)
3. twoBit file with sequence (for the assembly hub)

Steps:
1. Go to the 
   `UCSC genomc browser <https://genome.ucsc.edu/cgi-bin/hgHubConnect](https://genome.ucsc.edu/cgi-bin/hgHubConnect>`_
2. Format data - `datatypes
   supported <https://genome.ucsc.edu/goldenPath/help/hgTrackHubHelp.html#Intro:~:text=lists%20for%20lung-,Step,-1.%20Format%20the>`_
    1. BAM: contain alignments of generally short DNA reads to a reference
       sequence (complete genome). Binary version of SAM (sequence
       alignment map) format files. 
    2. Bam.bai : index for a bam file (stored separately, created in CL
       using: samtools index <bamfile.bam>
3. Create track hub directory
    1. Needs to be in internet accessible-location - for biowulf this is in
       the datashare directory
    2. The directory will contain hub.txt and genomes.txt files to define
       properties of of the track hub and the subdirectory for each of the
       genome assemblies covered by the hub track data. 

4. Config your files (hub.txt, genomes.txt, and trackDb.txt) and place your data
    1. Create hub.txt file - specifying what hub info you should include;
       should look like this: 

.. code-block:: python 
    :linenos: 

    1 hub TestTrackHub #this will be your public hub name
    2 shortLabel TrackHub Training in BSPC
    3 longLabel First TrackHub Training with Human BigWig Files
    4 genomesFile genomes.txt #genome configuration file
    5 email <email>

2. Create the genomes.txt file - to specify which genome you want to browse
        1. genome: must be a valid UCSC database name You can have multiple
           apparently (genome hg38\n genome hg37 maybe works?)
        2. trackDb: relative path of trackDb file located in subdirectory
           of the hub directory (specify a complete URL)
            1. You need to create a directory called hg38 and there needs
               to be a trackDb.txt existing inside
            2. inside hg38 there needs to be the bigwig files

.. code-block:: python 
    :linenos: 

    genomes.txt

    1 genome hg38 
    2 trackDb hg38/trackDb.txt``

3. Create trackDb.txt - will call the bigwig files 

.. code-block:: python
    :linenos:
    
    V1 track pinealGlandNight1 
    2 bigDataUrl
    Pineal_Gland_Night-1.cutadapt.bam.pos.bigwig 3 shortLabel
    pinealGlandNight1 
    4 longLabel pinealGlandNight1 
    5 type bigWig 
    6 
    7 track pinealGlandNight2 
    8 bigDataUrl
    Pineal_Gland_Night-2.cutadapt.bam.pos.bigwig 
    9 shortLabel
    pinealGlandNight2 
    10 longLabel pinealGlandNight2 
    11 type bigWig

Note: you need the 2bit from fasta to get the assembly and the annotations.bigBed

5. Connect URL to UCSC trackhub


.. todo::

    Topics needed for UCSC:
    
    - track hubs
    - udcTimeout=1
    - hosting files on datashare
    - custom tracks and tracklines
    - useful built-in tracks
