from django.shortcuts import get_object_or_404,render
from .models import book
# Create your views here.

def books(request):
    all_books= book.objects.all()
    return render(request,"store/index.html", {
        "books": all_books
    })


def book_detail(request, slug):
    books = get_object_or_404(book,slug = slug)
    
    return render(request, "store/book_detail.html",{
        "title": books.title,
        "author": books.author,
        "rating": books.rating,
        "bestseller": books.is_bestSeller,
    })


