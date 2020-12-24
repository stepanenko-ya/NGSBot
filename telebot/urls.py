from django.urls import path
from. import views

urlpatterns = [
    path("", views.main_page, name="main_page"),
    path("ajax_send_message/", views.ajax_send_message, name="ajax_send_message"),
    path("update_ajax/", views.update_ajax, name="update_ajax"),
]
