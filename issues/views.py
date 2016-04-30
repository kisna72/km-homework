from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "index.html")

def add_issue(request):
    return render(request, "add_issue.html")



def add_solution(request):
    return render(request, "add_solution.html")


def search(request):
    return render(request, "search.html")


def about(request):
    return render(request, "about.html")