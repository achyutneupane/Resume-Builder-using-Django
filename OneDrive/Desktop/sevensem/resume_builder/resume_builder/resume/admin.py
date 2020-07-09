from django.contrib import admin
from .models import *


class EducationalInfo(admin.TabularInline):
    model = EducationalInfo
    extra = 0

class ExperienceInfo(admin.TabularInline):
    model = ExperienceInfo
    extra = 0

class Skills(admin.TabularInline):
    model = Skills
    extra = 0

class Certificate(admin.TabularInline):
    model = Certificate
    extra = 0

class Language(admin.TabularInline):
    model = Language
    extra = 0

class Resume(admin.ModelAdmin):
    model   = PersonalInfo
    inlines = [EducationalInfo,ExperienceInfo,Skills,Certificate,Language]
# Register your models here.
admin.site.register(PersonalInfo,Resume)



