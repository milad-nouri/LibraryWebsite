from django.urls import path
from . import views

urlpatterns = [
    
    path('page', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
#  angle brackets define the part of the URL to be captured,
#  enclosing the name of the variable that the view can use to access the captured data.
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail')
]