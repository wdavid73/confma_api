from django.urls import path, include

urlpatterns = [
    path('sports/', include('confma.Uniforms.Sports.Domain.urls')),
    path('dairy_male/', include('confma.Uniforms.DairyMale.Domain.urls')),
    path('dairy_female/', include('confma.Uniforms.DairyFemale.Domain.urls')),
    path('shirts/', include('confma.Uniforms.Shirts.Domain.urls')),
    path('pants/', include('confma.Uniforms.Pants.Domain.urls')),
    path('dreesses/', include('confma.Uniforms.Dresses.Domain.urls')),
    path('shields/', include('confma.Uniforms.Shields.domain.urls')),
]
