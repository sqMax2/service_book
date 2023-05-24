from django.shortcuts import render
from rest_framework import viewsets, permissions
from django.views.generic import TemplateView


class AppView(TemplateView):
    template_name = 'default.html'

    # def get_context_data(self, **kwargs):
    #     context = super(AppView, self).get_context_data(**kwargs)
    #     context['custom_context'] = 'some custom context'
    #     return context


# REST viewsets
