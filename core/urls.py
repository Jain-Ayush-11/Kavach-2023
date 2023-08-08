from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello_world),
    path('social-media/', views.SocialMediaList.as_view()),
    path('transaction/<slug:pk>/', views.TransactionDetail.as_view()),
    path('watchlist/', views.WatchlistList.as_view()),
    path('node/<slug:address>/', views.node_view),
]