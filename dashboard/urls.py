from django.urls import path

from .views import (DashBoardsAPIView , DashBoardAPIView, 
                    TimeZoneHourAPIView, TimeZoneWeekAPIView, 
                    TimeZoneDayAPIView)


urlpatterns = [

                    path('dashboard/', DashBoardsAPIView.as_view(), name='dashboard'),
                    path('dashboard/<int:pk>/', DashBoardAPIView.as_view(), name='dashboard'),
                    path('dashboard/filterhour/<int:hour>/', TimeZoneHourAPIView.as_view(), name='time_zone'),
                    path('dashboard/filterday/<int:day>/', TimeZoneDayAPIView.as_view(), name='time_zone'),
                    path('dashboard/filterweek/<int:week>/', TimeZoneWeekAPIView.as_view(), name='time_zone'),
                    
                ]
