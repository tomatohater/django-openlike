"""
Template tag for integrating OpenLike widget
Basic usage: 
    {% openlike %}
"""

from django import template
from django.conf import settings
from django.contrib.sites.models import Site


register = template.Library()

def openlike(url='', title=''):
    """
    Returns the HTML/js code necessary to display the OpenLike widget.
    """
    
    sources = getattr(settings, 'OPENLIKE_SOURCES', None)
    header = getattr(settings, 'OPENLIKE_HEADER', None)
    
    opts = []
    if sources:
        opts.append('s: [%s]' % ', '.join(['\'%s\'' % s for s in sources]))
    if header:
        opts.append('header: \'%s\'' % header)
    if url:
        opts.append('url: \'%s\'' % url)
    if title:
        opts.append('title: \'%s\'' % title)
        
    return """
    <script type="text/javascript" src="http://openlike.org/v1/openlike.js"></script>
    <script type="text/javascript">
        OPENLIKE.Widget({%(options)s})
    </script> 
    """ % dict(options=', '.join(opts))

register.simple_tag(openlike)
