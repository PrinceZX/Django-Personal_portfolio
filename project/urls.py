
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'project'

urlpatterns = [
    path('', views.all_projects, name='all_projects'),
    path('<int:project_id>/', views.detail, name='detail'),
    #path('<slug:slug>/', views.post_detail, name='detail'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)