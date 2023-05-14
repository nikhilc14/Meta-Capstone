from django.contrib import admin
from django.urls import path,include
from . import views
from rest_framework import routers
from .views import BookingViewSet
from rest_framework.authtoken.views import obtain_auth_token 

#router = routers.DefaultRouter()
#router.register(r'tables', BookingViewSet)

urlpatterns = [
    path('menu-items/', views.MenuItemsView.as_view()),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
    path('restaurant/booking/', views.BookingViewSet.as_view()),
    path('api-token-auth/', obtain_auth_token),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken'))
]
 