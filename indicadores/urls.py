from django.urls import path

urlpatterns = [
    path('create', CreateView.as_view())
]
