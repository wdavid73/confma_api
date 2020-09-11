from django.urls import path,include

from ..Application.GetAndPostSweatShirt import GetAndPost

urlpatterns = [
    path('', GetAndPost.as_view(), name="get_sweatshirts_sports"),
]