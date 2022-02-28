from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from . import models
from . import forms
from checker.utils import get_news_by_source
import threading
from django.http import HttpResponse


class sourceListView(generic.ListView):
    model = models.source
    form_class = forms.sourceForm


class sourceCreateView(generic.CreateView):
    model = models.source
    form_class = forms.sourceForm


class sourceDetailView(generic.DetailView):
    model = models.source
    form_class = forms.sourceForm


class sourceUpdateView(generic.UpdateView):
    model = models.source
    form_class = forms.sourceForm
    pk_url_kwarg = "pk"


class sourceDeleteView(generic.DeleteView):
    model = models.source
    success_url = reverse_lazy("checker_source_list")


class newsListView(generic.ListView):
    model = models.news
    form_class = forms.newsForm
    paginate_by = 9


class newsCreateView(generic.CreateView):
    model = models.news
    form_class = forms.newsForm


class newsDetailView(generic.DetailView):
    model = models.news
    form_class = forms.newsForm


class newsUpdateView(generic.UpdateView):
    model = models.news
    form_class = forms.newsForm
    pk_url_kwarg = "pk"


class newsDeleteView(generic.DeleteView):
    model = models.news
    success_url = reverse_lazy("checker_news_list")


def check_news(request, pk):
    news_thread = threading.Thread(target=get_news_by_source, name="news_getter", args=[pk])
    news_thread.start()
    context = {'message': 'Please wait. Processing Source.'}
    return render(request, "index.html", context)
