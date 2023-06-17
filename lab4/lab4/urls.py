
from django.contrib import admin
from django.urls import path
from movies import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/', views.movie_list),
    path('movies/<int:pk>/', views.movie_detail),
    path('movies/create/', views.movie_create),
    path('movies/<int:pk>/update/', views.movie_update),
    path('movies/<int:pk>/partial_update/', views.movie_partial_update),
    path('movies/<int:pk>/delete/', views.movie_delete),
]

