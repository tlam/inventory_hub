from cgi import escape
import cStringIO as StringIO    
import os

from django.conf import settings
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template

import ho.pisa as pisa


def capwords(s):
    word_list = s.split(' ')
    cap_word_list = []
    for word in word_list:
        cap_word_list.append(word.capitalize())

    return ' '.join(cap_word_list)


def fetch_resources(uri, rel):
    """ 
    Prepares paths for pisa
    """
    path = os.path.join(settings.MEDIA_ROOT, uri.replace(settings.MEDIA_URL, ''))
    return path


def render_to_pdf(template_src, context_dict, filename):
    template = get_template(template_src)
    context = Context(context_dict)
    html = template.render(context)

    encoding = 'utf-8'
    response = HttpResponse(mimetype='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=%s.pdf' % filename
    pdf = pisa.pisaDocument(StringIO.StringIO(html.encode(encoding)), response, encoding=encoding, link_callback=fetch_resources)    
    if not pdf.err:
        return response    
    return HttpResponse('We had some errors<pre>%s</pre>' % escape(html))
