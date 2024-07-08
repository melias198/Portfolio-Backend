from django.urls import path
from .views import IntroductionView,AboutView,ProjectView,SkillView,CodingProfileView,BlogView,ContactCreateView

urlpatterns = [
    path('intro/',IntroductionView.as_view(),name='introduction'),
    path('about/',AboutView.as_view(),name='about'),
    path('project/',ProjectView.as_view(),name='project'),
    path('skill/',SkillView.as_view(),name='skill'),
    path('cp/',CodingProfileView.as_view(),name='cp'),
    path('blog/',BlogView.as_view,name='blog'),
    path('contact/',ContactCreateView.as_view(),name='contact'),
]
