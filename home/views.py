from django.views import View
from django.shortcuts import render, get_object_or_404
from django.views.decorators.cache import cache_page
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.conf import settings
from .models import Copy


class Home(View):
    """Home page class-based view

    Args:
        View (:obj:Django View base class, required)

    """

    def get(self, request):
        """get http method: very simple home page
        """

        copy = get_object_or_404(Copy, pk=1)
        return render(request, 'home/index.html', {'copy': copy})
