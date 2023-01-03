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
for this command to read more on what those arguments do, but this effectively recursively copies everything from the ``from/`` directory, preserving group, owner, permissions, and times, and shows progress while it's running.

The trickiest thing about rsync is that **it is sensitive to trailing slashes
(/) on the source directory.** In contrast, a trailing slash on the destination
has no effect.

To demonstrate, imagine we have a directory, ``from``, with one file in it::

    from/
    └── a.txt

Then we run these commands:

.. code-block:: bash

    rsync -r from to

    # No trailing slash on "from" puts the whole directory *inside* the
    # destination
    # to/
    # └── from
    #    └── a.txt

(then remove ``to`` so we can run the next test:)

.. code-block:: bash

    rsync -r from/ to
    #            ^
    #            |
    #            Trailing slash
    #
    # Copies the *contents* of source inside the destination
    to/
    └── a.txt

Working in shared directories
-----------------------------
Be careful using ``-a`` when transferring to shared directories, because
preserving the owner and group can mess up permissions. It's generally useful
to keep everything else, especially times since that's the primary information
rsync uses to decide if a file is up-to-date. So when transferring to a shared directory, use:

.. code-block:: bash

    rsync --recursive --times --permissions --progress source/ dest/

    # shorter version
    rsync -rtp --progress source/ dest/


Other useful options
--------------------

Sometimes you want to copy the files that symlinks point to, rather than the
symlink. In such a case, use the ``-L`` argument to follow symlinks.

If you have large uncompressed files or a slow connection, use ``-z`` to
compress over the wire. Rsync will automatically decompress on the remote. This
sends less data over the network at the cost of CPU to compress/decompress. It
uses zlib compression, so if you have lots of data in gzip or tar.gz files,
using ``-z`` will try to compress already-compressed data, wasting CPU. 

Use ``--partial`` (or ``-P``, which implies both ``--partial`` and
``--progress``) which will keep partially-transferred files on the remote. This
is especially good for large files, so rsync can pick up where it left off on
the same file.

More recent versions of rsync support the ``--info=progress2`` argument, which
reports the transfer speeds for the *entire transfer* rather than for each
file. This can give you a better idea of the real transfer speed.

Use ``--exclude`` to avoid transferring matching patterns. Useful to avoid
copying conda environments.
