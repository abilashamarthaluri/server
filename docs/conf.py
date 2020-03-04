# Copyright (c) 2018-2020, NVIDIA CORPORATION. All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
#  * Neither the name of NVIDIA CORPORATION nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS ``AS IS'' AND ANY
# EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
# PURPOSE ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR
# CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
# PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY
# OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('..'))
from builtins import str
import os
import re
import sphinx_rtd_theme
import subprocess
import textwrap

# -- Project information -----------------------------------------------------

project = u'NVIDIA Triton Inference Server'
copyright = u'2018, NVIDIA Corporation'
author = u'NVIDIA Corporation'

version_long = u'0.0.0'
with open("../VERSION") as f:
    version_long = f.readline()

version_short = re.match('^[\d]+\.[\d]+', version_long).group(0)

git_sha = os.getenv("GIT_SHA")

if not git_sha:
    try:
        git_sha = subprocess.check_output(["git", "log", "--pretty=format:'%h'", "-n1"]).decode('ascii').replace("'","").strip()
    except:
        git_sha = u'0000000'

git_sha = git_sha[:7] if len(git_sha) > 7 else git_sha

version = str(version_long + u"-" + git_sha)
# The full version, including alpha/beta/rc tags
release = str(version_long)

# hack: version is used for html creation, so put the version picker
# link here as well:
version = version + """<br/>
Version select: <select onChange="window.location.href = this.value" onFocus="this.selectedIndex = -1">
    <option value="https://docs.nvidia.com/deeplearning/sdk/tensorrt-inference-server-guide/docs/index.html">Current release</option>
    <option value="https://docs.nvidia.com/deeplearning/sdk/tensorrt-inference-server-master-branch-guide/docs/index.html">master (unstable)</option>
    <option value="https://docs.nvidia.com/deeplearning/sdk/inference-server-archived/index.html">Older releases</option>
</select>"""

# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.mathjax',
    'sphinx.ext.napoleon',
    'sphinx.ext.ifconfig',
    'sphinx.ext.extlinks',
    'nbsphinx',
    'breathe',
    'exhale'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path .
exclude_patterns = [u'build', 'Thumbs.db', '.DS_Store', '**.ipynb_checkpoints']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# Setup the breathe extension
breathe_projects = {
    "BreatheTritonServer": "./doxyoutput/xml"
}
breathe_default_project = "BreatheTritonServer"

# Setup the exhale extension
exhale_args = {
    # These arguments are required
    "containmentFolder":     "./cpp_api",
    "rootFileName":          "cpp_api_root.rst",
    "rootFileTitle":         "C++ API",
    "doxygenStripFromPath":  "..",
    # Suggested optional arguments
    "createTreeView":        True,
    # TIP: if using the sphinx-bootstrap-theme, you need
    # "treeViewIsBootstrap": True,
    "exhaleExecutesDoxygen": True,
    "exhaleDoxygenStdin": textwrap.dedent('''
        JAVADOC_AUTOBRIEF = YES
    INPUT = ../src/core/trtserver.h ../src/clients/c++/library/request.h ../src/clients/c++/library/request_grpc.h ../src/clients/c++/library/request_http.h ../src/backends/custom/custom.h ../src/custom/sdk/custom_instance.h
    ''')
}

# Tell sphinx what the primary language being documented is.
#primary_domain = 'cpp'

# Tell sphinx what the pygments highlight language should be.
highlight_language = 'text'


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    'canonical_url': 'https://docs.nvidia.com/deeplearning/sdk/tensorrt-inference-server-guide/docs/index.html',
    'collapse_navigation': False,
    'display_version': True,
    'logo_only': False,
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
#html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'NVIDIATritonServerdoc'


# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'NVIDIATritonServer.tex', u'NVIDIA Triton Inference Server Documentation',
     u'NVIDIA Corporation', 'manual'),
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'nvidiatritonserver', u'NVIDIA Triton Inference Server Documentation',
     [author], 1)
]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'NVIDIATritonServer', u'NVIDIA Triton Inference Server Documentation',
     author, 'NVIDIATritonServer', 'One line description of project.',
     'Miscellaneous'),
]


# -- Extension configuration -------------------------------------------------
extlinks = {'issue': ('https://github.com/NVIDIA/triton-inference-server/issues/%s',
                      'issue '),
            'fileref': ('https://github.com/NVIDIA/triton-inference-server/tree/' +
                        (git_sha if git_sha != u'0000000' else "master") + '/%s', ''),}

def setup(app):
    # If envvar is set then the file is expected to contain a script
    # that is added to every documentation page
    visitor_script = os.getenv("VISITS_COUNTING_SCRIPT")
    if visitor_script:
        app.add_js_file(visitor_script)
