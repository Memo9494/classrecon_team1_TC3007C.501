from django.urls import path
from .views import HomeView, CourseDetailView, attendance_statistics, take_attendance #,video_feed


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('<int:pk>/', CourseDetailView.as_view(), name='course_detail'),
    path('<int:pk>/take_attendance', take_attendance, name='take_attendance'),
    path('attendance/', attendance_statistics, name='attendance_statistics')
]