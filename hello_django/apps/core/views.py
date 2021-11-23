from django.shortcuts import render, HttpResponse


# Create your views here.

def hello(request, nome, idade):
    return HttpResponse('<h1> Hello {} - Idade: {} anos</h1>'.format(nome, idade))


def soma(request, valor1, valor2):
    resultado = valor1 + valor2
    return HttpResponse('{} + {} = {}'.format(valor1, valor2, resultado))


def multiplicacao(request, valor1, valor2):
    resultado = valor1 * valor2
    return HttpResponse('{} x {} = {}'.format(valor1, valor2, resultado))


def divisao(request, valor1, valor2):
    resultado = valor1 / valor2
    return HttpResponse('{} / {} = {}'.format(valor1, valor2, resultado))
