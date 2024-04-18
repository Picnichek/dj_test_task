from menu.models import MenuItem
from django import template

register = template.Library()


@register.inclusion_tag('menu/menu.html')
def draw_menu(main_menu: dict = None):
    def get_menu(menu_item: str = None, submenu: list = None, items_dict: dict = None):
        if items_dict is None:
            items_dict = {}

        menu = items_dict.get(
            None, []) if menu_item is None else items_dict.get(menu_item, [])
        if submenu:
            menu.insert(menu.index(submenu[0].parent) + 1, submenu)
        parent_item = None
        if menu_item:
            parent_item = items_dict.get(f'{menu_item}_obj').parent
        try:
            parent_name = parent_item.name if parent_item else None
            return get_menu(parent_name, submenu=menu, items_dict=items_dict)
        except AttributeError:
            return get_menu(items_dict=items_dict, submenu=menu)
        except ValueError:
            return menu

    items = MenuItem.objects.filter(
        menu__name=main_menu['menu_name']).select_related('parent', 'menu', 'parent__parent')
    items_dict = {}
    for item in items:
        parent_name = item.parent.name if item.parent else None
        if parent_name not in items_dict:
            items_dict[parent_name] = []
        items_dict[parent_name].append(item)
        items_dict[f'{item.name}_obj'] = item
    return {'menu': get_menu(items_dict=items_dict)} if main_menu['menu_name'] == main_menu['menu_item'] \
        else {'menu': get_menu(main_menu['menu_item'], items_dict=items_dict)}
