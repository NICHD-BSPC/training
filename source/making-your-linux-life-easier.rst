.. _making-your-linux-life-easier:

Making your Linux life easier
=============================

Here are some tips that you might not have picked up from introductory
command-line tutorials.

Aliases
-------

You can put any bash commands you’d like into an alias (see
http://tldp.org/LDP/abs/html/aliases.html for more).

For example, to log in to biowulf by typing ``b``, use:

.. code-block:: bash

   alias b="ssh -X $USER@biowulf.nih.gov"

To change to a frequently-visited directory,

.. code-block:: bash

   alias N="cd /data/project/"

Middle-click paste
------------------

This is frequently overlooked in intro Linux tutorials, but in most
software on Linux when you highlight text it goes into a separate copy
buffer that can be pasted with middle-mouse-button. This means you
effectively have two buffers, the typical Ctrl-C/Ctrl-X/Ctrl-V as well
as the last-selected text buffer.

This will work if you're on a Linux graphical user interface, for example if
you're using `NoMachine to log in to Biowulf
<https://hpc.nih.gov/docs/nx.html>`_.



Ctrl-C in terminals
-------------------

To interrupt a command, use Ctrl-C.

To paste text from the Ctrl-C/X/V buffer, use Ctrl-Shift-C or Ctrl-Shift-V
(using most terminal emulators).

If you're using tmux, it gets a little trickier -- see the :ref:`tmux` section
for more.

Opening files on Mac
--------------------
Use ``open`` on Mac to open the file in the appropriate program, e.g., ``open
document.docx`` to open in Word.

Opening HTML files
------------------

When a URL shows up somewhere in the terminal, depending on your terminal you
can easily open it on your local machine:

- macOS Terminal app: Commad-double-click
- iTerm2 app: Command-click
- Alacritty: click

dotfiles
--------

"Dotfiles" collectively refers to the various configuration files used by bash
(``.bashrc``, ``.bash_profile``), git (``.gitconfig``), tmux ``.tmux.conf``),
vim (``~/.vimrc`` or ``.config/nvim/init.vim``), and others. To prevent them
from showing up in a standard ``ls`` call, they start with a leading ``.``,
hence dotfiles.

You can grow your own over time, or see https://github.com/daler/dotfiles to
start with “the works”.

Ctrl-R
------

Ctrl-R lets you search through your history. It works in the R interpreter,
too. See ``fzf`` below in the tools section for a fancier way for searching
through history.

Tools
-----

Here are some useful tools to install. If you're using `my dotfiles
<https://github.com/daler/dotfiles>`_, you can use the ``setup.sh`` script to
easily install them.

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

tmux
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

Any content can be piped through fzf -- see the home page for all sorts of ways
it can be used.

ripgrep
~~~~~~~

`ripgrep <https://github.com/BurntSushi/ripgrep>`_ is like grep combined but
much faster. Perfect for looking through source code since it plays nice with
git repos -- for example, it will ignore searching in files added to
``.gitignore`` or will avoid searching in huge files.
