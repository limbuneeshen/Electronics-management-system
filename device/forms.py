from django import forms
from .models  import Device,Category

class DeviceForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'name'}))
    description=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
    type = forms.ModelChoiceField(queryset=Category.objects.all(),widget=forms.Select(attrs={'class':'form-control'}))
    class Meta:
        model = Device
        fields = '__all__'