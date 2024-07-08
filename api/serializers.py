from rest_framework import serializers
from .models import Introduction, About, Skill, Project, CodingProfile, Blog, Contact

class IntroductionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Introduction
        fields = '__all__'

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    technologies = serializers.StringRelatedField(many=True)
    class Meta:
        model = Project
        fields = '__all__'

class CodingProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CodingProfile
        fields = '__all__'

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
