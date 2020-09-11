from django.urls import path, include

from ..Application.GetAndPostUniformsMale import GetAndPost
from ..Application.PutAndDelete import PutAndDelete
urlpatterns = [
    path('', GetAndPost.as_view(), name="uniforms"),
    path('shirts/', include('confma.Uniforms.DairyMale.Shirts.Domain.urls'), name="shirts_male"),
    path('pants/', include('confma.Uniforms.DairyMale.Pants.Domain.urls'), name="pants_male"),
    path('<id>/', PutAndDelete.as_view(),
         name="uniform_male_detail"),
]
