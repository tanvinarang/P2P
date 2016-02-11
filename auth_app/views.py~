from django.shortcuts import render
import datetime
import json
from django.conf import settings
from django.contrib import messages
from django.contrib import auth
from django.core.mail import send_mail
from django.shortcuts import render, redirect,get_object_or_404
from django.template.defaultfilters import slugify
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from .models import Post,Person
from django.http import HttpResponse, HttpResponseRedirect
from django.template.defaultfilters import slugify
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.template import Context
#from django.contrib.auth.forms import UserCreationForm
#from .forms import DocumentForm


#User.email=None

# Create your views here.
def landingPage(request):
	##if request.user.is_authenticated():
		#return redirect('landingPage')
	if request.method=='GET':
		return render(request,'auth_app/index.html')
        

@csrf_exempt
def SignUp(request):
    data=request.POST
    if request.method == 'POST':
       user=User.objects.create_user(username=data['name'],first_name=data['name'],email=data['email'],password=data['password'])
       user.save()
       profile=Person(user=user,phone=data['phone'])
       profile.save()
       emailid = data['email']
       from_email=settings.EMAIL_HOST_USER
       to_email=[from_email,emailid]
       template_name="auth_app/success.html"
       c={
        	'user':'',
       }
       from django.template import loader
       message = loader.render_to_string(template_name, c)
       #send_mail(subject,message,from,to,fail_silently,html_message=message)
       send_mail('Welcome To P2P',message,from_email,to_email,fail_silently=True,html_message=message)
       return HttpResponse("Check your E-mail")
     
  
@csrf_exempt
def SignIn(request):
    return render(request,'auth_app/index.html' )

def auth_view(request):
    username =request.POST.get('username','')
    password =request.POST.get('password','')
    user=auth.authenticate(username=username,password=password)

    if user is not None:
       auth.login(request,user)#I want user to log in
       return HttpResponseRedirect('loggedin')
    else :
         return render(request,'auth_app/invalid.html')
    	
         
def loggedin(request):
    return render(request,'auth_app/dashboard.html', {'full_name' : request.user.username})

def BorrowersList(request):
   post=Post.objects.all()
   return render(request, 'auth_app/list.html',{'post':post})
   
       
@login_required(login_url = 'sign_in' )
def SignOut(request):
    auth.logout(request)
    return render(request,'auth_app/index.html')

@csrf_exempt
def single(request, postId):
    
    post = Post.objects.get(id=int(postId))#To get an id of the object,modify the template and then url!
    return render(request,'auth_app/form.html',{'post':post})
	
@csrf_exempt  
def Invest(request,post):
    
    p=Post.objects.get(id=int(post))
    amount=int(request.POST.get('amount',True))
    amt=int(p.amount_received)
    amt=amt+amount
    p.amount_received = amt 
    p.save()
    return render(request,'auth_app/list.html',{'p':p})
    #return HttpResponse("done")

def contact(request):
    
            
            
    return render(request , 'auth_app/contact.html')

def sendMessage(request):
    if request.method == 'POST':
       contact_name = request.POST.get('userName','')
       contact_email = request.POST.get('userEmail','')
       contact_number = request.POST.get('userPhone','')
       contact_message = request.POST.get('userMsg','')
       from_email=['contact_email']
       to_email=['narangtanvi19@gmail.com']
       template = "auth_app/success.html"
       context = Context({'contact_name': contact_name,'contact_email': contact_email,'contact_message': contact_message,})
       
       send_mail('Inquiry',contact_message,contact_email,to_email,fail_silently=True,html_message=contact_message)
       return HttpResponse("Message Successfully sent")


@login_required(login_url = 'sign_in' )
def dashboard(request):
   post=Post.objects.all()
   return render(request, 'auth_app/dashboard.html',{'post':post})


def myprofile(request):
    p=Person.objects.get(user__id=request.user.id) #To retreive a particular row in database
    return render(request, 'auth_app/profile.html',{'name':request.user.username,'email':request.user.email,'id':request.user.id,'salary':p.salary,'phone':p.phone})

def list(request):
    if request.method=='POST':
       form=DocumentForm(request.POST,request.FILES)
       if form.is_valid():
          newdoc=Person(image=request.FILES['docfile'])
          newdoc.save()

       return HttpResponseRedirect(reverse('auth_app.views.list'))
    else:
        form = DocumentForm()  # A empty, unbound form

    # Load documents for the list page
    person = Person.objects.all()

    # Render list page with the documents and the form
    return render( request,'auth_app/profile.html',{'person': person, 'form': form},context_instance=RequestContext(request))
    



		





