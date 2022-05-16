from django.http import HttpResponse


def index(request):
    return HttpResponse('Главная страница. Её я сделал сам, прям как hackerman')


def group_posts(request, slug):
    return HttpResponse(f'Страница с постами. А вот и '
                        f'неведомое сообщение переданое ранее - {slug}')


