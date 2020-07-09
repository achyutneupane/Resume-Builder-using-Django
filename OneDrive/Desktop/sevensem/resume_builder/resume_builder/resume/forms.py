from django import forms
from django.forms.fields import DateField
from .models import *

YEARS = [x for x in range(1940, 2030)]


class PersonalInfoForm(forms.ModelForm):
    class Meta:
        model = PersonalInfo
        gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect(
            attrs={'required': 'required', 'class': "form-check-input", 'type': "radio"})
                                   )

        fields = ['firstname', 'middlename', 'lastname', 'email', 'dob', 'gender', 'phone', 'country', 'state', 'city']
        widgets = {

            'firstname': forms.TextInput(
                attrs={'class': 'form-control', 'required': 'required', 'placeholder': "First Name"}),
            'middlename': forms.TextInput(
                attrs={'class': 'form-control ', 'required': 'required', 'placeholder': "Middle Name"}),
            'lastname': forms.TextInput(
                attrs={'class': 'form-control ', 'required': 'required', 'placeholder': "Last Name"}),
            'email': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': "Email"}),
            'dob': forms.SelectDateWidget(years=YEARS,
                                          attrs={'class': 'form-control', 'placeholder': "Date of Birth"}),
            'phone': forms.TextInput(
                attrs={'class': 'form-control', 'required': 'required', 'placeholder': "Phone"}),
            'country': forms.TextInput(
                attrs={'class': 'form-control', 'required': 'required', 'placeholder': "Country"}),
            'state': forms.TextInput(
                attrs={'class': 'form-control', 'required': 'required', 'placeholder': "State"}),
            'city': forms.TextInput(
                attrs={'class': 'form-control', 'required': 'required', 'placeholder': "city"}),
            # 'gender':forms.
        }


class EducationalForm(forms.ModelForm):
    class Meta:
        model = EducationalInfo
        fields = ['program', 'institution', 'course', 'edate1', 'edate2']
        widgets = {

            'program': forms.TextInput(
                attrs={'class': 'form-control', 'required': 'required', 'placeholder': "Enter program"}),
            'institution': forms.TextInput(
                attrs={'class': 'form-control ', 'required': 'required', 'placeholder': "Enter Institution "}),
            'course': forms.TextInput(
                attrs={'class': 'form-control ', 'required': 'required', 'placeholder': "Enter Course"}),
            'edate1': forms.SelectDateWidget(years=YEARS,
                                             attrs={'class': 'form-control', 'placeholder': "Date of edate1"}),
            'edate2': forms.SelectDateWidget(years=YEARS,
                                             attrs={'class': 'form-control', 'placeholder': "Date of date2"}),

        }


class ExperienceForm(forms.ModelForm):
    class Meta:
        model = ExperienceInfo
        fields = ['company', 'title', 'course', 'startingDate', 'endingDate', 'experienceInfo']

        widgets = {

            'company': forms.TextInput(
                attrs={'class': 'form-control', 'required': 'required', 'placeholder': "Enter Company"}),
            'title': forms.TextInput(
                attrs={'class': 'form-control ', 'required': 'required', 'placeholder': "Enter Job Title "}),
            'course': forms.TextInput(
                attrs={'class': 'form-control ', 'required': 'required', 'placeholder': "Enter Course / Project"}),
            'startingDate': forms.SelectDateWidget(years=YEARS,
                                                   attrs={'class': 'form-control', 'placeholder': "Date of Birth"}),
            'endingDate': forms.SelectDateWidget(years=YEARS,
                                                 attrs={'class': 'form-control', 'placeholder': "Date of Birth"}),
            'experienceInfo': forms.Textarea(
                attrs={'class': 'form-control', 'required': 'required', 'placeholder': "Enter Company"}),
        }


class SkillForm(forms.ModelForm):
    class Meta:
        model = Skills
        fields = ['skill']

        widgets = {

            'skill': forms.TextInput(
                attrs={'class': 'form-control', 'required': 'required', 'placeholder': "Skills seperated by comma , "})
        }


class CertificateForm(forms.ModelForm):
    class Meta:
        model = Certificate
        fields = ['certificate', 'certificateDate']
        widgets = {

            'certificate': forms.TextInput(
                attrs={'class': 'form-control', 'required': 'required', 'placeholder': "Certificate Name "}),
            'certificateDate': forms.SelectDateWidget(years=YEARS,
                                                 attrs={'class': 'form-control', 'placeholder': "Certiciate issued Date"}),
        }

class LanguageForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = ['language']

        widgets = {

            'language': forms.TextInput(
                attrs={'class': 'form-control', 'required': 'required', 'placeholder': "Language"})
        }