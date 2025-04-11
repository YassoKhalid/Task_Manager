from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect  # For redirecting the root URL

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', include('tasks.urls')),
    path('accounts/', include('django.contrib.auth.urls')),  # This includes the authentication URLs
    path('', lambda request: redirect('task_list')),  # Redirect root URL to the task list
]
