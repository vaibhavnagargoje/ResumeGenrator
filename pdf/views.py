from django.shortcuts import render
from .models import Profile
import pdfkit 
from django.http import HttpResponse
from django.template import loader
import io
# Create your views here.

def accepts(request):
    if request.method=="POST":
       name=request.POST.get("name","")
       email = request.POST.get("email","eample@gmail.com")
       phone = request.POST.get("phone","") 
       address=request.POST.get("address","")
       summary = request.POST.get("summary","")
       degree = request.POST.get("degree","")
       school = request.POST.get("school","")
       university = request.POST.get("university","")
       previous_work = request.POST.get("previous_work","Fresher")
       skill = request.POST.get("skills","")

       profile =Profile(name=name,email=email,phone=phone,address=address,summary=summary,degree=degree,school=school,university=university,previous_work=previous_work,skills=skill)
       profile.save()


    return render(request, 'pdf/accept.html')

def resume(request,id):
    user_profile = Profile.objects.get(pk=id)
    template = loader.get_template('pdf/resume.html')
    html = template.render({"user_profile":user_profile})
    options={
        'page-size':'Letter',
        'encoding':"UTF-8",

    }
    pdf =pdfkit.from_string(html,False,options)
    response=HttpResponse(pdf,content_type='application/pdf')
    response['content-Disposition']='attachment'
    filename='resume.pdf'
    return response

def list(request):
    profile = Profile.objects.all()
    return render(request,'pdf/list.html',{"profiles":profile})