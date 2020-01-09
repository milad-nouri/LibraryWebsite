
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from catalog import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalog/', include('catalog.urls')),
    path('', views.index, name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

