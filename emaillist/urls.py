from django.urls import path
from .views import EmailCreateView, EmailDeleteView, EmailListView, send_email

urlpatterns = [
    path('add-email/', EmailCreateView.as_view(), name='add_email'),
    path('delete-email/<int:pk>/', EmailDeleteView.as_view(), name='delete_email'),
    path('list-email/', EmailListView.as_view(), name='list_email'),
    path('send-email/', send_email, name='send_email'),
]