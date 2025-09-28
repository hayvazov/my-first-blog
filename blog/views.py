from django.shortcuts import render


def post_list(request):
    return render(request, 'blog/post_list.html', {})


def limpieza_de_sofas(request):
    """Renderiza la página de servicio de limpieza de sofás."""
    return render(request, 'blog/limpieza_de_sofas.html')

