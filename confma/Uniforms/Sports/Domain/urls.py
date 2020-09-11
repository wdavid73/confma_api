from django.urls import path,include

from ..Application.GetAndPostSports import GetAndPost
from ..Application.PutAndDeleteSports import PutAndDelete

urlpatterns = [
    path('', GetAndPost.as_view(), name="uniforms_sports"),
    path('shirts/', include('confma.Uniforms.Sports.Shirts.Domain.urls'), name="sports_shirts"),
    path('sweat_shirt/', include('confma.Uniforms.Sports.SweatShirt.Domain.urls'), name="sports_sweatshirt"),
    path('<id>/',PutAndDelete.as_view() , name="uniform_sports_detail")

]
