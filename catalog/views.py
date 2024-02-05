from django.shortcuts import render

def home(request):
    '''Контроллер, который будет обрабаывать
    наш запрос home.'''
    return render(request, 'home.html')

def contacts(request):
    '''Контроллер, который будет обрабаывать
    наш запрос contacts.'''
    return render(request, 'contacts.html')
