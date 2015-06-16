"""
WSGI config for {{ project_name }} project.

This module contains the WSGI application used by Django's development server
and any production WSGI deployments. It should expose a module-level variable
named ``application``. Django's ``runserver`` and ``runfcgi`` commands discover
this application via the ``WSGI_APPLICATION`` setting.

Usually you will have the standard Django WSGI application here, but it also
might make sense to replace the whole Django WSGI application with a custom one
that later delegates to the Django one. For example, you could introduce WSGI
middleware here, or combine a Django application with an application of another
framework.


NOTE: this uses the dj-static app by Kenneth Reitz to serve static assets
from the wsgi process (safely, not using the django dev server). Couple this
with a front end CDN like Amazon's Cloudfront or the CDNSumo heroku addon.

dj-static is the heroku officially suggested way to host your static files as
of 2013-08-17.
https://devcenter.heroku.com/articles/django-assets

"""
import os
from django.core.wsgi import get_wsgi_application
from dj_static import Cling

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings.dev")

# wrap wsgi with dj-static cling middleware
application = Cling(get_wsgi_application())
