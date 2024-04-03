from django.conf.urls import include
from django.urls import re_path
from rdrf.views.handler_views import handler404, handler500, handler_application_error, handler_exceptions


urlpatterns = [
    # Any custom URLs go here before we include the TRRF urls
    re_path(r'', include('rdrf.urls')),
]

handler404 = handler404
handler500 = handler500
handler_application_error = handler_application_error
handler_exceptions = handler_exceptions

