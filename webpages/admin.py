from django.contrib import admin
from . models import AboutMe, Achievement, Contact, Experience, Info, Work
from django.utils.html import format_html
# Register your models here.


class AdminExperience(admin.ModelAdmin):
    list_display = ('academic', 'year', 'created_at')
    list_filter = ('academic',)


class AdminContact(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message')
    list_filter = ('name',)


class AdminWorks(admin.ModelAdmin):
    def image(self, object):
        return format_html('<img src="{}" width="30" style="border-radius:50%;">'.format(object.photo.url))

    list_display = ('project_name', 'image', 'link')
    list_filter = ('project_name',)


class AdminAchievement(admin.ModelAdmin):
    def photo(self, object):
        return format_html('<img src="{}" width="30" style="border-radius:50%;">'.format(object.image.url))
    list_display = ('a_name', 'details', 'photo', 'c_link')
    list_filter = ('a_name',)


class AdminAboutMe(admin.ModelAdmin):
    list_display = ('short_description', 'pdf')


class AdminInfo(admin.ModelAdmin):
    def profile(self, object):
        return format_html('<img src="{}" width="30" style="border-radius:50%;">'.format(object.get_photo_url))
    list_display = ('name', 'profile', 'github', 'linkedin', 'insta')


admin.site.register(Contact, AdminContact)
admin.site.register(Work, AdminWorks)
admin.site.register(Experience, AdminExperience)
admin.site.register(Achievement, AdminAchievement)
admin.site.register(AboutMe, AdminAboutMe)
admin.site.register(Info, AdminInfo)
