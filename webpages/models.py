from django.db import models
from django.db.models.base import Model
from django.template.defaultfilters import default, truncatechars
# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)
    subject = models.TextField(max_length=255)
    message = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Work(models.Model):
    category_name = models.CharField(max_length=255)
    project_name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="project_name")
    link = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.project_name


class Experience(models.Model):
    academic = models.CharField(max_length=255)
    board = models.CharField(max_length=255, blank=True)
    school = models.CharField(max_length=255, blank=True)
    percentage = models.CharField(max_length=255, blank=True)
    year = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.academic


class Achievement(models.Model):
    a_name = models.CharField(max_length=255)
    details = models.TextField(max_length=255)
    c_link = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to="certificate")
    date = models.CharField(max_length=255)

    def __str__(self):
        return self.a_name


class AboutMe(models.Model):
    description = models.TextField(max_length=255)
    pdf = models.FileField(upload_to='pdf')

    def __str__(self):
        return self.description

    @property
    def short_description(self):
        return truncatechars(self.description, 100)

    class Meta:
        verbose_name = 'AboutMe'
        verbose_name_plural = 'AboutMe'


class Info(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(
        upload_to="profile")
    github = models.CharField(max_length=100)
    linkedin = models.CharField(max_length=100)
    insta = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    @property
    def get_photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url
        else:
            return "/static/images/avatar-1.svg"


# www.linkedin.com/in/angshumaan-basumatary-74a267171
