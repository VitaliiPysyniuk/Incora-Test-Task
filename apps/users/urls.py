from django.urls import path

from .views import UserListCreateView, UserRetrieveUpdateView

urlpatterns = [
    path('', UserListCreateView.as_view(), name='get_create_users'),
    path('/<int:id>', UserRetrieveUpdateView.as_view(), name='get_update_user_by_id'),
]
