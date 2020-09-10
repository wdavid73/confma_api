from django.urls import path, include

from ..Application.GetAndPostUniformFemale import GetAndPostUniformFemale
from ..Application.PutAndDeleteUniformFemale import PutAndDeleteUniformFemale

urlpatterns = [
    path('', GetAndPostUniformFemale.as_view(), name="uniforms"),

    path('dresses/', include('confma.Uniforms.DairyFemale.Dresses.Domain.urls'), name="dresses"),
    path('shirts/', include('confma.Uniforms.DairyFemale.Shirts.Domain.urls'),
         name="shirts_female"),
    path('<id>/', PutAndDeleteUniformFemale.as_view(),
         name="uniform_female_detail"),

]
