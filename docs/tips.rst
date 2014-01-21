Other tips
==========

1. **Syntax highlighting:** Python-Markdown has a pre-shipped codehilite
   extension which works perfectly, so add something like::

       WIKI_MARKDOWN_KWARGS = {'extensions': ['footnotes', 'attr_list', 'headerid', 'extra', 'codehilite', ]}

   to your settings. Currently, wiki-base shippes with a stylesheet
   that already has the syntax highlighting CSS rules built-in. Oh, and
   you need to ensure ``pip install pygments`` because Pygments is what
   the codehilite extension is using!
