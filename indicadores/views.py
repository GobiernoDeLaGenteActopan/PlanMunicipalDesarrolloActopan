from django.shortcuts import render
from django import views


class CreateView(views.View):
    def get(self, request):
        template_name = "indicadores/create.html"
        context = {}
        return render(request, template_name, context)
