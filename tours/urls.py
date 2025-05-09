from django.urls import path
from . import views

# URL routes for the tours app
urlpatterns = [
    path('', views.tour_list, name='tour_list'),                   # Main page (list of tours)
    path('tour/<int:pk>/', views.tour_detail, name='tour_detail'), # Detail page for specific tour
    path('tour/<int:pk>/book/', views.book_tour, name='book_tour'),
    path('my-bookings/', views.my_bookings, name='my_bookings'),

]
