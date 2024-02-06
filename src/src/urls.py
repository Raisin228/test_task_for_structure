from django.contrib import admin
from django.urls import path
from interaction_with_cloud_app.views import main_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_page)
]
