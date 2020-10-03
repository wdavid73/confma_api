from django.urls import path, include
from ..Application.GetAndPostUniformsMale import GetAndPost
from ..Application.PutAndDeleteUniformsMale import PutAndDelete
from ..Application.FindByNameCollege import FindByNameCollege

urlpatterns = [
    path('', GetAndPost.as_view(), name="uniforms"),
    path('find/<int:id>/', FindByNameCollege, name="find_by_name_college"),
    path('<id>/', PutAndDelete.as_view(), name="uniform_male_detail"),
]
