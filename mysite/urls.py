from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
	url(r'^admin/', admin.site.urls),
	url(r'^polls/', include('polls.urls')),
	url(r'^books/', include('books.urls')),
	# url(r'^introduce/', include('introduce.urls')),
	url(r'^', include('introduce.urls')),
	url(r'^blog/', include('blog.urls')),
]