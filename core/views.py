from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def list_habits(request):
    user = request.user
    return render(request, 'core/index.html', {'user': user})
