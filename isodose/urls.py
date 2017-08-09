from django.conf.urls import url
import views

urlpatterns = [
    url(r'^simulation/start', views.start_simulation)
]
