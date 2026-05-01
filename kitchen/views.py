from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.db.models import Q

from kitchen.models import Dish, DishType
from kitchen.forms import (
    CookCreateForm,
    CookUpdateForm,

    DishForm,
    DishSearchForm,

    DishTypeForm,
)

@login_required
def index(request: HttpRequest) -> HttpResponse:
    num_cook = get_user_model().objects.count()
    num_dishes = Dish.objects.count()
    num_dish_type = DishType.objects.count()

    context = {
        "num_cook": num_cook,
        "num_dishes": num_dishes,
        "num_dish_type": num_dish_type
    }

    return render(request, "kitchen/index.html", context=context)


class CookListView(LoginRequiredMixin, generic.ListView):
    model = get_user_model()
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CookListView, self).get_context_data(**kwargs)
        query = self.request.GET.get("query", "")
        context["search_form"] = DishSearchForm(
            initial={"query": query}
        )
        return context

    def get_queryset(self):
        query = self.request.GET.get("query")
        queryset = get_user_model().objects.all()
        if query:
            return queryset.filter(
                Q(username__icontains=query) |
                Q(first_name__icontains=query) |
                Q(last_name__icontains=query)
            )
        return queryset


class DishTypesListView(LoginRequiredMixin, generic.ListView):
    model = DishType
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DishTypesListView, self).get_context_data(**kwargs)
        query = self.request.GET.get("query", "")
        context["search_form"] = DishSearchForm(
            initial={"query": query}
        )
        return context

    def get_queryset(self):
        query = self.request.GET.get("query")
        queryset = DishType.objects.all()
        if query:
            return queryset.filter(
                Q(name__icontains=query)            )
        return queryset


class DishTypesCreateView(LoginRequiredMixin, generic.CreateView):
    model = DishType
    form_class = DishTypeForm
    success_url = reverse_lazy("kitchen:dish-types")


class DishTypesDetailView(LoginRequiredMixin, generic.DetailView):
    model = DishType


class DishTypesUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = DishType
    form_class = DishTypeForm

    def get_success_url(self):
        return reverse("kitchen:dish_type-detail", kwargs={"pk": self.object.pk})


class DishTypesDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = DishType
    success_url = reverse_lazy("kitchen:dish-types")

class CookCreateView(LoginRequiredMixin, generic.CreateView):
    model = get_user_model()
    form_class = CookCreateForm
    success_url = reverse_lazy("kitchen:cook-list")


class CookDetailView(LoginRequiredMixin, generic.DetailView):
    model = get_user_model()


class CookUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = get_user_model()
    form_class = CookUpdateForm

    def get_success_url(self):
        return reverse("kitchen:cook-detail", kwargs={"pk": self.object.pk})


class CookDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = get_user_model()
    success_url = reverse_lazy("kitchen:cook-list")


class DishListView(LoginRequiredMixin, generic.ListView):
    model = Dish
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DishListView, self).get_context_data(**kwargs)
        query = self.request.GET.get("query", "")
        context["search_form"] = DishSearchForm(
            initial={"query": query}
        )
        return context

    def get_queryset(self):
        query = self.request.GET.get("query")
        queryset = Dish.objects.all()
        if query:
            return queryset.filter(
                Q(name__icontains=query) |
                Q(dish_type__name__icontains=query)
            )
        return queryset


class DishCreateView(LoginRequiredMixin, generic.CreateView):
    model = Dish
    form_class = DishForm
    success_url = reverse_lazy("kitchen:dish-list")

class DishDetailView(LoginRequiredMixin, generic.DetailView):
    model = Dish


class DishDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Dish
    success_url = reverse_lazy("kitchen:dish-list")

class DishUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Dish
    form_class = DishForm
    def get_success_url(self):
        return reverse("kitchen:dish-detail", kwargs={"pk": self.object.pk})


