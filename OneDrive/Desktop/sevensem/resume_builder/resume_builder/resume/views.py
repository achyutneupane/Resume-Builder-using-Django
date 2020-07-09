import datetime
from django.shortcuts import render, redirect, HttpResponse
from .forms import *
from django.forms import modelformset_factory
from django.db import transaction, IntegrityError
from .utils import *
from django.views.generic import View


# Create your views here.
def index(request):
    data = {
        'personalinfodata': PersonalInfo.objects.filter(author__username=request.user)
    }
    return render(request, 'pages/index.html', data)


def resumeForm(request):
    personalform = PersonalInfoForm(request.POST or None)
    EduFormset = modelformset_factory(EducationalInfo, form=EducationalForm)
    eduform = EduFormset(request.POST or None, queryset=EducationalInfo.objects.none(), prefix='educationalInfo')
    ExpFormset = modelformset_factory(ExperienceInfo, form=ExperienceForm)
    experienceform = ExpFormset(request.POST or None, queryset=ExperienceInfo.objects.none(), prefix='experienceInfo')
    SkillFormset = modelformset_factory(Skills, form=SkillForm)
    skillsform = SkillFormset(request.POST or None, queryset=Skills.objects.none(), prefix='skills')
    certificateFormset = modelformset_factory(Certificate, form=CertificateForm)
    certificateform = certificateFormset(request.POST or None, queryset=Certificate.objects.none(),
                                         prefix='certificate')
    languageFormset = modelformset_factory(Language, form=LanguageForm)
    languageform = languageFormset(request.POST or None, queryset=Language.objects.none(), prefix='language')

    if request.method == 'POST':
        if personalform.is_valid() and eduform.is_valid() \
                and experienceform.is_valid() and skillsform.is_valid() \
                and certificateform.is_valid() and languageform.is_valid():

            print("test complited")
            try:
                with transaction.atomic():
                    personalinfo = personalform.save(commit=False)
                    personalinfo.author = request.user
                    personalinfo.save()

                    for educationalInfo in eduform:
                        data = educationalInfo.save(commit=False)
                        data.personalinfo = personalinfo
                        data.save()

                    for experienceInfo in experienceform:
                        experienceforms = experienceInfo.save(commit=False)
                        experienceforms.personalinfo = personalinfo
                        experienceforms.save()

                    for skills in skillsform:
                        skillsforms = skills.save(commit=False)
                        skillsforms.personalinfo = personalinfo
                        skillsforms.save()

                    for certicate in certificateform:
                        certificateforms = certicate.save(commit=False)
                        certificateforms.personalinfo = personalinfo
                        certificateforms.save()

                    for language in languageform:
                        languageforms = language.save(commit=False)
                        languageforms.personalinfo = personalinfo
                        languageforms.save()

            except IntegrityError:
                print('error')

            return redirect('resumeform')

    data = {
        'form': personalform,
        'formset': eduform,
        'experienceform': experienceform,
        'skillform': skillsform,
        'certificateform': certificateform,
        'languageform': languageform
    }
    return render(request, 'form/testform.html', data)


def templates(request, id):
    if request.user.is_authenticated:
        data = templatesdata(id)
    else:
        return redirect('resumeform')
    return render(request, 'resumes/resume1.html', data)


def templatesdata(id):
    data = {
        'personalinfodata': PersonalInfo.objects.get(id=id),
        'educationalinfodata': EducationalInfo.objects.filter(personalinfo__id=id),
        'experienceinfodata': ExperienceInfo.objects.filter(personalinfo__id=id),
        'certificatedata': Certificate.objects.filter(personalinfo__id=id),
        'skilldata': Skills.objects.filter(personalinfo__id=id),
        'languagedata': Language.objects.filter(id=id),

    }
    return data


def storage(request):
    data = {
        'personalinfodata': PersonalInfo.objects.filter(author__username=request.user)
    }
    return render(request, 'pages/storage.html', data)


def generate_view(request, id, *args, **kwargs):
    template = get_template('pdf/invoice.html')
    data = templatesdata(id)
    html = template.render(data)
    pdf = render_to_pdf('pdf/invoice.html', data)
    if pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "Invoice_%s.pdf" % ("12341231")
        content = "inline; filename='%s'" % (filename)
        download = request.GET.get("download")
        if download:
            content = "attachment; filename='%s'" % (filename)
        response['Content-Disposition'] = content
        return response
    return HttpResponse("Not found")
