from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import event

# Create your views here.
def index(request):
    querySet = event.objects
    mondaySet = querySet.filter(day="Monday")
    TruesdaySet = querySet.filter(day="Tuesday")
    WednesdaySet = querySet.filter(day="Wednesday")
    ThrusdaySet = querySet.filter(day="Thursday")
    FridaySet = querySet.filter(day="Friday")
    events={}
    events['Monday'] = mondaySet
    events['Tuesday'] = TruesdaySet
    events['Wednesday'] = WednesdaySet
    events['Thursday'] = ThrusdaySet
    events['Friday'] = FridaySet
    events['All'] = querySet.all()
    # print(events)
    return render(request, "design/index.html", {"events": events})


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
    # print("%s %s %s %s " %(name, day, startTime, endTime))
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

def event_delete(request):
    id = request.POST.get('course', '')
    print(id)
    try:
        obj = event.objects.get(id=id)
        obj.delete()
    except Exception as e:
        print(e)
        return redirect('/design/index/')
    else:
        print("successfully deleted")
        return redirect('/design/index/')


def demo(request):
    return render(request, "design/demo.html")

def get_events(request):
    day = request.GET.get("day")
    queryset = event.objects.filter(day=day)
    arr = []
    for obj in queryset:
        arr.append({'id':obj.id, 'name': obj.name})
    return JsonResponse({'code': 0, "data": arr})