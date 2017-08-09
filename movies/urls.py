from django.conf.urls import url
from movies import views

urlpatterns = [
    url(r'^movies/$',views.MoviesList.as_view()),
]
