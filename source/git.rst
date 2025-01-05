.. _git:

Git
===

"*Your closest collaborator is you six months ago, but you don't reply to emails*" `

Writing code and documentation involves lots of iterative revisions. Just like
keeping a lab notebook, you'll need to keep track of these changes. And if
something goes wrong, or you don't like the direction things are going, it
would be nice to rewind history to get your code back to a working state.

``git`` does all of this. It's sort of like "track changes" in Word, but for
entire directories rather than a single file. And with the full power of
a command-line interface.

``git`` is "version control software" -- a tool that allows you to track the
history of files in a repository that lives within a working directory. This
repository can stay private on disk or can optionally be shared with
collaborators either publicly or privately, using web services like GitHub,
GitLab, or Bitbucket.


Should you learn git?
---------------------

If you plan on doing substantial programming or analysis of any sort, you
should learn git. Just like if you are going to be doing any substantial
experiments, you should keep a lab notebook.

Git can be hard to learn! The concepts are unfamiliar and the commands feel
like arcane incantations. But the payoff -- being able to step through time,
rewinding the history of your work and keeping checkpoints -- is well worth it.

In BSPC, git is a critical part of our workflow. If you are aiming to work
directly in BSPC, it will be important to know git.

If you just started R or Python or Bash, you should probably focus on that
first. If you decide to stick with it, git would be a good next thing to learn.

.. note::

    A note of warning, especially important to genomics where we work with large data sets:

    **DO NOT COMMIT DATA TO GIT!**

    Only small files (code, documentation) should be committed to a git
    repository. Even if you mistakenly add data and then immediately remove it,
    *it stays in the history*.

    To fix it, see `these instructions
    <https://help.github.com/en/github/authenticating-to-github/removing-sensitive-data-from-a-repository>`_.
    It's a pain. All the more reason to not commit data!

Learning git
------------

Here are some resources to learn the above commands. As with all self-directed
training, it is worth looking at all of these resources at least briefly to
decide what fits your brain the best.

-  `A quick introduction to version control with Git and GitHub
   <http://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1004668>`__
   This guide, written by scientists, for scientists, walks you through a very
   practical example. It includes files to download to follow along and
   explains a lot of the concepts you’ll see while using git. It has a concise
   glossary of terms you'll see

-  `Chapter 2 of Plain Person’s Guide
   <https://kieranhealy.org/files/papers/plain-person-text.pdf>`__ does not
   give direct commands, but does a nice job of framing the motivation for why
   learning and using git is a good thing.

-  `Git Handbook <https://guides.github.com/introduction/git-handbook/>`_
   gives an overview and commands, and links out to YouTube videos on
   particular topics. It's written by GitHub, so it's understandably biased
   towards working with GitHub.

- `Bitbucket's git tutorials <https://www.atlassian.com/git/tutorials>`_ has
  multiple learning tracks. Bitbucket is a GitHub competitor, so some of their
  content is skewed towards using their product. But the rest of the content is
  very well written.

  - `Beginner <https://www.atlassian.com/git/tutorials/setting-up-a-repository>`_ (init, clone, config, add, commit, .gitignore))
  - `Collaborating <https://www.atlassian.com/git/tutorials/syncing>`_ (remote, fetch, push, pull, using branches, merge)
  - `Advanced tips <https://www.atlassian.com/git/tutorials/advanced-overview>`_

-  `Git and GitHub
   chapter <https://seankross.com/the-unix-workbench/git-and-github.html>`_
   of the Unix Workbench. This is similar to the PLOS Comp Bio paper linked
   above, but also has some exercises which may be helpful to test your
   learning.

-  `Learn Git Branching <https://learngitbranching.js.org/>`_, an
   interactive tutorial that turns learning about branching into a game. What
   makes it really useful is how visual it is.

-  A `cheatsheet <https://training.github.com/downloads/github-git-cheat-sheet.pdf>`_
   of commonly-used commands, useful if you need a refresher.

- An `essay on the inner workings of git
  <https://codewords.recurse.com/issues/two/git-from-the-inside-out>`_. Starts
  off like the others, but quickly gets quite advanced. This is great if you
  want to know how it all actually works or need to dig around to do some fancy
  stuff.

- An examination of a `good git commit
  <https://fatbusinessman.com/2019/my-favourite-git-commit>`_. This is not
  about the mechanics of git, but rather about best-practices of practical use.

- When working with pull requests from contributors to a repository you manage,
  `this blog post
  <https://tighten.com/blog/adding-commits-to-a-pull-request/>`_ walks you
  through making your own commits that get added to that PR.

- Eventually, you'll be contributing to open source software. That may involve
  rebasing a fork of an upstream repo. `How to fork
  <https://joaquimrocha.com/2024/09/22/how-to-fork/>`__ is about this, but also
  is a great explanation of rebasing.

Do you know git?
----------------

Here are some git commands split into different levels of git knowledge. This is just one
way of thinking about it, but if you're wondering where you stand along your
training then this can give you a rough idea.

Beginner
~~~~~~~~

- ``git add``
- ``git status``
- ``git commit``
- ``git log``
- ``git checkout``
- ``git push origin master``
- ``git pull origin master``
- ``git checkout -b newbranch``
- ``git checkout -- <filename>``

Intermediate
~~~~~~~~~~~~
- ``git rm``
- ``git mv``
- ``git merge newbranch``
- ``git checkout HEAD~~``
- ``git add -p``
- ``git tag``
- resolving merge conflicts
- ``git cola``
- ``git blame``

Advanced
~~~~~~~~

- ``git rebase``
- ``git cherry-pick``
- ``git-bisect``
- resolving 3-way merges
- using the `fugitive <https://github.com/tpope/vim-fugitive>`_ vim plugin
