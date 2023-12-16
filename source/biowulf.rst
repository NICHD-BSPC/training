Biowulf help topics
===================

In BSPC, our general workflow when connecting to Biowulf is this:

1. Open a terminal
2. SSH to Helix
3. Create a tmux session or attach to an existing one

When doing graphics-heavy work, like plotting in R or Python, then instead we will:

1. Open NoMachine
2. Connect to Biowulf
3. Open a terminal from within NoMachine session on Biowulf.


Tips
----

Here are some tips for making it as seamless as possible to connect.

More convenient SSH
-------------------
Typically when you SSH to Biowulf you will get asked for your password. This
can be made a bit more convenient as follows.

First, create a new key pair and copy it to biowulf using `these
instructions <https://www.ssh.com/ssh/copy-id>`_.

**You should use a passphrase** otherwise anyone with access to your
machine will be able to also access every other server you have copied
your SSH key to.

Then, see `this SO answer <https://stackoverflow.com/a/18915067>`_
for a function to add to your ``.bashrc`` that will add the key to your
session. This is sort of a security compromise that asks for your key once per
bash session rather than every time it’s used.

Now when you connect you are just substituting your pass phrase for your
password, but this makes other things possible (see next section).

Add SSH key to Mac keychain
~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you're on a Mac, adding the following lines to your ``~/.ssh/config`` file
will allow SSH to use the Mac keychain. This means that once you log in to your
Mac like normal, you don't need to enter your SSH pass phrase at all. That
means `ssh user@biowulf.nih.gov` will immediately and automatically connect.

Note that this example uses RSA keys; modify as needed if using ed25519 or
ecdsa algorithms.

.. code-block::

    Host *
        AddKeysToAgent yes
        UseKeychain yes
        IdentityFile ~/.ssh/id_rsa.pub

Then run:

.. code-block:: bash

    ssh-add -K ~/.ssh/id_rsa

to add it to the keychain.

More info `here <https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent#adding-your-ssh-key-to-the-ssh-agent>`_.

You can always add an alias to your `.bashrc`, like:

.. code-block:: bash

    alias b="ssh $USER@biowulf.nih.gov"

So that to connect Biowulf, you open a terminal, type ``b``, then Enter, and you're in.



NoMachine and RStudio
~~~~~~~~~~~~~~~~~~~~~

When doing visualization-heavy work, especially in RMarkdown in RStudio, we use NoMachine.

In BSPC, we prefer to manage our own conda environments so we can install
exactly the versions we need (and use development versions of packages if
needed) without affecting the global installation and allowing us to use
different sets of packages for different projects.

If you have conda configured on Biowulf and your ``.bashrc`` adds the
conda-installed version of Python to your path, NoMachine will fail. This is
because it needs the system-wide installed Python version.

To avoid this, you can wrap the block of code that ``conda init bash`` adds to
your ``.bashrc`` in an if-clause:

.. code-block:: bash

    if [ -z "$NX_CLIENT" ]; then

        # conda activate stuff

    fi

Since the ``NX_CLIENT`` environment variable is only set when using NoMachine,
this will only activate conda if that environment variable is not set.


.. note::

    When creating a conda environment, you should NOT add RStudio to that
    environment. RStudio is simply a convenient interface; it is not required
    for reproducibility. RStudio can use the R version in the conda env as
    described below.

To run RStudio in NoMachine:

1. Connect to Biowulf with NoMachine
2. Open a terminal within NoMachine
3. Get an interactive node with scratch space (e.g., ``sinteractive --mem=8g --gres=lscratch:8``)
4. Load the RStudio module (note the lowercase "s"): ``module load Rstudio``.
   You may see a message like "Remember to load an R module before starting
   Rstudio", but don't do that if you're using a conda env.
5. Activate your conda env e.g., ``conda activate ./env``)
6. Use the wrapper provided in the module to load RStudio, using the
   (undocumented) flag ``--conda``. This sets things up properly to use the
   conda-installed version of R in RStudio.

RStudio Server on Biowulf
~~~~~~~~~~~~~~~~~~~~~~~~~

We can use `RStudio Server <https://posit.co/products/open-source/rstudio-server/>`_
instead of NoMachin for R programming on Biowulf. This requires setting up an SSH tunnel 
between your local computer and Biowulf using your SSH keys.
Ensure that the SSH keys are set up for Biowulf (see 
`More convenient SSH <biowulf.html#more-convenient-ssh>`_).

Once you have the SSH keys ready, add the following proxy configuration to the ``~/.ssh/config``
on your mac.

.. code-block:: bash

   Host cn*
   User username
   ProxyCommand /usr/bin/ssh -o ForwardAgent=yes username@biowulf.nih.gov nc -w 120ms %h %p

Configure your proxy by following steps 6 and 7 in the `Windows: Run VS Code on a compute node
<https://hpc.nih.gov/apps/vscode.html#win>`_ if you're using Windows.

To run RStudio Server on Biowulf:

* Log into Biowulf using your NIH account.
* Allocate an `interactive node <https://hpc.nih.gov/docs/userguide.html#int>`_ with the ``-T/--tunnel``
  (for tunneling) and ``--gres=lscratch:N`` (to allocate temporary space for RStudio Server) parameters.

  .. code-block:: bash

    user@biowulf:~$ sinteractive --tunnel
    salloc.exe: Pending job allocation 26710013
    salloc.exe: job 26710013 queued and waiting for resources
    salloc.exe: job 26710013 has been allocated resources
    salloc.exe: Granted job allocation 26710013
    salloc.exe: Waiting for resource configuration
    salloc.exe: Nodes cn3094 are ready for job

    Created 1 generic SSH tunnel(s) from this compute node to 
    biowulf for your use at port numbers defined 
    in the $PORTn ($PORT1, ...) environment variables.


    Please create a SSH tunnel from your workstation to these ports on biowulf.
    On Linux/MacOS, open a terminal and run:

        ssh  -L 45000:localhost:45000 biowulf.nih.gov

    For Windows instructions, see https://hpc.nih.gov/docs/tunneling

* Load RStudio Server as `guided by NIH HPC <https://hpc.nih.gov/apps/rstudio-server.html>`_.

  .. code-block:: bash

    [user@cn1640 ~]$ module load rstudio-server
    [+] Loading gcc  9.2.0  ...
    [-] Unloading gcc  9.2.0  ...
    [+] Loading gcc  9.2.0  ...
    [+] Loading openmpi 4.0.5  for GCC 9.2.0
    [+] Loading ImageMagick  7.0.8  on cn4280
    [+] Loading HDF5  1.10.4
    [-] Unloading gcc  9.2.0  ...
    [+] Loading gcc  9.2.0  ...
    [+] Loading NetCDF 4.7.4_gcc9.2.0
    [+] Loading pandoc  2.17.1.1  on cn4280
    [+] Loading pcre2 10.21  ...
    [+] Loading R 4.2.2
    [+] Loading rstudio-server  2023.03.0-386


* Ensure that R is available by loading `Biowulf's module <https://hpc.nih.gov/apps/R.html#int>`_ 
  or by activating your conda environment where ``r-base`` is installed.
* Start RStudio Server on your interactive node.

  .. code-block:: bash

    [user@cn1640 dir]$ rstudio-server

    Please ensure you have set up the SSH port forwarding as described in the sinteractive instructions.

    Please connect to http://localhost:39689/auth-sign-in?user=test2&password=nRmzfPWh_X8Z-03hbDjPz3bm
    Use your username 'user' and the pasword 'nRmzfPWh_X8Z-03hbDjPz3bm' to login

* Create an SSH tunnel connecting your local computer to Biowulf. If you're using Mac or Linux,
  copy and paste the following code into a new terminal on your local machine.

  .. code-block:: bash

    (local_computer)$ alias tun='$(ssh biowulf.nih.gov /usr/local/slurm/bin/reconnect_tunnels)'
    (local_computer)$ tun
    ...
    (biowulf)$

  Follow the `Tunneling from Windows <https://hpc.nih.gov/docs/tunneling/#windows>`_ instruction
  if you're using Windows. Do not close the tunneling terminal while using RStudio Server.

* Copy and paste the host address 
  (e.g. ``http://localhost:39689/auth-sign-in?user=test2&password=nRmzfPWh_X8Z-03hbDjPz3bm``)
  provided by ``rstudio-server`` into your browser.

.. note::

   RStudio Server may raise an error with R in versions newer than those in Biowulf's module.
   If you encounter this issue, downgrade your R version in conda environment or load it from 
   Biowulf.

tmux
~~~~

We typically SSH into Helix and attach to a persistent tmux session (or create
a new tmux session, roughly once a month). From there we ssh over to Biowulf.
Helix has lots more resources available and tends to have less lag or slowdown
issues than the Biowulf head node.

Helix reboots the first Monday of each month, so make sure you're done with
your tmux session by then!

See :ref:`tmux` for more info.

Limitations of mounted drives
-----------------------------

While it’s convenient to map biowulf drives locally, there are
limitations. It would be best to treat the mapped drive as
**read-only**.


Executable permissions:

-  **Executables cannot be called on the mounted drive**, even if they
   have the executable bit set. This means that running conda
   environments stored in the analysis directory will not work. A
   workaround is either to remove the “noperm,file_mode=0660” options
   from above, or use the ``--conda-prefix`` argument to Snakemake when
   running locally (e.g.,
   ``--conda-prefix $HOME/snakemake-conda-envs``).

**Symlinks are not handled correctly.** Even with the ``mkfsymlinks``
option,

-  Symlinks created on Biowulf do not appear locally
-  Symlinks created locally do not appear on Biowulf
-  If you open something that looks like a regular file locally but that
   is actually symlink on biowulf and then save it, **the symlink is
   destroyed and replaced with a regular file**.


squeue
------

The default output of ``squeue -u`` doesn’t have a lot of info. Also,
it’s a pain (for me) to type. Digging through the man page for squeue, I
found you can control which columns are shown. Here’s what I’ve aliased
to ``q`` in my biowulf ``.bashrc`` file:

.. code-block:: bash

   alias q='squeue -u $USER -o "%9A %18j %5C %5m %.9L %.9M %9N %8T %o"'

Now the easier-to-type ``q`` gives output with info on the node resources, how
much time is left, and a longer “name” field and “command” field to better
track which job is which when you have a ton of jobs going.




fastq-dump
----------

By default, fastq-dump uses local caching in your home directory
(``~/ncbi`` I believe) which, if you’re not careful can fill up all your
quota. If you use ``module load sratoolkit`` on biowulf, it sets a
particular environment variable to override this behavior. You can see
what it’s doing with ``module show sratookit``.

To mimic this behavior when using conda environment containing
``sratools``, you can acheive the same thing by putting this in your
``.bashrc``:

.. code:: bash

   export VDB_CONFIG=/usr/local/apps/ncbi/config/biowulf.kfg

When writing swarmfiles or otherwise using fastq-dump to get lots of
files, it’s important to write things to be robust against accidental
failures where you may get a partially-downloaded fastq. It’s difficult
to know when that happens, so one way around it is to download to a temp
location and then move the resulting temp file only if the previous
command exited cleanly. The move operation is instantaneous so it
doesn’t add any time.

Also, the fastq-dump implementation of gzip is slow, so for single-end
reads you might want to consider writing out to stdout and piping to
gzip for single-end.

For example, to download a single-end FASTQ, a swarmfile entry might be:

.. code-block:: bash

   export SRR=SRR00001; \
   export TEMP_PATH=/temp/directory; \
   export FINAL_PATH=/directory/for/final/data; \
   cd $TEMP_PATH; \
     module load sratoolkit; \
     fastq-dump $SRR --gzip \
     && mv $TEMP_PATH/$SRR_1.fastq.gz $FINAL_PATH

**Note:** ``TEMP_PATH`` and ``FINAL_PATH`` should be absolute paths.

For paired-end, use ``--split-files`` and move both ends over the final
directory.

.. code-block:: bash

   export SRR=SRR00001; \
   export TEMP_PATH=/temp/directory; \
   export FINAL_PATH=/directory/for/final/data; \
   cd $TEMP_PATH; \
     module load sratoolkit; \
     fastq-dump $SRR --split-files --gzip \
     && mv $TEMP_PATH/$SRR_{1,2}.fastq.gz $FINAL_PATH


Avoid ``swarm`` clutter
-----------------------

When running ``swarm``, use ``--noout --noerror`` to avoid getting all the ``swarm_*`` output files.

Consider ``/dev/shm`` for high I/O
----------------------------------

Copying data to ``/dev/shm`` to put it in the memory temp file system. This
should be super fast I/O access. The size is limited to the ``--mem`` for the
job and to 50% of node memory.

There's some more info on this on the Biowulf help page for ``kraken``,
https://hpc.nih.gov/apps/kraken.html.

.. note::

   ``/dev/shm`` is not cleaned up after a job like ``lscratch`` is. Be sure to
   clean up when you're done!
