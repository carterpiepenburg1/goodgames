from django.shortcuts import render, redirect
from django.views import View

class feed(View):
    def get(self, request):
        return render(request, "feed.html", {})