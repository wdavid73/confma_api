from django.urls import path, include

from ..Application.GetAndPostUniformFemale import GetAndPost
from ..Application.PutAndDeleteUniformFemale import PutAndDelete
from ..Application.FindByNameCollege import FindByNameCollege

urlpatterns = [
    path('', GetAndPost.as_view(), name="uniforms_female"),
    path('find/<int:id>/', FindByNameCollege, name="find_by_name_college"),
    path('<id>/', PutAndDelete.as_view(), name="uniform_female_detail"),
]
