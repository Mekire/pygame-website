from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from views import landingPage

urlpatterns = [
    url(r'^$', landingPage, name='index'),
    # app pages
    url(r'^forums/', include('forums.urls')),
    # admin pages
    url(r'^admin/', include(admin.site.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'Pygame Website'

