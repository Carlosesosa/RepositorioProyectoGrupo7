from django.shortcuts import render



def Home(request):
    return render(request,'inicio.html')

def SobreNosotros(request):
    return render(request, 'sobrenosotros.html')

