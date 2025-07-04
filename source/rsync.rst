.. _rsync:

Rsync
=====

Rsync is the best way to transfer files between hosts or even within the same
system. It has features like:

- If a connection is broken, it will pick up where it left off.

- It will synchronize a directory, only copying over files that are newer. If
  configured to do so, it can also clean up files on the remote that have been
  deleted locally

- Can compress data over the wire, resulting in faster transfers

- Verifies if the file was correctly transferred

- More performant, flexible, and configurable than alternatives like scp or cp

Rsync is installed by default on most Mac and Linux machines. It works over SSH
so it's secure, and has more features than scp and even cp. Use it any time
you're transferring between local and remote, and use it any time you're
copying large directories locally.

Typical usage is:

.. code-block:: bash

    rsync -av --progress from/ user@hostname:/to/

See `explainshell <https://explainshell.com/explain?cmd=rsync+-av+--progress>`_
for this command to read more on what those arguments do, but this effectively
recursively copies everything from the ``from/`` directory, preserving group,
owner, permissions, and times, and shows progress while it's running.

One tricky thing about rsync is that **it is sensitive to trailing slashes
(/) on the source directory.** A trailing slash on the destination, however,
has no effect.

To demonstrate, imagine we have a directory, ``source``, with one file in it::

    source/
    └── a.txt

Then we run these commands to transfer to the ``dest`` directory:

.. code-block:: bash

    rsync -r source dest


When we check the contents of ``dest``, we see that no trailing slash on
``source`` put the whole directory *inside* the destination::

    dest/
    └── source/
       └── a.txt

If we instead add a trailing slash in the command:


.. code-block:: bash

    rsync -r source/ dest
    #              ^
    #              |
    #              Trailing slash


Then the *contents* of ``source`` get copied inside ``dest``::

    dest/
    └── a.txt



Working in shared directories
-----------------------------
When transferring to a shared directory, or any directory that might have
special permissions (like `Biowulf's datashare directories
<https://hpc.nih.gov/nih/datashare.html>`) then be careful using the ``-a``
argument. This is because that argument tries to preserve the owner and group
can mess up permissions in the shared directory.

It's generally useful to use all the other arguments implied by ``-a``, so when
transferring to a shared directory, use:

.. code-block:: bash

    rsync --recursive --times --permissions --progress source/ dest/

    # shorter version
    rsync -rtp --progress source/ dest/


Other useful options
--------------------

- Sometimes you want to copy the files that symlinks point to, rather than the
  symlink. In such a case, use the ``-L`` argument to follow symlinks.

- If you have large uncompressed files or a slow connection, use ``-z`` to
  compress over the wire. Rsync will automatically decompress on the remote.
  This sends less data over the network at the cost of CPU to
  compress/decompress. It uses zlib compression, so if you have lots of data in
  gzip or tar.gz files, using ``-z`` will try to compress already-compressed
  data, wasting CPU. 

- Use ``--partial`` (or ``-P``, which implies both ``--partial`` and
  ``--progress``) which will keep partially-transferred files on the remote.
  This is especially good for large files, so rsync can pick up where it left
  off on the same file.

- More recent versions of rsync support the ``--info=progress2`` argument,
  which reports the transfer speeds for the *entire transfer* rather than for
  each file. This can give you a better idea of the real transfer speed.

- Use ``--exclude`` to avoid transferring matching patterns. Useful to avoid
  copying conda environments, for example.

You can read a bit more about the rationale and algorithm behind rsync in
`Tridgell & Mackerras (1996)
<https://www.andrew.cmu.edu/course/15-749/READINGS/required/cas/tridgell96.pdf>`__. 

There are many more options for rsync, so as usual, read the manual (e.g.,
``man rsync``)!

