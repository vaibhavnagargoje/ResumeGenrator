from . import views
from django.urls import path

urlpatterns=[
    path('',views.accepts,name="accept"),
    path('<int:id>/',views.resume,name="resume"),
    path("list/",views.list,name="list"),

]