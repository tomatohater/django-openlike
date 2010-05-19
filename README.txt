# django-openlike

Django template tag for easily implementing and extending OpenLike protocol.
See http://www.openlike.org/ for more info.


FEATURES:

- Export django.contrib.comments to DISQUS
- Dump comments from DISQUS into a local JSON file
- Templatetags for displaying OpenLike widget


TODO:

- Documentation.
- Assumes links are "http". Add support for "https".
- Add support for extended sources.


AUTHOR'S NOTE:

This app is most definitely overkill given the simplicy of OpenLike and the 
ease of pure JavaScript implementation. But it was a fun project to fully 
support a third-party service in Django.

