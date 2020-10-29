from django.urls import re_path
from .views import PlansView

urlpatterns = [
    re_path(r'^plan/([a-zA-Z0-9-]+)/$', PlansView.as_view()),

]