from django.urls import path
from .views import NoteListCreateView, NoteDetailView, RegisterView, CustomTokenObtainPairView

urlpatterns = [
    path('notes/', NoteListCreateView.as_view()),
    path('notes/<int:pk>/', NoteDetailView.as_view()),
    path('auth/register/', RegisterView.as_view()),
    path('auth/login/', CustomTokenObtainPairView.as_view()),
]
