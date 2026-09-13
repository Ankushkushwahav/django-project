from django.contrib import admin
from django.urls import path
from core.views import (
    reset_password_api,
    home,
    register_view,
    login_view,
    dashboard,
    add_task,
    complete_task,
    delete_task,
    logout_view,
    task_api,
    task_detail_api,
    login_api,
    jwt_login_api,
    react_register_api,
    forgot_password_api,
    profile_api,
    change_password_api,
    jwt_refresh_api,
    register_api,
    api_test_page,
    profile_api,
    logout_api,
)

urlpatterns = [
    path('api/reset-password/', reset_password_api, name='reset_password_api'),
    path('api/forgot-password/', forgot_password_api, name='forgot_password_api'),
    path('admin/', admin.site.urls),

    path('', home, name='home'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('dashboard/', dashboard, name='dashboard'),
    path('logout/', logout_view, name='logout'),

    path('task/add/', add_task, name='add_task'),
    path(
        'task/<int:task_id>/complete/',
        complete_task,
        name='complete_task'
    ),
    path(
        'task/<int:task_id>/delete/',
        delete_task,
        name='delete_task'
    ),

    path('api-test/', api_test_page, name='api_test_page'),
    path('api/profile/', profile_api, name='profile_api'),
    path('api/logout/', logout_api, name='logout_api'),
    path('api/register/', register_api, name='register_api'),
    path('api/jwt-login/', jwt_login_api, name='jwt_login_api'),
path('api/react-register/', react_register_api, name='react_register_api'),
path('api/jwt-refresh/', jwt_refresh_api, name='jwt_refresh_api'),
    path('api/login/', login_api, name='login_api'),
    path('api/tasks/', task_api, name='task_api'),
    path(
        'api/tasks/<int:task_id>/',
        task_detail_api,
        name='task_detail_api'
    ),
]
