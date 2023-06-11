from django.urls import path
from .views import HomePageView,AboutUsView,ActivityPageView

app_name = 'inua'

urlpatterns = [
    path('',HomePageView.as_view(),name='homepage'),
    path('activity/',ActivityPageView.as_view(),name='activity'),
    path('aboutus/',AboutUsView.as_view(),name='aboutus'),
]