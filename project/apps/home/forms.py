from django import forms

from . import models

class cita_agendaForm(forms.ModelForm):
    class Meta:
        model = models.cita_agenda
        fields = "__all__"
        

class autorForm(forms.ModelForm):
    class Meta:
        model = models.autor
        fields = "__all__"
        
        
class clienteForm(forms.ModelForm):
    class Meta:
        model = models.cliente
        fields = "__all__"