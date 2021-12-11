import random
import string

from django.shortcuts import HttpResponse, redirect

from .models import Link


def add_url(request) -> HttpResponse:
    """
    Checks if url parameter in request dictionary.
    Checks for such url existing in DB.
    If url isn`t uniq returns the code for this url.
    If url is uniq generates the uniq code for this url
    and add code in DB.
    """
    if request.GET.get('url'):
        url = request.GET.get('url')
        link, status = Link.objects.get_or_create(url=url)

        if not status:  # If status create equals False. In other words - if url is in DB.
            code = link.code
            return HttpResponse(f'<h3>Код для ссылки {url} - {code}</h3>')

        code = generate_code()
        link.code = code
        link.save()
        return HttpResponse(f'<h3>Код для ссылки {url} - {code}</h3>')

    return HttpResponse('Не найден параметр url')


def generate_code() -> str:
    """
    Generates 8 digits code.
    Checks if such code exists in DB.
    If code uniq returns code.
    Other way repeats the loop.
    """
    code = ''.join(random.choices(string.digits + string.ascii_letters, k=8))
    while len(Link.objects.filter(code=code)) != 0:
        code = generate_code()

    return code


def show_url(request, code: str) -> HttpResponse or redirect:
    """
    Takes code as an argument.
    Check for correct len of the code.
    Looks in DB for row with given code.
    If row does exist, redirects to url.
    If no such code in DB, return html msg.
    """
    if len(code) != 8:
        return HttpResponse('Код должен состоять из восьми символов. '
                            f'Код предостваленный вами - {code} '
                            f'состит из {len(code)} символов. '
                            'Пожалуйста проверте код.')

    link = Link.objects.filter(code=code)
    if len(link) != 0:
        url = link[0].url
        return redirect(url)

    return HttpResponse(f'{code} этот код не привязан к ссылке.')
