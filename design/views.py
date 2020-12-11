from django.shortcuts import render, redirect
from .models import event

# Create your views here.
def index(request):
    return render(request, "design/index.html")


def event_create(request):
    print("hello")
    if not request.META['REQUEST_METHOD'] == 'POST':
        print("failed")
        return redirect('/design/index/')

    name = request.POST.get("name", "")
    day =  request.POST.get("day", "")
    startTime = request.POST.get("startTime","")
    endTime = request.POST.get("endTime", "")
    details = request.POST.get("details", "")
    print("%s %s %s %s " %(name, day, startTime, endTime))
    if not name or not day or not startTime:
        print("error")
        redirect('/design/index/')

    obj = event()
    obj.name = name
    obj.day = day
    obj.startTime = startTime
    obj.endTime = endTime
    obj.details = details
    print("%s %s %s %s " % (obj.name, obj.day, obj.startTime, obj.endTime))
    try:

        obj.save()
    except Exception as e:
        print(e)
        return redirect('/design/index/')
    else:
        print("successfully created")
        return redirect('/design/index/')


def demo(request):
    return render(request, "design/demo.html")