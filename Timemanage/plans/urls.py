from django.urls import re_path
from .views import PlansView

urlpatterns = [
    re_path(r'^plan/$', PlansView.as_view()),

]