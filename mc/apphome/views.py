from django.shortcuts import render, redirect
from django.views.generic.base import View


class HomeHomeView(View):

    def get(self, request, *args, **kwargs):
        return redirect('/culto')