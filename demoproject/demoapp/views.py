from django.http import HttpResponse
from django.views import View
from demoapp.forms import DemoForm,DemoModelForm
from django.shortcuts import render


def form_view(request):
    form =DemoModelForm()
    if request.method == "POST":
        form=DemoModelForm(request.POST)
        if form.is_valid():
            form.save()
        
    context ={"form":form}
    return render(request,"home.html",context)

def form_view_2(request):
    form =DemoForm()
    context ={"form":form}
    return render(request,"home_2.html",context)


# Create your views here.
def index(request):
    path  = request.path
    method = request.method
    scheme = request.scheme
    address = request.META['REMOTE_ADDR']
    user_agent = request.META['HTTP_USER_AGENT']
    content = f"""<center><h2>Testing Django Request Response Objects</h2> 
<p>Request path : " {path}</p> 
<p>Request Method :{method}</p></center> 
<p>Request scheme :{scheme}</p></center> 
<p>Request address :{address}</p></center> 
<p>Request user_agent :{user_agent}</p></center> """
    return HttpResponse(content, content_type='text/html',charset='utf-8')


# class based views
class MyView(View):
    def get(self, request):
        # logic
        # 'result = 
        return HttpResponse('result')
    def post(self, request):
        # logic
        # 'result = 
        return HttpResponse('result')
    
# handling errors 
from django.http import Http404, HttpResponse 
from .models import Menu 

def detail(request, id): 
    try: 
        p = Menu.objects.get(pk=id) 
    except Product.DoesNotExist: 
        raise Http404("Product does not exist") 
    return HttpResponse("Product Found") 

def myview(request): 
    if not request.user.has_perm('myapp.view_mymodel'): 
        raise PermissionDenied() 
    return HttpResponse() 


# Custom error pages
"""
If you want to show your own error page whenever the user encounters a 404 error,
you must create a 404.html page and put it in the project/templates folder. 
"""

