from django.urls import path
from . import views
from django.urls import re_path

urlpatterns = [
    path('', views.hello_world),
    path('social-media/', views.SocialMediaList.as_view()),
    path('transaction/<slug:pk>/', views.TransactionDetail.as_view()),
    path('watchlist/', views.WatchlistList.as_view()),
    path('website-report/', views.WebsiteReportView.as_view()),
    path('node/<slug:address>/', views.node_view),
    path('geofencer/', views.get_geofencer),
    re_path(r'^totp/create/$', views.TOTPCreateView.as_view(), name='totp-create'),
    re_path(r'^totp/login/(?P<token>[0-9]{6})/$', views.TOTPVerifyView.as_view(), name='totp-login'),
    path("login/", views.LoginView.as_view(), name="login"),
]