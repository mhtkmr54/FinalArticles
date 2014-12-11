#from django.template.loader import get_template
#from django.template import Context
#from mysite.books.models import Article
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
#from django.contrib.auth.forms import PasswordResetForm
from .forms import UserForgotPasswordForm
from django.shortcuts import render
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
#import datetime

#def hell(request):
  #  now = datetime.datetime.now()
  #  t = get_template('my.html')
   # html = t.render(Context({'current_date': now}))
   # return HttpResponse(html)
   
def search_form(request):
    return render(request, 'search_form.html')

def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        books = Article.objects.filter(title__icontains=q)
        return render(request, 'search_results.html',
            {'books': books, 'query': q})
    else:
        return HttpResponse('Please submit a search term.')

def login(request):
    c={}
    c.update(csrf(request))
    return render_to_response('login.html',c)

def auth_view(request):
    username = request.POST.get('username','')
    password = request.POST.get('password','')
    user = auth.authenticate(username=username,password=password)
    
    
    if user is not None:
        auth.login(request,user)
        return HttpResponseRedirect('/accounts/loggedin')
     
    else:
      return HttpResponseRedirect('/accounts/invalid')
    
def loggedin(request):
    return render_to_response('loggedin.html',{'full_name': request.user.username})

    
def invalid_login(request):
    return render_to_response('invalid_login.html')

def logout(request):
    auth.logout(request)
    return render_to_response('logout.html')

def register_user(request):
    if request.method == 'POST' :
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/register_success')
        
    args={}
    args.update(csrf(request))
    args['form'] = UserCreationForm()
    return render_to_response('register.html' , args)

def register_success(request):
    return render_to_response('register_success.html',{'full_name' : request.user.username})


def UserResetPassword(request):
    errors = []
    if request.method == 'POST':
       
        if request.POST.get('email') and '@' not in request.POST['email']:
            errors.append('Enter a valid e-mail address.')
        if not errors:
            send_mail('request for password reset','click on the link <a href="http://127.0.0.1:8000/accounts/forgot_password_FORM/">reset password</a> to fill password reset form',
                'mhtkmr54@gmail.com',
                [request.POST.get('email')],
            )
            return HttpResponseRedirect('/accounts/confirm/')
    return render(request, 'forgotpassword.html',
        {'errors': errors})

def confirm(request):
    return render(request, 'confirm.html')
    
   