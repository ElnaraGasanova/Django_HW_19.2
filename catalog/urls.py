from django.urls import path

# указываем контроллеры home и contacts
urlspatterns = [
    path('',home, contacts, name='catalog')
]
