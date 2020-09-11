from django.urls import path, include

from ..Application.GetAndPostUniformFemale import GetAndPost
from ..Application.PutAndDeleteUniformFemale import PutAndDelete

urlpatterns = [
    path('', GetAndPost.as_view(), name="uniforms_female"),
    path('dresses/', include('confma.Uniforms.DairyFemale.Dresses.Domain.urls'), name="dresses"),
    path('shirts/', include('confma.Uniforms.DairyFemale.Shirts.Domain.urls'),name="shirts_female"),
    path('<id>/', PutAndDelete.as_view(),name="uniform_female_detail"),
]
