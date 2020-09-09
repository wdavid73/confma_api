from django.urls import path, include

from ..Application.GetUniformsMale import GetUniformsMale

urlpatterns = [
    path('', GetUniformsMale.as_view(), name="uniforms"),
    path('shirts/', include('confma.Uniforms.DairyMale.Shirts.Domain.urls'), name="shirts_male"),
    path('pants/', include('confma.Uniforms.DairyMale.Pants.Domain.urls'), name="pants_male"),
]
