from django.urls import path
from .views import CreateView

app_name="indicadores"
urlpatterns = [
    path('create', CreateView.as_view(), name="create"),
]
