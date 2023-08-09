from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello_world),
    path('social-media/', views.SocialMediaList.as_view()),
    path('transaction/<slug:pk>/', views.TransactionDetail.as_view()),
    path('watchlist/', views.WatchlistList.as_view()),
    path('website-report/', views.WebsiteReportView.as_view()),
    path('node/<slug:address>/', views.node_view),
    path('geofencer/', views.get_geofencer),
    path('demixer/', views.demixing),
    path('destination-address/<slug:tx_id>/', views.get_dest),
    path('report/', views.ReportView.as_view()),
]