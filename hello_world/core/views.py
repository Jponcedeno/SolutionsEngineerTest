
from ..models import Book
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from ..models import Book

def index(request):
    books = Book.objects.all()
    book_count = books.count()  # Get the total number of books
    print("Books", books)
    context = {
        "title": "Django example",
        "books": books,
        "book_count": book_count
        
    }
    return render(request, "index.html", context)


@csrf_exempt
@csrf_exempt
def add_book(request):
    if request.method == 'POST':
        if request.content_type == 'application/json':
            data = json.loads(request.body)
            book = Book.objects.create(
                title=data['title'],
                author=data['author'],
                published_date=data['published_date'],
                isbn=data['isbn'],
                price=data['price'],
                stock_quantity=data['stock_quantity']
            )
            return JsonResponse({'id': book.id})
        else:
            book = Book.objects.create(
                title=request.POST['title'],
                author=request.POST['author'],
                published_date=request.POST['published_date'],
                isbn=request.POST['isbn'],
                price=request.POST['price'],
                stock_quantity=request.POST['stock_quantity']
            )
            return redirect('add_book')
    else:
        return render(request, 'add_book.html')


# Retrieve Book Endpoint
@csrf_exempt
def retrieve_book(request, isbn):
    try:
        book = get_object_or_404(Book, isbn=isbn)
        if request.content_type == 'application/json':
            data = {
                'title': book.title,
                'author': book.author,
                'published_date': book.published_date,
                'isbn': book.isbn,
                'price': book.price,
                'stock_quantity': book.stock_quantity
            }
            return JsonResponse(data)
        else:
            context = {
                'book': book
            }
            return render(request, 'book_detail.html', context)
    except Book.DoesNotExist:
        return JsonResponse({'error': 'Book not found'}, status=404)

# Update Stock Quantity Endpoint
@csrf_exempt
def update_stock(request, isbn):
    if request.method == 'PUT':
        if request.content_type == 'application/json':
            data = json.loads(request.body)
            stock_quantity = data.get('stock_quantity')
            if stock_quantity is not None:
                try:
                    book = get_object_or_404(Book, isbn=isbn)
                    book.stock_quantity = stock_quantity
                    book.save()
                    return JsonResponse({'status': 'Stock updated'})
                except Book.DoesNotExist:
                    return JsonResponse({'error': 'Book not found'}, status=404)
            else:
                return JsonResponse({'error': 'Stock quantity not provided'}, status=400)
        else:
            return JsonResponse({'error': 'Invalid content type'}, status=400)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

# Delete Book Endpoint
@csrf_exempt
def delete_book(request, isbn):
    if request.method == 'DELETE':
        try:
            book = get_object_or_404(Book, isbn=isbn)
            book.delete()
            return JsonResponse({'status': 'Book deleted'})
        except Book.DoesNotExist:
            return JsonResponse({'error': 'Book not found'}, status=404)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)    
