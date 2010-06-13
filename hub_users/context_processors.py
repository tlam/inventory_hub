def current_user(request):
    return {
        'user': request.user,
    }
