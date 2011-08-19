from django.conf.urls.defaults import patterns, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('asphodel.views',
    # Examples:
    # url(r'^$', 'app.views.home', name='home'),
    url(r'^$', 'index'),
    url(r'^universe_image.png$', 'universe_image'),
)
