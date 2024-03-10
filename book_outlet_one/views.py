from django.shortcuts import get_object_or_404, render, get_list_or_404

import book_outlet_one
from .models import Book, Author
from django.db.models import Avg

# Create your views here.

def all_books(request):
    book = Book.objects.all().order_by("title")
    book_count = book.count()
    avg_rating = book.aggregate(Avg("rating"))

    return render(request, "book_outlet_one/index.html", {
        "total_book": book,
        "book_count": book_count,
        "avg_of_book": avg_rating
    })

def book_detail(request, slug):
    book = get_object_or_404(Book, slug=slug)
    return render(request, "book_outlet_one/indiviualbook.html", {
        "title": book.title,
        "rating": book.rating,
        "author": book.author,
        "published_countries": book.published_countries
    })