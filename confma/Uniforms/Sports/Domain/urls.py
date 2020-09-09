from django.urls import path,include

from ..Application.GetUniformSports import GetUniformSports

urlpatterns = [
    path('', GetUniformSports.as_view(), name="uniforms_sports"),
    path('shirts/', include('confma.Uniforms.Sports.Shirts.Domain.urls'), name="sports_shirts"),
    path('sweat_shirt', include('confma.Uniforms.Sports.SweatShirt.Domain.urls'), name="sports_sweatshirt"),
]
