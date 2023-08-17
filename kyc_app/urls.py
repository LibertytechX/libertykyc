from django.urls import path
from kyc_app import views


urlpatterns = [
    path("dojah-bvn-verification", views.DojahBvNverificationView.as_view())
]