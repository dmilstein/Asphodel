from os.path import join, dirname, abspath
import shutil

from django.http import HttpResponse

from django.shortcuts import render_to_response

def index(request):
    return render_to_response('asphodel/index.html', {})

# Awful hack, I'm tired
static_dir = abspath(join(dirname(__file__), '..', 'static'))

def universe_image(request):
    """
    Serving dynamically even though I have a static image lying around,
    because we may want to generate from graphviz on the fly soonish.
    """
    response = HttpResponse(mimetype="image/png")
    f = open(join(static_dir, 'universe.png'), 'r')
    shutil.copyfileobj(f, response)
    f.close()
    return response
