from django.urls import path

from .views import UserListCreateView, UserUpdateView

urlpatterns = [
    path('', UserListCreateView.as_view(), name='get_create_users'),
    path('/<int:id>', UserUpdateView.as_view(), name='get_update_user_by_id')
]
