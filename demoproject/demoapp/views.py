from django.http import HttpResponse

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