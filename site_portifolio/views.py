from django.shortcuts import render

# Create your views here.

def home(request):
    nome = 'Samyra'
    conhecimentos = ['HTML', 'CSS', 'JavaScript', 'Python', 'Django', 'Gi', 'Tamborim', 'Dar cambalhotas', 'Palntar bananeira']
    return render(request, 'index.html', {'conhecimentos': conhecimentos, 'nome'= nome})