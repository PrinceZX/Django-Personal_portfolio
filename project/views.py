from django.shortcuts import render, get_object_or_404


from .models import AutoProject
# Create your views here.

def home(request):
    projects = AutoProject.objects.all()
    return render(request, 'project/home.html', {'projects':projects})

def all_projects(request):
    projects = AutoProject.objects.order_by('-date')[:5]
    return render(request, 'project/all_projects.html', {'projects':projects})

def detail(request, project_id):
    project = get_object_or_404(AutoProject, pk=project_id)
    return render(request, 'project/detail.html', {'project':project})
