from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def main(request):
    title = 'Головна'
    context = {
        'title': title,
    }
    return render(request, 'mainapp/index.html', context)

def voicep243():
    pass