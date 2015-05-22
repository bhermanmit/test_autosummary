import sys, os

import sphinx.writers.latex
import sphinxcontrib.bibtex.nodes
from docutils import nodes


def visit_reference(self, node):

    # Hack to set references label tag
    text = node[0].astext()
    if text.startswith("[") and text.endswith("]"):
        if "refid" in node:
            node["refuri"] = "%references#kelly2013mc21"
            del node["refid"]

    # base code from sphinx bibtex
    for id in node.get('ids'):
        self.body += self.hypertarget(id, anchor=True)
    uri = node.get('refuri', '')
    if not uri and node.get('refid'):
        uri = '%' + self.curfilestack[-1] + '#' + node['refid']
    if self.in_title or not uri:
        self.context.append('')
    elif uri.startswith('mailto:') or uri.startswith('http:') or \
            uri.startswith('https:') or uri.startswith('ftp:'):
        self.body.append('\\href{%s}{' % self.encode_uri(uri))
        # if configured, put the URL after the link
        show_urls = self.builder.config.latex_show_urls
        if node.astext() != uri and show_urls and show_urls != 'no':
            if uri.startswith('mailto:'):
                uri = uri[7:]
            if show_urls == 'footnote' and not \
               (self.in_footnote or self.in_caption):
                # obviously, footnotes in footnotes are not going to work
                self.context.append(
                    r'}\footnote{%s}' % self.encode_uri(uri))
            else:  # all other true values (b/w compat)
                self.context.append('} (%s)' % self.encode_uri(uri))
        else:
            self.context.append('}')
    elif uri.startswith('#'):
        # references to labels in the same document
        id = self.curfilestack[-1] + ':' + uri[1:]
        self.body.append(self.hyperlink(id))
        self.body.append(r'\emph{')
        if self.builder.config.latex_show_pagerefs and not \
                self.in_production_list:
            self.context.append('}}} (%s)' % self.hyperpageref(id))
        else:
            self.context.append('}}}')
    elif uri.startswith('%'):
        # references to documents or labels inside documents
        hashindex = uri.find('#')
        if hashindex == -1:
            # reference to the document
            id = uri[1:] + '::doc'
        else:
            # reference to a label
            id = uri[1:].replace('#', ':')
        self.body.append(self.hyperlink(id))
        self.body.append(r'\emph{')
        if len(node) and hasattr(node[0], 'attributes') and \
           'std-term' in node[0].get('classes', []):
            # don't add a pageref for glossary terms
            self.context.append('}}}')
        else:
            if self.builder.config.latex_show_pagerefs and not \
               self.in_production_list:
                self.context.append('}}} (%s)' % self.hyperpageref(id))
            else:
                self.context.append('}}}')
    else:
        self.builder.warn('unusable reference target found: %s' % uri,
                          (self.curfilestack[-1], node.line))
        self.context.append('')


def visit_label(self, node):
    if isinstance(node.parent, nodes.citation):
        self.bibitems[-1][0] = node.astext()
        self.bibitems[-1][2] = "references"
        self.bibitems[-1][3] = node.parent['ids'][0]
    raise nodes.SkipNode

sphinx.writers.latex.LaTeXTranslator.visit_label = visit_label
sphinx.writers.latex.LaTeXTranslator.visit_reference = visit_reference

sys.path.insert(0, os.path.abspath('.'))

sys.path.append(os.path.abspath('ext'))

extensions = ['sphinx.ext.autosummary', 'changeorder', 'sphinxcontrib.bibtex']

# The suffix of source filenames.
source_suffix = '.rst'
autosummary_generate = True
