from django.urls import re_path
from .views import PlansView, PolicyDetailsView, MDPlanView

urlpatterns = [
    re_path(r'^plan/\d+/$', PlansView.as_view()),
    re_path(r'^plan/mdplan/([a-zA-Z0-9-]+)([a-zA-Z0-9-]+)|/$', MDPlanView.as_view()),
    re_path(r'^details/([a-zA-Z0-9-]+)([a-zA-Z0-9-]+)|/$', PolicyDetailsView.as_view()),

]