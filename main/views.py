from django.shortcuts import render


def main_menu(request):
    menu = ['Главная', 'Меню', 'Вход', 'Выход', 'Регистрация']
    return render(request, 'main/main.html', {'menu': menu})
