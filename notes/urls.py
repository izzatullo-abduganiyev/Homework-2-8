from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import NoteViewSet, RegisterView, CustomTokenObtainPairView

router = DefaultRouter()
router.register('notes', NoteViewSet, basename='notes')

urlpatterns = [
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', CustomTokenObtainPairView.as_view(), name='login'),
]

urlpatterns += router.urls
