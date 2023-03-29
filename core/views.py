from django.shortcuts import redirect, render
from .models import Topico, Conteudo, Conversor
from .forms import TopicoForm, ConteudoForm, ConversorForm
from .funcoes import calculateNyquist, calculateShannon, conversor, qam

# Create your views here.
def index_view(request):
    return render(request, 'core/index.html')


def topicos_view(request):

    topicos = Topico.objects.all().order_by('ordem')

    context = {
        'topicos':topicos
    }

    return render(request, 'core/topicos.html', context)


def conversor_view(request):
    resultado = "Resultado"
    if request.method == "POST":
        valor = request.POST['valor']
        unidade1 = request.POST['unidade1']
        unidade2 = request.POST['unidade2']
        resultado = conversor(valor, unidade1, unidade2)
    context = {
        'resultado': resultado
    }

    return render(request, 'core/conversor.html', context)

def nyquist_view(request):
    resultado = "Resultado"
    if request.method == "POST":
        b = request.POST['b']
        v = request.POST['v']
        resultado = calculateNyquist(b, v)
    context = {
        'resultado': resultado
    }

    return render(request, 'core/nyquist.html', context)

def shannon_view(request):
    resultado = "Resultado"
    if request.method == "POST":
        b = request.POST['b']
        snr = request.POST['snr']
        resultado = calculateShannon(b, snr)
    context = {
        'resultado': resultado
    }

    return render(request, 'core/shannon.html', context)


def edita_topicos_view(request):

    topicos = Topico.objects.all().order_by('ordem')

    context = {
        'topicos':topicos
    }

    return render(request, 'core/edita_topicos.html', context)


def novo_topico_view(request):

    topico_form = TopicoForm(request.POST or None)
    if topico_form.is_valid():
        topico_form.save()
        return redirect('core:edita_topicos')

    context = {'topico_form':topico_form}
    return render(request, 'core/novo_topico.html', context)


def edita_topico_view(request, topico_id):

    topico = Topico.objects.get(id=topico_id)
    topico_form = TopicoForm(request.POST or None, instance=topico)
    if request.method == "POST" and topico_form.is_valid():
        topico_form.save()
        return redirect('core:edita_topicos')

    context = {'topico_form':topico_form, 'topico_id':topico_id}
    return render(request, 'core/edita_topico.html', context)


def apaga_topico_view(request, topico_id):
    topico = Topico.objects.get(id=topico_id)
    topico.delete()
    return redirect('core:edita_topicos')


def novo_conteudo_view(request):

    conteudo_form = ConteudoForm(request.POST or None)
    if conteudo_form.is_valid():
        conteudo_form.save()
        return redirect('core:edita_topicos')

    context = {'conteudo_form':conteudo_form}
    return render(request, 'core/novo_conteudo.html', context)


def edita_conteudo_view(request, conteudo_id):

    conteudo = Conteudo.objects.get(id=conteudo_id)
    conteudo_form = ConteudoForm(request.POST or None, instance=conteudo)
    if request.method == "POST" and conteudo_form.is_valid():
        conteudo_form.save()
        return redirect('core:edita_topicos')

    context = {'conteudo_form':conteudo_form, 'conteudo_id':conteudo_id}
    return render(request, 'core/edita_conteudo.html', context)


def apaga_conteudo_view(request, conteudo_id):
    conteudo = Conteudo.objects.get(id=conteudo_id)
    conteudo.delete()
    return redirect('core:edita_topicos')

def meios_view(request):
    return render(request, 'core/meios.html')

def sinais_view(request):
    return render(request, 'core/sinais.html')

def mpsk_view(request):
    

    return render(request, 'core/mpsk.html')

def mqam_view(request):
    resultado = "Resultado"
    if request.method == "POST":
        b = request.POST['b']
        db = request.POST['db']
        ber = request.POST['ber']
        resultado = qam(b, db, ber)
    context = {
        'resultado': resultado
    }
    return render(request, 'core/mqam.html', context)

def modulacoes_view(request):
    return render(request, 'core/modulacoes.html')
