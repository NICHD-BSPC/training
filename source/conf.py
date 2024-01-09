# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'BSPC Training'
copyright = '2020, Ryan Dale'
author = 'Ryan Dale'

# Added to avoid error "contents.rst not found"
master_doc = 'index'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    #'sphinxcontrib.asciinema',
    'sphinx.ext.todo',
]

todo_include_todos = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# CUSTOMIZATION FOR THIS REPO: the sphinx-better-theme has been added to this
# repo, so we use it here.  The following lines have been added to customize
# sphinx-better-theme.  Try changing html_theme to 'alabaster' or other
# built-in themes.
#
html_theme = 'better'
html_theme_path = ['_templates/sphinx-better-theme']

# Files in the following directories are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_title = ''
html_theme_options = {
  # show sidebar on the right instead of on the left
  'rightsidebar': False,

  # inline CSS to insert into the page if you're too lazy to make a
  # separate file
  'inlinecss': '',

  # CSS files to include after all other CSS files
  # (refer to by relative path from conf.py directory, or link to a
  # remote file)
  'cssfiles': ['_static/style.css'],  # default is empty list

  # show a big text header with the value of html_title
  'showheader': True,

  # show the breadcrumbs and index|next|previous links at the top of the page
  'showrelbartop': True,

  # same for bottom of the page
  'showrelbarbottom': True,

  # show the self-serving link in the footer
  'linktotheme': False,

  # width of the sidebar. page width is determined by a CSS rule.
  # I prefer to define things in rem because it scales with the
  # global font size rather than pixels or the local font size.
  'sidebarwidth': '15rem',

  # color of all body text
  'textcolor': '#333333',

  # color of all headings (<h1> tags); defaults to the value of
  # textcolor, which is why it's defined here at all.
  'headtextcolor': '',

  'footertextcolor': '#888888',

}

html_short_title = "Home"
html_sidebars = {
    '**': ['localtoc.html', 'sourcelink.html', 'searchbox.html'],
}

# Running `make linkcheck` will ensure links are working. However, some sites
# are resistant to scraping, so need some tweaks here:
linkcheck_request_headers = {
    # Add a user agent to everything
    "*": {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    }
}

# Avoids downloading the entire page to check anchors.
linkcheck_anchors = False

# Completely ignore these regexes
linkcheck_ignore = [
    # Appears to be using CloudFlare, not worth the effor to spoof here
    r'https://gatk.broadinstitute.org',

    # Also scrape-resistant
    r'https://twitter.com',

    # SSL/TLS errors
    r'https://www.sempf.net',

    # Scraping returns 500, but website seems fine. Possibly a timeout issue
    # since the site seems slow.
    r'http://blogs.nature.com/methagora',
]
