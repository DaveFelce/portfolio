from django.conf.urls import url
from django.views.decorators.cache import cache_page

from .views import Home

app_name = 'home'

urlpatterns = [
    url(r'^$', cache_page(60 * 15)(Home.as_view()), name='index'),
]
