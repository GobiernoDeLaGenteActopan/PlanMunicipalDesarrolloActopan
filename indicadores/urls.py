from django.urls import path
from .views import CreateView, ListView, LandingView, DetailView

app_name="indicadores"
urlpatterns = [
    path('', LandingView.as_view(), name="landing"),
    path('list', ListView.as_view(), name="list"),
    path('create', CreateView.as_view(), name="create"),
    path('detail/<int:pk>', DetailView.as_view(), name="detail")
]
