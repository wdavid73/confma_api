from django.urls import path,include

from ..Application.GetUniformFemale import GetUniformFemale

urlpatterns = [
    path('', GetUniformFemale.as_view(), name="uniforms"),
    path('dresses/', include('confma.Uniforms.DairyFemale.Dresses.Domain.urls'), name="dresses"),
    path('shirts/', include('confma.Uniforms.DairyFemale.Shirts.Domain.urls'), name="shirts_female")
]
