from django.urls import path

from api import views

urlpatterns = [
    path('drivers/', views.driver_list),
    path('drivers/<int:pk>', views.driver_detail),

    path('teams/', views.team_list),
    path('teams/<int:pk>', views.team_detail)
]