# django-openlike

Django template tag for easily implementing and extending OpenLike protocol.
See http://www.openlike.org/ for more info.

FEATURES:
- Templatetags for displaying OpenLike widget

USAGE:
- Basic: {% openlike %}
- Less basic: {% openlike "http://domain.com/" "Page title" %}

TODO:
- Documentation.
- Add support for extended sources.
- Configuration via Django admin

AUTHOR'S NOTE:
This app is most definitely overkill given the simplicy of OpenLike and the 
ease of pure JavaScript implementation. But it was a fun project to fully 
support a third-party service in Django.

