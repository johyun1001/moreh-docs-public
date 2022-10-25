# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'docs'
copyright = '2022, johyun'
author = 'johyun'
release = '0.5'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [    'sphinx_rtd_theme','myst_parser', 'sphinx.ext.autodoc', 'sphinx.ext.doctest']

templates_path = ['_templates']
exclude_patterns = []

root_doc = 'index.md'
language = 'ko'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

#html_theme = 'alabaster'

#html_theme = "sphinx_rtd_theme"
html_theme = "sphinx_material"
html_static_path = ['_static']

html_theme_options = {
    'analytics_id': 'UA-XXXXXXX-1',  #  Provided by Google in your dashboard
    'analytics_anonymize_ip': False,
    'logo_only': False,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    'vcs_pageview_mode': '',
    'style_nav_header_background': 'orange',
    # Toc options
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False
}