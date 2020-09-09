from django.urls import path, include

urlpatterns = [
    path('deportives/', include('confma.Uniforms.Deportive.Domain.urls')),
    path('dairy_male/', include('confma.Uniforms.DairyMale.Domain.urls')),
    path('dairy_female/', include('confma.Uniforms.DairyFemale.Domain.urls')),
]
