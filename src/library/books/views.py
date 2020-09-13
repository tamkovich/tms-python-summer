from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Books


class BookCreate(PermissionRequiredMixin, CreateView):
    permission_required = 'polls.can_add'
    model = Books
    fields = ["title", "author_name", "description"]


class BookUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'polls.can_edit'
    model = Books
    fields = ["title", "author_name", "description"]


class BookDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'polls.can_delete'
    model = Books
    success_url = reverse_lazy('index')


class BookListView(ListView):
    model = Books
    context_object_name = 'book_list'
    queryset = Books.objects.order_by('-id')
    template_name = 'books/index.html'


class BookDetailView(DetailView):
    model = Books
    context_object_name = 'book_detail'
