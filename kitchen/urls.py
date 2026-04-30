from django.urls import path
from .views import (
    index,
    CookListView,
    CookCreateView,
    CookDetailView,
    CookUpdateView,
    CookDeleteView,

    DishListView,
    DishCreateView,
    DishUpdateView,
    DishDetailView,
    DishDeleteView
)

urlpatterns = [
    path("", index, name="index"),
    path("cook/", CookListView.as_view(), name="cook-list"),
    path("cook/create/", CookCreateView.as_view(), name="cook-create"),
    path("cook/<int:pk>/detail", CookDetailView.as_view(), name="cook-detail"),
    path("cook/<int:pk>/delete", CookDeleteView.as_view(), name="cook-delete"),
    path("cook/<int:pk>/update", CookUpdateView.as_view(), name="cook-update"),

    path("dish/", DishListView.as_view(), name="dish-list"),
    path("dish/create", DishCreateView.as_view(), name="dish-create"),
    path("dish/<int:pk>/detail", DishDetailView.as_view(), name="dish-detail"),
    path("dish/<int:pk>/delete", DishDeleteView.as_view(), name="dish-delete"),

    path("dish/<int:pk>/update", DishUpdateView.as_view(), name="dish-update"),
]


app_name = "kitchen"
