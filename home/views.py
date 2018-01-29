from django.views import View
from django.shortcuts import render

class Home(View):
    """Home page class-based view

    Args:
        View (:obj:Django View base class, required)

    """

    def get(self, request):
        """get http method: very simple home page
        """

        return render(request, 'home/index.html')
