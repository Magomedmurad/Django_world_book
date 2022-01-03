from django.template.defaulttags import url
from django.urls import path
from .import views

urlpatterns = [

    path('', views.index, name='index'),
    url(r'^mybooks/$', views.LoanedВooksByUserListView.as_view(), name='my-borrowed'),
    url(r'^book/create/$', views.BookCreate.as_view(), name='book_create'),
    url(r'^book/update/(?P<pk>\d+)$', views.BookUpdate.as_view(), name='book_update'),
    url(r'^book/delete/(?P<pk>\d+)$', views.BookDelete.as_view(), name='book_delete'),
]