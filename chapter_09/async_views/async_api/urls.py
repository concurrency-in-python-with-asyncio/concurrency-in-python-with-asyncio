from django.urls import path
from . import views

app_name = 'async_api'

urlpatterns = [
    path('', views.requests_view, name='requests'),
    path('sync_to_async', views.sync_to_async_view),
    path('async_to_sync', views.requests_view_sync)
]
