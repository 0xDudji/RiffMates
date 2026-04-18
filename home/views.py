from django.http import HttpResponse

def credits(request):
    content = "Nicky\nYour Name"
    
    return HttpResponse(content, content_type="text/plain")

def about(request):
    content = "<h1>This is a website for sharing guitar riffs and collaborating with other musicians.</h1>"
    
    return HttpResponse(content, content_type="text/html")

def version(request):
    content = '{"version": "1.0.0"}'
    
    return HttpResponse(content, content_type="application/json")