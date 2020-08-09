from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views
admin.site.site_header = "Ankit's Career Blog Admin"
admin.site.site_title = "Ankit's Career Blog Portal"
admin.site.index_title = "Welcome to Ankit's Career Blog"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('accounts/login/', views.LoginView.as_view(), name='login'),
     path('accounts/logout/', views.LogoutView.as_view(next_page='/'), name='logout'),
]