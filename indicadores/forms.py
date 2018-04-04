from django import forms
from .models import Indicadores

class IndicadorForm(forms.ModelForm):
    indicador = forms.CharField(label="Indicador", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Indicador'}))
    eje = forms.CharField(label="Eje", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Eje'}))
    objetivo = forms.CharField(label="Objetivo", widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Objetivo','rows':5}))
    estrategia = forms.CharField(label="Estrategia", widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Estrategia','rows':5}))
    linea_accion = forms.CharField(label="Línea de acción", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Línea de acción'}))
    descripcion = forms.CharField(label="Descripción", widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Descripción','rows':5}))
    nombre_formato = forms.CharField(label="Nombre de formato", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre de formato'}))
    dimension_medir = forms.CharField(label="Dimensión a medir", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Dimensión a medir'}))
    observaciones = forms.CharField(label="Observaciones", widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Descripción','rows':5}))
    metodo_calculo = forms.CharField(label="Método de Cálculo", widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Método de Cálculo','rows':5}))
    frecuencia_medicion = forms.CharField(label="Frecuencia de medición", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Frecuencia de medición'}))
    fuente = forms.CharField(label="Fuente", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Fuente'}))
    responsable = forms.CharField(label="Responsable", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Responsable'}))
    meta_programada = forms.CharField(label="Meta programada", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Meta programada'}))
    sentido_indicador = forms.CharField(label="Sentido indicativo", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Sentido indicativo','value':'Ascendente'}))
    medicion_anterior = forms.CharField(label="Medición Anterior", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Medición Anterior'}))
    linea_base = forms.CharField(label="Línea de base", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Línea de base'}))
    elaboro = forms.CharField(label="Elaboró", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Elaboró'}))


    class Meta:
        model = Indicadores
        fields = ['indicador','eje','objetivo','estrategia','linea_accion','descripcion','nombre_formato','dimension_medir',
        'observaciones','metodo_calculo','frecuencia_medicion','fuente','responsable','meta_programada','sentido_indicador',
        'medicion_anterior','linea_base','elaboro']
