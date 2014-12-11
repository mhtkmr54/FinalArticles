from django.shortcuts import render
from django.http import HttpResponse
from forms import ArticleForm
#from django.template.loader import get_template
#from django.template import Context
from .models import Article
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordResetForm
from .forms import ContactForm
from .forms import ArticleForm
from books.models import Article
from django.shortcuts import render
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
#from books.forms import CommentForm
#import datetime

#def hell(request):
  #  now = datetime.datetime.now()
  #  t = get_template('my.html')
   # html = t.render(Context({'current_date': now}))
   # return HttpResponse(html)
   
def search_form(request):
    return render(request, 'search_form.html')

def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term or else why are you on this page?')
        elif len(q) > 20:
            errors.append('Article_name is never too long,use ommom sense, Please enter at most 20 characters.')
        else:
            books = Article.objects.filter(title__icontains=q)
            return render(request, 'search_results.html',
                {'books': books, 'query': q})
    return render(request, 'search_form.html',
        {'errors': errors})

def contact(request):
    form = ContactForm(request.POST)
    errors = []
    if request.method == 'POST':
        if not request.POST.get('subject', ''):
            errors.append('Enter a subject.')
        elif not request.POST.get('message', ''):
            errors.append('Enter a message.')
        elif request.POST.get('email') and '@' not in request.POST['email']:
            errors.append('Enter a valid e-mail address.')
        elif not errors:
            send_mail(
                request.POST['subject'],
                request.POST['message'],
                request.POST.get('email', 'noreply@example.com'),
                ['mhtkmrarticles@gmail.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')
        
    
        form = ContactForm(
            initial={'subject': 'I love your site!'}
        )
        
    return render(request, 'contact_form.html',
        { 'errors': errors,
          'subject': request.POST.get('subject', ''),
          'message': request.POST.get('message', ''),
          'email': request.POST.get('email', ''),
         })
   
def about(request):
     return render(request, 'about.html')
    
def contact_thanks(request):
    return render(request, 'thanks.html')

def articles(request):
    return render_to_response('articles.html',
                              {'articles':Article.objects.all() })

def article(request,article_id=1):
    return render_to_response('article.html',
                              {'article':Article.objects.get(id=article_id) })

def create(request):
    if request.method == 'POST' :
        form = ArticleForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/articles/all')
    else:
        form = ArticleForm()
    
    args={}
    args.update(csrf(request))
    args['form'] = form
    return render_to_response('create_article.html' , args)
   
def like_article(request,article_id):
    if article_id:
        a = Article.objects.get(id=article_id)
        count = a.likes
        count += 1
        a.likes=count
        a.save()
        
    return  HttpResponseRedirect('/articles/get/%s' % article_id)
        
def unlike_article(request,article_id):
    if article_id:
        a1 = Article.objects.get(id=article_id)
        count1 = a1.unlikes
        count1 += 1
        a1.likes=count1
        a1.save()
        
    return  HttpResponseRedirect('/articles/get/%s' % article_id)
        

   
    
    
     #if request.POST:,request.FILES
        #form=ArticleForm(request.POST)
 