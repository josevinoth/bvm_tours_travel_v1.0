from django.shortcuts import render

def blog(request):
    return render(request, 'tt_html/blog.html')
