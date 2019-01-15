
from django.urls import path, include
from django.contrib import admin

api_urlpatters = [
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
]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('isodose.urls'))
]
