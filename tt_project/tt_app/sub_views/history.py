from django.shortcuts import render

def history(request):
    return render(request, 'tt_html/history.html')
