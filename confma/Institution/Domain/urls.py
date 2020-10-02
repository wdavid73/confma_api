from django.urls import path

from ..Application.GetAndPostInstitution import GetAndPost

urlpatterns = [
    path('', GetAndPost.as_view(), name="institution_get_post")
]
