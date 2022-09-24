Making your Linux life easier
=============================

Intermediate command-line use
-----------------------------
Here are some tips that you might not have picked up from introductory
command-line tutorials.

Aliases
~~~~~~~

You can put any bash commands you’d like into an alias (see
http://tldp.org/LDP/abs/html/aliases.html for more).

For example, to log in to biowulf by typing ``b``, use:

.. code-block:: bash

   alias b="ssh -X $USER@biowulf.nih.gov"

To change to a frequently-visited directory,

.. code-block:: bash

   alias N="cd /data/NICDH-core0/"

Middle-click paste
~~~~~~~~~~~~~~~~~~

This is frequently overlooked in intro Linux tutorials, but in most
software on Linux when you highlight text it goes into a separate copy
buffer that can be pasted with middle-mouse-button. This means you
effectively have two buffers, the typical Ctrl-C/Ctrl-X/Ctrl-V as well
as the last-selected text buffer.

Ctrl-C in terminals
~~~~~~~~~~~~~~~~~~~

To interrupt a command, use Ctrl-C. To paste text from the Ctrl-C/X/V
buffer, use Ctrl-Shift-C or Ctrl-Shift-V (using most terminal
emulators).

dotfiles
~~~~~~~~

I’ve collected a lot of configurations over the years. You can grow your
own over time, or see https://github.com/daler/dotfiles to start with
“the works”.

Ctrl-R
~~~~~~

This lets you search through your history . . . but see ``fzf`` below in the
tools section for a fancier way.

Tools
-----

.. _meld:

meld
~~~~

`Meld <http://meldmerge.org/>`__ is an amazing tool for visually looking
at the differences between two files and merging them. I used meld for a
while but have now moved to using ``vim`` in diff mode, and the
`vim-fugitive <https://github.com/tpope/vim-fugitive>`__ vim plugin
helps especially with Git-related diffs and merges.


visidata
~~~~~~~~

We work a lot with TSV files and we work a lot on the command line.
Things like ``less`` and ``vim`` don’t format the data as nice as a
spreadsheet program like LibreOffice Calc or Gnumeric do.

`visidata <https://www.visidata.org/>`_ formats TSV files into a browsable,
sortable table with all sorts of convenient hotkeys. Makes it trivial to find
the most strongly differentially expressed genes from a TSV of DESeq2 results.

See a lightning demo `here <https://www.youtube.com/watch?v=N1CBDTgGtOU>`_.


.. _tmux:

Tmux
~~~~

-  Brief guide to tmux:
   https://medium.com/actualize-network/a-minimalist-guide-to-tmux-13675fb160fa
-  Lots more details: https://leanpub.com/the-tao-of-tmux/read
-  Recent HN post: https://news.ycombinator.com/item?id=17998649

Copy/paste between tmux, vim/neovim, and the system clipboard can get a
bit crazy. See
http://www.rushiagr.com/blog/2016/06/16/everything-you-need-to-know-about-tmux-copy-pasting-ubuntu
for the details.

fzf
~~~
`fzf <https://github.com/junegunn/fzf>`_ is a fuzzy-finder. The installation
script will make Ctrl-R, for searching through history, use ``fzf``.

Any content can be piped through fzf. For example, to search through ``conda``
environments here's a function to put in your ``.bashrc``. Then you can use
the ``sa`` command to search through your environments, and when you hit enter
that environment will be activated.

.. code-block:: bash

   # Select a conda env to activate
   sa() {
       local name=$(conda env list | grep -v "#" | fzf)
       local env=$(echo $name | awk '{print $1}');
       eval "source activate $env";
   }

autojump
~~~~~~~~
`autojump <https://github.com/wting/autojump>`_ remembers where you've changed
directories, and lets you jump right there with ``j``. Or hit ``j`` and
tab-complete to see alternatives.

This is a huge time saver when you're frequently visting highly-nested directories.

ripgrep
~~~~~~~

`ripgrep <https://github.com/BurntSushi/ripgrep>`_ is like grep combined but
much faster. Perfect for looking through source code since it plays nice with
git repos -- for example, it will ignore searching in files added to
``.gitignore`` or will avoid searching in huge files.
