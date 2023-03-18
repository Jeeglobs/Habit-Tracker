from django.shortcuts import render


def list_habits(request):
    user = request.user
    return render(request, 'core/index.html', {'user': user})
