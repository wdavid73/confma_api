from django.urls import path,include

from ..Application.GetAndPostShirtsFemale import GetAndPost
from ..Application.PutAndDeleteShirtsFemale import PutAndDelete
urlpatterns = [
    path('', GetAndPost.as_view(), name="get_shirts_female"),
    path('<id>/',PutAndDelete.as_view(),name="shirts_female_details")
]