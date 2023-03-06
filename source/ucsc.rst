UCSC Genome Browser
===================

Track hubs are directories of genomic data that can be viewed on the `UCSC Genome Browser <https://genome.ucsc.edu/index.html>`_. Researchers to access, view, and build their own and others' "tracks" using this tool. 

Nature Publication's Scitable resource has an  `ebook on UCSC Genome Browser <https://www.nature.com/scitable/ebooks/cntNm-16569863/contents/>`_.

Manually Setting up a TrackHub
##############################

If you do not have much experience building tracks, have few tracks you need to build, can use one of UCSC's pre-built genomes, and do not need much customization - manually setting up a trackhub is a good starting point. Here is how to establish a trackhub using NIH's Biowulf Server (internet-accessible). 

Needs: 

1. BAM File - need to be in binary index format (*.bai*)
2. Text files - for specifying properties (configuration files)
3. twoBit file with sequence (for the assembly hub)

Steps: 


.. todo::

    Topics needed for UCSC:
    
    - track hubs
    - udcTimeout=1
    - hosting files on datashare
    - custom tracks and tracklines
    - useful built-in tracks
