from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from basic_app.forms import ContactForm
from basic_app.models import Post
# Create your views here.

def index(request):
    return render(request, 'basic_app/index.html')


#portfolio_details view
def portfolio_details(request):
    return render(request, 'basic_app/portfolio-details.html')

def about(request):
    return render(request, 'basic_app/about.html')


def contact(request):
    contact_form = ContactForm()
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)

        if contact_form.is_valid():
            contact_form.save(commit=True)
            return HttpResponseRedirect(reverse('index'))
        else:
            return HttpResponse('form is not valid')
    return render(request,'basic_app/contact.html',{'contact_form':contact_form})




def services(request):
    return render(request, 'basic_app/services.html')


def blog_single(request):
    content = Post.objects.all()
    return render(request, 'basic_app/blog-single.html',{'admin_post':content})

#hire me view
def hire_me(request):
    return render(request, 'basic_app/hire_me.html')
