from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView

from introduce.models import TestModel

from django.http import HttpResponse
from django.template import Context, loader

class Introduce(TemplateView):
    template_name = 'introduce/index.html'


def AboutMe(request):
    template = loader.get_template('aboutme.html')
    return HttpResponse(template.render())

def IsWhat(request):
    template = loader.get_template('iswhat.html')
    return HttpResponse(template.render())

'''
class AboutMe(TemplateView):
    template_name = 'introduce/aboutme.html'

'''

'''
#--- TemplateView
class BooksModelView(TemplateView):
    template_name =  'books/index.html'

    def get_context_data(self, **kwargs):
        context = super(BooksModelView, self).get_context_data(**kwargs)
        context['object_list'] =  ['Book', 'Author', 'Publisher']
        return context

#--- ListView

class BookList(ListView):
    model = Book

class AuthorList(ListView):
    model = Author

class PublisherList(ListView):
    model = Publisher


#--- DetailView

class BookDetail(DetailView):
    model = Book

class AuthorDetail(DetailView):
    model = Author

class PublisherDetail(DetailView):
    model = Publisher

'''
