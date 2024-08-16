from django.shortcuts import render

def group_tours(request):
    return render(request, 'tt_html/group_tours.html')
