from django.http import HttpResponse

def front_page(request):
    return HttpResponse('Hello, world!', mimetype='text/plain')
