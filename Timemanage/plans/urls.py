from django.urls import re_path
from .views import PlansView, PolicyDetailsView, MDPlanView

urlpatterns = [
    re_path(r'^details/$', PolicyDetailsView.as_view()),
    re_path(r'^plan/([a-zA-Z0-9-]+)([a-zA-Z0-9-]+)|/$', PlansView.as_view()),
    re_path(r'^plan/mdplan/([a-zA-Z0-9-]+)([a-zA-Z0-9-]+)|/$', MDPlanView.as_view()),

]