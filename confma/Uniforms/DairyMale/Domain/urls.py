from django.urls import path, include
from ..Application.GetAndPostUniformsMale import GetAndPost
from ..Application.PutAndDeleteUniformsMale import PutAndDelete
from ..Application.FindByNameCollege import FindByNameCollege

urlpatterns = [
    path('', GetAndPost.as_view(), name="uniforms"),
    path('shirts/', include('confma.Uniforms.DairyMale.Shirts.Domain.urls'), name="shirts_male"),
    path('pants/', include('confma.Uniforms.DairyMale.Pants.Domain.urls'), name="pants_male"),
    path('find/<str:name>/', FindByNameCollege, name="find_by_name_college"),
    path('<id>/', PutAndDelete.as_view(),name="uniform_male_detail"),
]
