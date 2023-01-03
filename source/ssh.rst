.. _ssh:

SSH
===

Quickstart
----------

Do this on *each* machine you will be connecting from:

- Create a new keypair::

    ssh-keygen -t ed25519 -C "your_email@example.com"

- Copy the public key to each host you want to connect to:

  .. code-block:: bash

      # for each host you want to connect to
      ssh-copy-id user@hostname

- Log in to your GitHub account, GitLab account, or any other services that use
  SSH keys. Paste the contents of ``~/.ssh/id_ed25519.pub`` into the settings
  of your account profile. 

- Once per bash session, run this to load your key into memory for the duration
  of that session:

  .. code-block:: bash

      # See below for more info on macOS
      eval `ssh-agent`; ssh-add


More details below....

Overview
--------

SSH (secure shell) is the primary way to connect from one machine to another
from a terminal. Technically ssh is a *protocol* that specifies how a client and
a server talk to each other. Mac and Linux have ssh clients installed by
default, it's available with the ``ssh`` command from the terminal. On Windows,
`PuTTY <https://www.putty.org/>`_ is a commonly used one (if a bit basic);
`MobaXTerm <https://mobaxterm.mobatek.net/>`_ has many more options.

For example, using ssh from a laptop you could:

- log in to a high-performance cluster like `Biowulf <https://hpc.nih.gov>`_ to
  write code and start jobs running
- set up a web server in the cloud
- log in to your desktop at work to copy files over to your laptop

SSH is also used anytime something needs to be transferred securely. For
example, when you are cloning, pushing, and pulling commits from GitHub, this is
typically done over SSH.

Basic usage
-----------

From the command line, ssh as ``user`` to the host machine ``host`` with::

    ssh user@host

Where ``host`` is an IP address or a hostname like ``biowulf.nih.gov``.

When you hit enter, you will be asked for the password for that user on that
host. You may get a message saying something about a fingerprint and if you
really want to connect. This is normal for the first time you are connecting and
you can choose "yes" (this is discussed more below).

You will then be on the remote machine, which should also be indicated by
a change in the prompt (e.g. ``user@remote.host.name``). **Anything you type
here is going to the remote machine.** If you want commands to go to the local
machine, you must open a new shell (or terminal window), or exit ssh.

To exit ssh, use the ``exit`` command. It will close the connection and put you
back on your local machine (again, pay attention to the prompt for clues).

Setting up SSH keys
-------------------

SSH has the concept of a *keypair* which can take the place of a password. This
can be more secure than a password, and can also be useful for automation when
it is inconvenient (or impossible) to manually enter a password. You can read
more about why keys are preferred over passwords in `this
security.stackexchange answer
<https://security.stackexchange.com/questions/69407/why-is-using-an-ssh-key-more-secure-than-using-passwords>`_.

A keypair consists of a **public key** and a **private key**. One way to think
about them is that the public key is like a lock. That lock can be put on
anything, and it's OK for the lock to be seen by others. Only the corresponding
private key can open that lock, so the private key needs to be kept safe. That
private key is typically also protected with a *passphrase* -- a password
separate from any user accounts.

Another way to think about keypairs, and how they can be secure even if one is
public, is with the "color mixing" analogy, visually represented in `this
section of a description of the Diffie-Hellman key exchange
<https://www.comparitech.com/blog/information-security/diffie-hellman-key-exchange/#How_does_the_Diffie-Hellman_key_exchange_work>`_.

Another reason keys are useful is that you can use the *ssh-agent* to store, in
memory and for the duration of a terminal session, the decrypted key. Then you
can ssh, use git push/pull, rsync, and anything else using the ssh protocol,
without entering a password. This will be described below; first how to set up
your keys.

The command is:

.. code-block:: bash

    # replace the email with your own
    ssh-keygen -t ed25519 -C "your_email@example.com"

This will create two files: ``~/.ssh/id_ed25519`` (the *private* key) and
``~/.ssh/id_ed25519.pub`` (the *public* key). The ``ed25519`` specifies the
algorithm. The default algorithm is ``RSA`` which is OK if you use longer than
2048 bits, but it is generally recommended to use ``ed25519`` because it is
more secure and more performant.

For more details, `see this documentation page from GitHub
<https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent>`_.

Tell other hosts about your key
-------------------------------

In order to use your keypair with another system, you need to tell that
other system about it. But you only tell the other system about the *public*
key, and you use your private key to access.

Copy your public key automatically to another host like this:

.. code-block:: bash

    ssh-copy-id user@hostname

You will be prompted for your *password for that user on the remote host*. The
command will copy your public key(s) over to the remote host (technically, into
the ``~/.ssh/authorized_keys`` file on that host).

So we are using the username/password to authenticate to the remote host, and
using that authentication to allow transferring our public key over there
because the remote host is convinced it's really us.

The next time you log in to that host from the same machine, it will recognize
you have set up keys and will then ask you for your *ssh key passphrase*.

Using SSH keys for accessing GitHub, etc
----------------------------------------

Some sites, notably GitHub and GitLab, use SSH keys to authenticate. That's
because you're typically interfacing with those sites via command-line ``git``,
and they need some secure way of authenticating. User/password could be one
way, but SSH keys are considered more secure.

In general, you log in to the site as normal. Go to your profile settings, and
there will be a section on SSH keys where you can add your public key. For
example, here are the `GitHub docs
<https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account>`_
for adding your SSH key to your GitHub account.

Similarly, here are the `GitLab docs
<https://docs.gitlab.com/ee/user/ssh.html>`_ for adding your SSH key to your
GitLab account.


Start the agent for automatic login
-----------------------------------

It's pretty common to log in to multiple machines, pop on and off of servers,
make multiple pushes and pulls over git, and run rsync transfers over ssh. To
avoid needing to enter password or passphrase every single time, you can just
enter it once per Bash session (or once per restart on Mac). This will load it
into memory so ssh can provide it automatically.

This is the most basic:

.. code-block:: bash

    # most basic usage
    eval "$(ssh-agent)"; ssh-add

You may find it convenient to put it into a function in your ``.bashrc``, say,
called ``s``, so that you just need to remember to run ``s`` once per session:

.. code-block:: bash

    # function to go in, e.g., ~/.bashrc
    function s () {
        eval "$(ssh-agent)"
        ssh-add
    }

On Mac, it can be more convenient to allow the keychain to handle this, however
this depends on the version of macOS you're using. See `this apple.stackexchange
answer <https://apple.stackexchange.com/a/250572>`_ for details:

.. code-block:: bash

    # On macOS versions <12.0
    function s () {
        eval "$(ssh-agent)"
        ssh-add -K
    }

    # On macOS versions >=12.0
    function s () {
        eval "$(ssh-agent)"
        ssh-add --apple-use-keychain
    }

Here's a function you can use in all your dotfiles on all hosts -- it sets arguments correctly depending on Linux/Mac and macOS version:

.. code-block:: bash

    # Start the ssh-agent and add keys to the agent.
    # Detects if on Mac; if so detects the macOS version and provides the
    # appropriate args to add keys to the keychain
    SSH_ENV=$HOME/.ssh/environment
    function start_agent {
        echo "Initializing new SSH agent..."
        eval "$(ssh-agent)"

        additional_arg=""
        if [[ $OSTYPE == darwin* ]]; then
            if [[ $(sw_vers -productVersion | cut -f1 -d '.') -lt 12 ]]; then
                additional_arg="-K"
            else
                additional_arg="--apple-use-keychain"
            fi
        fi
        ssh-add "$additional_arg"
    }

On Mac, you *also* need to make this change in your ssh config to allow ssh to
use the keychain for any hosts:

.. code-block::

    # this goes in ~/.ssh/config
    Host *
      UseKeychain yes
      AddKeysToAgent yes
      IdentityFile ~/.ssh/id_ed25519

Next steps
----------

These are all optional, but some next logical steps might be:

- Modify your ssh config file, ``~/.ssh/config``, to have aliases for different
  hosts
- Make aliases to login to commonly-used hosts
- SSH tunneling is a way of attaching other hosts to ports on your local
  machine. See the `Biowulf SSH tunneling <https://hpc.nih.gov/docs/tunneling/>`_ docs for more on this.

References
----------
- `ssh.com <https://www.ssh.com/academy/ssh>`_, which has lots of good
  information on SSH (despite trying to sell products)
- `apple.stackexchange answer
  <https://apple.stackexchange.com/questions/48502/how-can-i-permanently-add-my-ssh-private-key-to-keychain-so-it-is-automatically>`_
  about adding SSH private key to the keychain on Mac
- `GitHub docs
  <https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent>`_
  on generating a keypair
- ``man`` pages for ``ssh``, ``ssh-keygen``, ``ssh-copy-id``, ``ssh-agent``, ``ssh add``
