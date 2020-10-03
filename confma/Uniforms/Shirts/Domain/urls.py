from django.urls import path, include

from ..Application.GetAndPostShirtsMale import GetAndPost
from ..Application.PutAndDeleteShirtsMale import PutAndDelete
from ..Application.GetShirtByType import getShirtsMale, getShirtsFemale

urlpatterns = [
    path('', GetAndPost.as_view(), name="get_all_shirts"),
    path('male/', getShirtsMale, name="get_shirt_male"),
    path('female/', getShirtsFemale, name="get_shirt_female"),
    path('<id>/', PutAndDelete.as_view(), name="shirts_detail")
]
