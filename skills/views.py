from django.shortcuts import render
from .models import Skill

def skills(request):
    programming = Skill.objects.filter(category='Programming')
    analytics = Skill.objects.filter(category='Analytics')
    fintech = Skill.objects.filter(category='FinTech')
    tools = Skill.objects.filter(category='Tools')
    context = {
        'programming': programming,
        'analytics': analytics,
        'fintech': fintech,
        'tools': tools,}
    return render(request, 'skills/skill.html', context)