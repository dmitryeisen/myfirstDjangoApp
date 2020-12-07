from django.urls import path

from . import views
app_name = 'boardmodul'
urlpatterns = [
    path("", views.index, name = "index"),
    path("<int:boardmodul_id>/", views.detail, name = "detail"),
    path("<int:boardmodul_id>/leave_comment/", views.leave_comment, name = "leave_comment"),

]
