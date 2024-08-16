from django.shortcuts import render

def packages_india_view(request):
    return render(request, 'tt_html/packages_india.html')
