from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def informatics(request):
    tasks = [
        'Что такое алгоритм?',
        'Что такое оперативная память?'
    ]
    return render(request, 'subject.html', {
        'subject': 'Информатика',
        'tasks': tasks
    })


def physics(request):
    tasks = [
        'Что такое физическое тело?',
        'Как найти скорость движения тела?'
    ]
    return render(request, 'subject.html', {
        'subject': 'Физика',
        'tasks': tasks
    })


def mathematics(request):
    tasks = [
        'Решите уравнение: 2x + 5 = 15.',
        'Найдите площадь квадрата со стороной 6 см.'
    ]
    return render(request, 'subject.html', {
        'subject': 'Математика',
        'tasks': tasks
    })