What is `$PATH`?
================




Fundemantal
-----------


Technically, the ``$PATH`` is an environment variable used in the Unix system. Windows and DOS use ``%PATH%`` instead of ``$PATH``. The ``$PATH`` literally stores colon (``:``)-separated paths. Check your ``$PATH`` variable with the command ``echo $PATH`` in your terminal. 

.. code-block:: bash

    $ echo $PATH
    /home/mira/.cargo/bin:/home/mira/.cargo/bin:/home/mira/miniconda3/bin:/home/mira/miniconda3/condabin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/home/mira/opt/bin:/home/mira/miniconda3/bin:/home/mira/miniconda3/bin:/home/mira/.fzf/bin


My ``$PATH`` has 16 colon-separated paths.

What do they mean? Let's go back to the command ``echo`` which you ran seconds ago. How did it work? You might be able to get a hint by running ``which echo`` shown here:


.. code-block:: bash

    $ which echo
    /usr/bin/echo


I learned that the ``echo`` locates in the directory ``/usr/bin`` from the info given by ``which``. That's the eighth one out of sixteen paths printed by ``echo $PATH``.

What if I search for a command that's not present or is invisible on my computer? Searching for a random command ``cool`` gives no output as shown below:


.. code-block:: bash

    $ which cool
    $


That's because my computer failed to find its location unlike the case of ``echo``. It means my computer has no idea what to do for the command.

Given that, there are two requirements if you want to run commands from a new tool in your bioinformatics analysis:

1) installing the tool
2) updating your ``$PATH`` with a new path storing new commands


For example, documentations for `Bowtie2 <https://bowtie-bio.sourceforge.net/bowtie2/manual.shtml#building-from-source>`_ and `HISAT2 <http://daehwankimlab.github.io/hisat2/manual/>`_ remind users to ensure that the directory path for ``Bowtie2`` or ``HISAT2`` is added to ``$PATH`` so every command from the new tool is visible and executable on users' computer. 


How do I add a path to the variable ``$PATH``? As the ``$PATH`` consists of multiple colon-separated paths, it can be simply concatenated with a ``:`` before- or afterhand.



.. code-block:: bash

    # New path added to the last
    PATH=$PATH:~/path/to/new/tool

    # New path added to the front
    PATH=~/path/to/new/tool:$PATH



Afterwards, the updated ``$PATH`` has to be exported (``export PATH=$PATH:~path/to/new/tool``) in the terminal so your current shell picks the change.


## Taking advantage of ``$PATH``


Then, is it possible to make the commad ``cool`` executable? Yes, it is! First, I define what my computer will do if the command is given.


.. code-block:: bash

    #!/bin/bash

    echo "I'm cool!"



It will print "I'm cool!". And I ensure the file is executable by running ``chmod 770 cool`` (this will give read/write/execute permission of the file ``cool`` to me and my group members). The next step is to export the updated ``$PATH`` with the new directory having ``cool``.



.. code-block:: bash

    # Assume that `cool` is present in `~/Downloads/path_variable`
    $ export PATH=~/Downloads/path_variable:$PATH



I see that my ``$PATH`` has been updated (see the first path ``/home/mira/Downloads/path_variable``). 


.. code-block:: bash

    $ echo $PATH
    /home/mira/Downloads/path_variable:/home/mira/.cargo/bin:/home/mira/.cargo/bin:/home/mira/miniconda3/bin:/home/mira/miniconda3/condabin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/home/mira/opt/bin:/home/mira/miniconda3/bin:/home/mira/miniconda3/bin:/home/mira/.fzf/bin



Can my computer find ``cool``?


.. code-block:: bash

    $ which cool
    /home/mira/Downloads/path_variable/cool


It tells that the command is found in ``/home/mira/Downloads/path_variable/cool``. What will happen if I run ``cool``?



.. code-block:: bash 

    $ cool
    I'm cool!


It prints what's been defined in the file ``cool``. You can create new commands as many as you want!


Essential question
------------------


Here, a question arises. What if I have an identical command from multiple directories in the ``$PATH``? The answer is, it's determined by the order set in the ``$PATH``. Revisiting the output of my original ``echo $PATH`` below:



.. code-block:: bash

    $ echo $PATH
    /home/mira/.cargo/bin:/home/mira/.cargo/bin:/home/mira/miniconda3/bin:/home/mira/miniconda3/condabin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/home/mira/opt/bin:/home/mira/miniconda3/bin:/home/mira/miniconda3/bin:/home/mira/.fzf/bin



commands are executed preferentially from the front directories. It indicates that commands in the ``/home/mira/.cargo/bin`` will always win no matter what other directories contain the same command. Accordingly, you need to adjust the order of paths in your ``$PATH`` if you want a preferential execution of your analysis tool.


In practice, users who use `Conda <https://docs.conda.io/en/latest/>`_ to manage tools don't have to manually update ``$PATH``. While my ``$PATH`` has the following paths set under my default conda env:



.. code-block:: bash

    (base) $ echo $PATH
    /home/mira/.cargo/bin:/home/mira/.cargo/bin:/home/mira/miniconda3/bin:/home/mira/miniconda3/condabin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/home/mira/opt/bin:/home/mira/miniconda3/bin:/home/mira/miniconda3/bin:/home/mira/.fzf/bin



I get my ``$PATH`` updated with ``/home/mira/miniconda3/envs/snakemake_mapping/bin`` being added to the front part when having my conda env ``snakemake_mapping`` (``/home/mira/miniconda3/envs/snakemake_mapping``) being activated as shown below:



.. code-block:: bash

    (snakemake_mapping) $ echo $PATH
    /home/mira/miniconda3/envs/snakemake_mapping/bin:/home/mira/.cargo/bin:/home/mira/.cargo/bin:/home/mira/miniconda3/bin:/home/mira/miniconda3/condabin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/home/mira/opt/bin:/home/mira/miniconda3/bin:/home/mira/miniconda3/bin:/home/mira/.fzf/bin



It clarifies that any tools/commands which I've installed in the conda env will be executed preferentially and that the ``Conda`` manages not only installation of my tools but my ``$PATH``.


