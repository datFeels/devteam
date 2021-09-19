from django.urls import path
from .views import course_list, course_create_view, course_update_view

urlpatterns = [
    path('', course_list, name='course-list'),
    path('create/', course_create_view, name='course-create'),
    path('<int:id>/update/', course_update_view, name='course-update')
]