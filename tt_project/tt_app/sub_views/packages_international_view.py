from django.shortcuts import render

def packages_international_view(request):
    return render(request, 'tt_html/packages_international.html')
