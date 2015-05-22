def setup(app):

    print "HELLO FROM NEW EXTENSION"

    app.connect('env-before-read-docs', env_before_read_docs_handler)

    return {'version': '0.1'}   # identifies the version of our extension

def env_before_read_docs_handler(app, env, docnames):

    print "IN DOC HANDLER"
#    temp = docnames[0]
#    docnames[0] = docnames[-1]
#    docnames[-1] = temp
    print docnames
