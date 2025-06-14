from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import *


urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('favorites/add/', views.add_to_favorite, name='add-favorite'),
    path('favorites/remove/', views.remove_from_favorite, name='remove-favorite'),
    path('favorites/', views.list_user_favorites, name='list-favorites'),

    path('flats/', get_flats),
    path('flats/<uuid:pk>/', get_flat),
    path('flats/create/', create_flat),
    path('flats/<uuid:pk>/edit/', edit_flat),
    path('flats/<uuid:pk>/delete/', delete_flat),

    path('gardenhouses/', get_gardenhouses),
    path('gardenhouses/<uuid:pk>/', get_gardenhouse),
    path('gardenhouses/create/', create_gardenhouse),
    path('gardenhouses/<uuid:pk>/edit/', edit_gardenhouse),
    path('gardenhouses/<uuid:pk>/delete/', delete_gardenhouse),

    path('offices/', get_offices),
    path('offices/<uuid:pk>/', get_office),
    path('offices/create/', create_office),
    path('offices/<uuid:pk>/edit/', edit_office),
    path('offices/<uuid:pk>/delete/', delete_office),

    path('garages/', get_garages),
    path('garages/<uuid:pk>/', get_garage),
    path('garages/create/', create_garage),
    path('garages/<uuid:pk>/edit/', edit_garage),
    path('garages/<uuid:pk>/delete/', delete_garage),

    path('lands/', get_lands),
    path('lands/<uuid:pk>/', get_land),
    path('lands/create/', create_land),
    path('lands/<uuid:pk>/edit/', edit_land),
    path('lands/<uuid:pk>/delete/', delete_land),


]

