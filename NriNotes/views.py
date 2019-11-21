from django.shortcuts import render,redirect
from . models import Subscriber, Content, User
from django.core.mail import EmailMessage

def index(request):
   return render(request,'Index.html')

def about(request):
   return render(request,'About.html')

def Subscribe(request):
   name=request.POST['fullname']
   email=request.POST['email']
   data=Subscriber(name=name,email=email)
   data.save()
   mail = EmailMessage('WELCOME','welcome to engineering notes. You have successfully registered to this website. You will be notified through a mail for all the updates on this website.',to = [email])
   mail.send()
   return redirect('/')

def notes(request):
   return render(request,'Notes.html')

def search(request):
   content_type=request.POST['type']
   branch=request.POST['branch']
   semester=request.POST['semester']
   data=Content.objects.all().filter(content_type=content_type,branch=branch,semester=semester)
   return render(request,'NotesSearch.html',{'data':data})

def adminlogin(request):
   return render(request,'AdminLogin.html')

def checklogin(request):
   username=request.POST['username']
   password=request.POST['password']
   login=False
   data=User.objects.all().filter(username=username)
   for i in data:
      if i.password==password:
         login=True
         break
   if login:
      return render(request,'Upload.html')
   else:
      return redirect('/AdminLogin')

def upload(request):
   content_type=request.POST['type']
   branch=request.POST['branch']
   semester=request.POST['semester']
   subject=request.POST['subject']
   file=request.FILES['file']
   data=Content(content_type=content_type,branch=branch,semester=semester,subject=subject,file=file)
   data.save()
   data = Subscriber.objects.all()
   receiver =[]
   for i in data:
      receiver.append(i.email)
   email = EmailMessage('Content Uploaded','We have uploaded '+content_type+' for '+branch+' branch and '+semester+' semester for the subject '+subject,to = receiver)
   email.send()
   return render(request,'Upload.html')
   
   
