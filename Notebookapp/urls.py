from django.urls import path

from Notebookapp import  views

urlpatterns = [
    # get the data
    path('get/',views.newbook_view),
    # post the data
    path('post/',views.postNootbook_view),
    path('put/<int:id>/',views.updateNotebook_view),
    path('delete/<int:id>/',views.deleteNotbook_view),


]