"""Microservice_1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from authentication import views

urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('verifyToken/', views.VerifyTokenView.as_view()),
    path('contractor/', views.ContractorCreateView.as_view()),
    path('contractor/all',views.ContractorApi.as_view()), #Permite ver todos los usuarios
    path('contractor/create',views.ContractorDetailView.as_view()),
    path('contractor/<int:pk>',views.ContractorUpdateApi.as_view()),
    path('contractor/<int:pk>/delete',views.ContractorDeleteApi.as_view()),
    path('specialist/all',views.SpecialistApi.as_view()), #Permite ver todos los usuarios
    path('specialist/create',views.SpecialistDetailView.as_view()),
    path('specialist/<int:pk>',views.SpecialistUpdateApi.as_view()),
    path('specialist/<int:pk>/delete',views.SpecialistDeleteApi.as_view()),
    path('specialist/allXcategory/<str:param>',views.SpecialistApiXCategory.as_view()),
    #url(r'^specialist/allXcategory/(?P<cat>\s+)/$',views.SpecialistApiXCategory.as_view(), name="SpecialistApiXCategory"),
]
