from django.contrib import admin
from django.urls import path, include
admin.site.site_header = "Ankit's Career Blog Admin"
admin.site.site_title = "Ankit's Career Blog Portal"
admin.site.index_title = "Welcome to Ankit's Career Blog"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
]