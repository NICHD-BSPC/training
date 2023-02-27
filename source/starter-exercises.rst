About
"""""

It can be very intimidating when starting to learn basic bioinformatics skills and tools - what is necessary for the upmost beginner? 
Here are some some exercises to help guide you.

Some basics assumptions I have made: 
1) When I write `something` this is a specific command you can type and it should work. 
2) `<something>.txt` is me using the '<' and ">' as fill-able spots. So you may then write `test.txt` or `help.txt`.

Command Line, Vim, and Bash Basics
''''''''''''''''''''''''''''''''''

Setting up your working directory is really important and keeping a clean, organized workspace will save you time in the future. Developing a standardized directory setup may help when you develop automated testing, need to check if certain directories (you know should) exist, and help remind you about where files are located days, weeks, months, maybe even years later. 

Let's start by creating a directory and filling it with some items - do all of this in your terminal. 

1) Create 5 directories labeled 'data', 'test', 'workflows', 'output', 'logs', 'extras'. Can you imagine what might go inside each of these directories?
2) From the main direcotry, `cd` into the 'data' directory and create 5 '.fasta' files using the `touch` command. Name each of these files something meaningful. Then open the files using `vim` and fill them int with some fasta data.
- keep in mind these are many types of ways to label files, but commonly we would NOT use spaces, rather 'camelCaseInstead' or 'just-dashes' or 'underscores_can_be_our_friends'
3) Now `cd` back into the main directory and from this directory add a bash (.sh) script called 'fastaParser.sh' in the workflows directory. 
- use `pwd` to figure out what directory's path you're in and use the tab key to autocomplete where you want to go. 
4) Now use `vim` to edit your fastaParser.sh and you'll realize you cannot immediately type. You'll actually have to use `i` to enter the 'Insert' mode. 
- Other little hints include: `a` to append, `:w` to write (and exit Insert mode), `:q` to exit vim itself.
5) Fill the fastaParser with a little bash script that will loop through the fasta files in your 'data' directory and pull out the header names' and output them to a file called 'headers.txt' in the 'output' directory. 
Can you think of anything else you could extract from the fasta files?
- `*` acts like a wildcard - can you imagine what `*.txt` might indicate? 
- In your script, `echo` acts like Python's print()
6) Run the bash script in the command line using `sbatch fastaParser.sh`. 
- Make sure you have some 'echos' in your script so that the terminal will output the header names. 
7) Use `cat` to concatenate all of your fasta files in one file called 'allFastas.fasta' which will be redirected using `>` into the outputs directory.
8) Now we have some output including a file containing header names and all of the fastas together. Check using `head` and `tail` on the command line - can you infer what they do? And what your files should look like?
9) Go into the output directory and now count the number of fasta entries we have using the `wc -l` command o the 'allFastas.fasta' file. Is this number correct and how did you figure that out?
10) Just for fun, copy all the headers.txt and allFastas.fasta and place them in the test directory using `cp <oldfilepath/file>.txt <newfilepath>.txt`
11) Go to the test directory and use `grep --file <headerfile>.txt allFastas.fasta` to search for the headers in the allFastas file. How can you pull out the sequence though?


GEO Submissions
'''''''''''''''
Gene Expression Omnibus (GEO) repository holds gene expression datasets. A good chunk of BSPC projects are Bulk RNA Sequence projects. Understanding the data and how it is organized is crucial. 

TRIP Dataset
''''''''''''

Biological Background: Thousands of Reports In Parallel (TRIP) is a protocol that allows the parallelization of inserations/deletions/mutations at various genomic regions using unique barcode identifiers of random (shotgunned) sequences of DNA. It's an interesting way to cast a wide net of genomc regions of interest that may relate to gene expression. Maybe we have lots of ctcf-binding sites and want to understand which portions of the DNA that have these sites are important. We can barcode various ctcf binding sites, add them into the genome, and then check for read counts of those DNA fragments. Because they're barcoded we can known which sample/experiment they came from. 

Sometimes we want to pull out crucial information from our datasets without disrupting the files too much or directing going into the filters. 

Example the file in the terminal using `vd final_TRIP_data_table.txt`. Take note of how this file is organized - what are exact of the columns representing?

Use your terminal commands to manipulate the final_TRIP_output.txt file to answer the following questions: 

1) How many entries are there in this dataset?
2) How many entries are positive stranded?
3) How many entries are positive stranded AND from Chr19? Hint: There are actually two columns that dictate the barcode is from Chr19.
4) How many unique barcodes are in this dataset?
5) Look at the sampletable (`vd sampletable.tsv`) and try and match the barcodes with the the sample
6) What biological meaning can be extract from this table? Write all your findings in a WORKLOG.rst. To add headers to your text add `"""` underneath the text

Exploring/Parsing a GTF File
''''''''''''''''''''''''''''

Parsing a Fasta/Fastq File
''''''''''''''''''''''''''

We use lots of fasta and fastq files as input files - but what are they?
Explore this fasta and fastq file to understand what a sample file may look like.

Think about and use your terminal commands to answer the following questions: 

1) What is the difference between the two files? 
2) When might one be more helpful than the other?
3) How many entries are in the fasta?
4) How many entries are in the fastq?
5) Create a fasta file from the first 23 entries of the fastq file

