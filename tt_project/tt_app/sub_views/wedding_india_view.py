from django.shortcuts import render

def wedding_india_view(request):
    return render(request, 'tt_html/wedding_india.html')