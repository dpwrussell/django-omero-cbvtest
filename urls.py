import django
if django.VERSION < (1, 6):
    from django.conf.urls.defaults import *
else:
    from django.conf.urls import *

from . import views

urlpatterns = patterns('django.views.generic.simple',

    url( r'^$', views.CBVTestView.as_view(), name='cbvtest' )
)
