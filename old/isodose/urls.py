from django.urls import path
from . import views

urlpatterns = [
    path('simulations/', views.SimulationViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('simulations/<pk>/', views.SimulationViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path('simulations/<pk>/run/', views.SimulationViewSet.as_view({
        'get': 'run'
    })),
    # path(r'^simulation/start', views.start_simulation),
    # path(r'^simulation', views.create_simulation)
]
