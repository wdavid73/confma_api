from django.urls import path, include

from ..Application.GetAndPostUniformFemale import GetAndPost
from ..Application.PutAndDeleteUniformFemale import PutAndDelete

urlpatterns = [
    path('', GetAndPost.as_view(), name="uniforms_female"),
    path('<id>/', PutAndDelete.as_view(),name="uniform_female_detail"),
]
