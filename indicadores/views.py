from django.shortcuts import render
from django import views
from .forms import IndicadorForm
from django.http import FileResponse, Http404
from django.contrib import messages

class CreateView(views.View):
    def get(self, request):
        template_name = "indicadores/create.html"
        indicadorForm = IndicadorForm()
        context = {'form':indicadorForm}
        return render(request, template_name, context)

    def post(self, request):
        template_name = "indicadores/create.html"
        data = request.POST
        print(request.POST)
        form = IndicadorForm(data)
        print(form)
        context = {'form':form}

        if form.is_valid():
            form_save = form.save(commit=False)
            form_save.save()
            messages.add_message(request, messages.SUCCESS, "Indicador guardado")
        else:
            context = {'form':form}
            messages.add_message(request, messages.ERROR, "Hubo un error al guardar")

        return render(request, template_name, context)
