from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Autor, BookInstance
from django.views.generic import ListView, DetailView

class AutorDetailView(DetailView):
    model = Autor

class AutorListView(ListView):
    model = Autor
    paginate_by = 4

class BookDetailView(DetailView):
    model = Book
    context_object_name = 'book'

class BookListView(ListView):
    model = Book
    context_object_name = 'books'
    paginate_by = 5

def index(request):
    text_head = 'На нашем сайте вы можете получить книги в электронном виде'
    books = Book.objects.all()
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(
        status__exact=2).count()
    authors = Autor.objects
    num_authors = Autor.objects.count()
    context = {'text_head': text_head,
               'books': books, 'num_books': num_books,
               'num_instances': num_instances,
               'num_instances_available': num_instances_available,
               'authors': authors, 'num_authors': num_authors}
    return render(request, 'catalog/index.html', context)


def about(request):
    text_head = 'Сведения о компании'
    name = 'ООО "Интелектуальные информационные системы"'
    rab1 = 'Разаработка проложений на основе систем искусственного интелекта'
    rab2 = 'Распознавание обьектов дорожной инфраструктуры'
    rab3 = 'Создание графических АРТ-обьектов на основе систем искусственного интелекта'
    rab4 = 'Создание цифровых интерактивных книгб учебных пособий фвтоматизирываных обучающих систем'
    context = {
        'text_head': text_head, 'name': name,
        'rab1': rab1, 'rab2': rab2, 'rab3': rab3, 'rab4': rab4
    }
    return render(request, 'catalog/about.html', context)

def contact(request):
    text_head = 'Контакты'
    name = 'ООО "Интелектуальные информационные системы"'
    address = 'Днепр, Спасская 221а'
    tel = '380976543123'
    email = 'gwondoys@gmail.com'
    context = {
        'text_head': text_head,
        'name': name, 'address': address,
        'tel': tel, 'email': email
    }
    return render(request, 'catalog/contact.html', context)


























