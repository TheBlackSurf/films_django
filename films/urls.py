from django.urls import path
from films import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('index/', views.IndexView.as_view(), name='index'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path("register/", views.RegisterView.as_view(), name="register"),
    path('films/', views.film_list, name='films'),
]

htmx_urlpatterns = [
    path('check_username/', views.check_username, name='check_username'),
    path('check_title/', views.check_title, name='check_title'),
    path('check_password/', views.check_password, name='check_password'),
    path('add-film/', views.add_film, name='add-film'),
    path('search-film/', views.search_film, name='search-film'),
    path('delete-film/<str:pk>/', views.delete_film, name='delete-film'),
    path('change-film/<str:pk>/', views.change_status, name='change_status'),
]

urlpatterns += htmx_urlpatterns
