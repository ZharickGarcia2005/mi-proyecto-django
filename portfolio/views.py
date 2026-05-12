from django.shortcuts import render
from .models import Portfolio

def portfolio(request):
    proyectos = Portfolio.objects.all()
    return render(request, "portfolio/portfolio.html", {'proyectos': proyectos})