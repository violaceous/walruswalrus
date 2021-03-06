import sys

from flask import Flask, render_template
from flask_flatpages import FlatPages
from flask_frozen import Freezer

DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'

app = Flask(__name__)
app.config.from_object(__name__)
pages = FlatPages(app)
freezer = Freezer(app)

@app.route('/')
def index():
    return render_template('index.html', pages=pages)
    
@app.route('/posts/')
def posts():
    return render_template('posts.html', pages=pages)
    
@app.route('/contact/')
def contact():
    return render_template('contact.html')    

@app.route('/<path:path>/')
def page(path):
    page = pages.get_or_404(path)
    tags = page.meta.get('tags', [])
    taggedPages = []
    for tag in tags:
        toExtend = [p for p in pages if tag in p.meta.get('tags', [])]
        taggedPages.extend(toExtend)
    taggedPages = list(set(taggedPages))
    return render_template('page.html', page=page, pages=pages, tags=tags, taggedPages=taggedPages)
    
@app.route('/tag/<string:tag>/')
def tag(tag):
    tagged = [p for p in pages if tag in p.meta.get('tags', [])]
    return render_template('tag.html', pages=tagged, tag=tag)

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        app.run(port=8000)
