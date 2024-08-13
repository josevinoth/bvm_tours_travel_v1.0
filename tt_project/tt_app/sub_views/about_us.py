from django.shortcuts import render

def about_us(request):
    return render(request, 'tt_html/about_us.html')
