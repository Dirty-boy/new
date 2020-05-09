
from django.urls import path
from . import views
urlpatterns = [
    path('good/',views.Tested.as_view()),
    path('oo/',views.CC),
]
