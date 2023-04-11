from django.urls import path
from .views import HomeView, ProductView, about
urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('product-details/<slug:slug>/',
         ProductView.as_view(), name="product-details"),
    path('about/', about, name="about")
]
