from django.shortcuts import render
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from .models import Project

def project_list(request):
    projects = Project.objects.all()
    paginator = Paginator(projects, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render( request, 'projects/project_list.html',{'page_obj': page_obj})

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'projects/project_detail.html', {'project': project})