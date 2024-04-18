from django.shortcuts import render

from .models import Menu

menus = Menu.objects.all()


def index(request):
    return render(request, 'menu/index.html', {'menus': menus})


def draw_menu(request, path):
    splitted_path = path.split('/')
    menu_name = splitted_path[0]
    menu_item = splitted_path[-1]
    context = {
        'main_menu': {'menu_name': menu_name,
                      'menu_item': menu_item,
                      },
        'menus': menus,
    }
    return render(request, 'menu/index.html', context)
