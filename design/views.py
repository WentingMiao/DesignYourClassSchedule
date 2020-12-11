from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "design/index.html")


def demo(request):
    return render(request, "design/demo.html")