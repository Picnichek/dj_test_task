from django.db import models
from django.urls import reverse


class Menu(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="Название меню",
        unique=True,
    )

    class Meta:
        ordering = ['id']
        verbose_name = "Меню"
        verbose_name_plural = 'Меню'

    def get_absolute_url(self):
        return reverse("draw_menu", kwargs={"path": self.name})

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    name = models.CharField(
        'Название пункта меню', max_length=50, unique=True)

    description = models.TextField(
        'Описание', max_length=300, blank=True)
    url = models.CharField(
        verbose_name='URL-адрес стороннего ресурса',
        help_text=(
            'Указывается для перехода на ресурс из конечного пункта меню, '
            'если не указать, то алгоритм будет пытаться найти потомков '
            'данного пункта меню и создать из них подменю'),
        max_length=50, blank=True)
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True)
    menu = models.ForeignKey(
        Menu, on_delete=models.CASCADE, related_name='menu_items')

    class Meta:
        ordering = ['id']
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'

    def get_absolute_url(self):
        path_parts = [self.name]
        current_parent = self.parent
        while current_parent:
            path_parts.insert(0, current_parent.name)
            current_parent = current_parent.parent

        menu_name = self.menu.name
        path = '/'.join(path_parts)
        if self.parent:
            return reverse("draw_menu", kwargs={"path": f'{menu_name}/{path}'})
        else:
            return reverse("draw_menu", kwargs={"path": f'{menu_name}/{self.name}'})

    def __str__(self):
        return self.name
