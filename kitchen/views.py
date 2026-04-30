from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.conf import settings

from kitchen.forms import CookCreateForm, CookUpdateForm, DishForm
from kitchen.models import Dish, DishType


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


class CookListView(generic.ListView):
    model = get_user_model()
    paginate_by = 2


class CookCreateView(generic.CreateView):
    model = get_user_model()
    form_class = CookCreateForm
    success_url = reverse_lazy("kitchen:cook-list")


class CookDetailView(generic.DetailView):
    model = get_user_model()


class CookUpdateView(generic.UpdateView):
    model = get_user_model()
    form_class = CookUpdateForm

    def get_success_url(self):
        return reverse("kitchen:cook-detail", kwargs={"pk": self.object.pk})


class CookDeleteView(generic.DeleteView):
    model = get_user_model()
    success_url = reverse_lazy("kitchen:cook-list")


class DishListView(generic.ListView):
    model = Dish
    paginate_by = 3


class DishCreateView(generic.CreateView):
    model = Dish
    form_class = DishForm
    success_url = reverse_lazy("kitchen:dish-list")

class DishDetailView(generic.DetailView):
    model = Dish


class DishDeleteView(generic.DeleteView):
    model = Dish
    success_url = reverse_lazy("kitchen:dish-list")

class DishUpdateView(generic.UpdateView):
    model = Dish
    form_class = DishForm
    def get_success_url(self):
        return reverse("kitchen:dish-detail", kwargs={"pk": self.object.pk})


