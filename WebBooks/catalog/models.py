from django.db import models
from django.urls import reverse
# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=200,
                            help_text='Input genre book',
                            verbose_name='Genre book')
    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=20,
                            help_text='Input language book',
                            verbose_name='Language book')
    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=20,
                            help_text='Input name of publisher',
                            verbose_name='Publisher')
    def __str__(self):
        return self.name


class Autor(models.Model):
    first_name = models.CharField(max_length=100,
                            help_text='Input name autor',
                            verbose_name='Name autor')
    last_name = models.CharField(max_length=100,
                            help_text='Input lastname autor',
                            verbose_name='Lastname autor')
    date_of_birth = models.DateField(
        help_text='Input date of birth',
        verbose_name='Date of birth',
        null=True, blank=True
    )
    about = models.TextField(help_text='Input info about autor',
                             verbose_name='About autor')
    photo = models.ImageField(upload_to='images',
                              help_text='Input foto autor',
                              verbose_name='Foto autor',
                              null=True, blank=True)

    def __str__(self):
        return self.last_name

class Book(models.Model):
    title = models.CharField(max_length=200,
                             help_text='Input name book',
                             verbose_name='Name book')
    genre = models.ForeignKey('Genre',
                              on_delete=models.CASCADE,
                              help_text="Choice genre for book",
                              verbose_name='Genre book', null=True)
    language = models.ForeignKey('Language',
                              on_delete=models.CASCADE,
                              help_text="Choice language for book",
                              verbose_name='Language book', null=True)
    publisher = models.ForeignKey('Publisher',
                              on_delete=models.CASCADE,
                              help_text="Choice publisher",
                              verbose_name='Publisher', null=True)
    year = models.CharField(max_length=4,
                            help_text='Choice year publish')
    author = models.ManyToManyField('Autor',
                                    help_text='Choice author(s) book',
                                    verbose_name='Autor(s) book')
    summary = models.TextField(max_length=1000,
                               help_text='Input summary of book',
                               verbose_name='Annotation of book')
    ibsn = models.CharField(max_length=13,
                            help_text='Must input 13 char',
                            verbose_name='IBSN book')
    price = models.DecimalField(decimal_places=2, max_digits=7,
                                help_text='Input price of book',
                                verbose_name='Price (usd.)')
    photo = models.ImageField(upload_to='images',
                              help_text='Input image book',
                              verbose_name='Image book')

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])
    def display_author(self):
        return ', '.join([author.last_name for author in self.author.all()])
    display_author.short_description = 'Autors'



class Status(models.Model):
    name = models.CharField(max_length=20,
                            help_text="Input status exemplar of book",
                            verbose_name='STATUS')
    def __str__(self):
        return self.name

class BookInstance(models.Model):
    book = models.ForeignKey('Book', on_delete=models.CASCADE, null=True)
    inv_nom = models.CharField(
        max_length=20,
        null=True,
        help_text='Input inventar number exemplar',
        verbose_name='Inventar number')
    status = models.ForeignKey('Status',
                               on_delete=models.CASCADE,
                               null=True,
                               help_text='Change state exemplar',
                               verbose_name='Status exemplar book')
    due_back = models.DateField(null=True, blank=True,
                                help_text='Input end time status',
                                verbose_name='Date of end status')

    class Meta:
        ordering = ['due_back']
    def __str__(self):
        return '%s %s %s' % (self.inv_nom, self.book, self.status)
