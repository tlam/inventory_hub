from utils.constants import APP_CHOICES


def site_wide(request):
    app_name = request.GET.get('current-app', '')
    if not app_name:
        full_path = request.get_full_path()
        full_path_list = full_path.split('/')
        if len(full_path_list) > 2:
            app_name = full_path_list[1]
        else:
            app_name = ''

    return {
        'app_choices': APP_CHOICES,
        'app_name': app_name,
    }
