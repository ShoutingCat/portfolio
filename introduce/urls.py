from django.conf.urls import url
from introduce import views

app_name = 'introduce'
urlpatterns = [

    url(r'^$', views.Introduce.as_view(), name='index'),
    url(r'^aboutme/$', views.AboutMe, name='aboutme'),
    url(r'^iswhat/$', views.IsWhat, name='iswhat'),

]



'''
   url(r'^$', views.BooksModelView.as_view(), name='index'),
   url(r'^book/$', views.BookList.as_view(), name ='book_list'),
   url(r'^author/$', views.AuthorList.as_view(), name ='author_list'),
   url(r'^publisher/$', views.PublisherList.as_view(), name='publisher_list'),
'''
