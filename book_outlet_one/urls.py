from django.urls import path
from .import views

urlpatterns = [
    path("", views.all_books),
    path("<slug:slug>", views.book_detail, name="book-detail")
]
