from contacts.models import Email, Phone
from home.models import Home
from stocks.models import Category
from utils.constants import APP_CHOICES, QUOTATIONS_APP


def site_wide(request):
    try:
        tax = Home.objects.get().tax
    except:
        tax = None

    app_name = request.GET.get('current-app', '')
    if not app_name:
        full_path = request.get_full_path()
        full_path_list = full_path.split('/')
        if len(full_path_list) > 2:
            app_name = full_path_list[1]
        else:
            app_name = ''

    print app_name == QUOTATIONS_APP

    return {
        'app_choices': APP_CHOICES,
        'app_name': app_name,
        'categories': Category.objects.all(),
        'email_choices': Email.EMAIL_CHOICES,
        'is_quotation': app_name == QUOTATIONS_APP,
        'phone_choices': Phone.PHONE_CHOICES,
        'tax': tax,
    }
