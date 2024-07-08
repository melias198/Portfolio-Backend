from django.db import models

class Introduction(models.Model):
    name = models.CharField(max_length=100)
    image = models.URLField(max_length=500)
    designation = models.CharField(max_length=250)
    description = models.TextField()  
    
    def __str__(self):
        return self.name

class About(models.Model):
    bio = models.CharField(max_length=200)
    headline = models.CharField(max_length=200)
    description = models.TextField()  
    
    def __str__(self):
        return self.bio

class Skill(models.Model):
    name = models.CharField(max_length=100)
    image = models.URLField(max_length=500)
    
    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=200)
    image = models.URLField(max_length=500)
    type = models.CharField(max_length=100) 
    backend_link = models.URLField(max_length=300)
    live_link = models.URLField(max_length=300)
    frontend_link = models.URLField(max_length=300, null=True, blank=True)
    technologies = models.ManyToManyField(Skill)
    
    def __str__(self):
        return self.name

class CodingProfile(models.Model): 
    name = models.CharField(max_length=200)
    image = models.URLField(max_length=500)
    rating = models.IntegerField()
    solved = models.IntegerField()
    link = models.URLField(max_length=200)
    
    def __str__(self):
        return self.name

class Blog(models.Model):
    image = models.URLField(max_length=500)
    headline = models.CharField(max_length=200)
    description = models.TextField()  
    link = models.URLField(max_length=500)
    
    def __str__(self):
        return self.headline

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField(max_length=2000)  
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
