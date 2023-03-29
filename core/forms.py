from django.forms import ModelForm
from .models import Topico, Conteudo, Conversor, Nyquist, Shannon, Meios


class TopicoForm(ModelForm):
    class Meta:
        model = Topico
        fields = '__all__'

class ConteudoForm(ModelForm):
    class Meta:
        model = Conteudo
        fields = '__all__'

class ConversorForm(ModelForm):
    class Meta:
        model = Conversor
        fields = '__all__' 

class NyquistForm(ModelForm):
    class Meta:
        model = Nyquist
        fields = '__all__'    

class ShannonForm(ModelForm):
    class Meta:
        model = Shannon
        fields = '__all__'   

class MeiosForm(ModelForm):
    class Meta:
        model = Meios
        fields = '__all__' 