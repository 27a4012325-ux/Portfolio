from django.shortcuts import render
from profiles.models import Profile
from projects.models import Project
from skills.models import Skill

# Create your views here.
def home(request):
    profile = Profile.objects.first()
    total_projects = Project.objects.count()
    total_skills = Skill.objects.count()
    context = {
        'profile': profile,
        'total_projects': total_projects,
        'total_skills': total_skills
    }
    return render(request,'home/home.html',context)