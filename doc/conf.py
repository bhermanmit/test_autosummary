import sys, os

sys.path.insert(0, os.path.abspath('.'))

sys.path.append(os.path.abspath('ext'))

extensions = ['sphinx.ext.autosummary', 'changeorder']

# The suffix of source filenames.
source_suffix = '.rst'
autosummary_generate = True
