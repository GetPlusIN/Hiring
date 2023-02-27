from django.urls import path

from . import views

# app_name = "books"
urlpatterns = [
    # path("<int:user_id>", views.index, name="index"),
    # path("<int:user_id>/create/", views.create, name="create"),
    # path("<int:user_id>/delete/", views.delete, name="delete"),
    # path("<int:user_id>/update/", views.update, name="update"),
    path("", views.book_list, name="list"),
    path("create/", views.book_new, name="create"),
    path("delete/", views.book_delete, name="delete"),
    path("update/", views.book_edit, name="update"),
    path("query/", views.book_detail, name="query"),
]
