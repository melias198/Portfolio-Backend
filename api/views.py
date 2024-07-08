from rest_framework import generics
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from .models import Introduction,About,Project,Skill,CodingProfile,Blog,Contact
from .serializers import IntroductionSerializer,AboutSerializer,ProjectSerializer,SkillSerializer,CodingProfileSerializer,BlogSerializer,ContactSerializer


class IntroductionView(generics.ListAPIView):
    queryset = Introduction.objects.all()
    serializer_class = IntroductionSerializer
    
class AboutView(generics.ListAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer
    
class ProjectView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class SkillView(generics.ListAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    
class CodingProfileView(generics.ListAPIView):
    queryset = CodingProfile.objects.all()
    serializer_class = CodingProfileSerializer
    
class BlogView(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class ContactCreateView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def perform_create(self, serializer):
        contact = serializer.save()
        self.send_contact_email(contact)

    def send_contact_email(self, contact):
        subject = "Portfolio Message"
        context = {
            'name': contact.name,
            'email': contact.email,
            'message': contact.message
        }
        message = render_to_string('contact_email.html', context)
        recipient_list = ["meliash198@gmail.com"]
        
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            recipient_list,
            fail_silently=False,
            html_message=message  
        )