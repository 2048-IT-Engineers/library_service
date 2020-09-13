"""Core views.py"""
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import render
from django.views import View


class IndexPageView(View):
    """IndexPageView class"""

    def __init__(self, **kwargs: dict):
        self.template_name = 'core/index.html'
        self.context = {'page_name': 'Main page'}
        super().__init__(**kwargs)

    def get(self, request: HttpRequest) -> render:
        """
        Processing get request

        :param request: HttpRequest
        :return: render
        """

        return render(request, self.template_name, self.context)
