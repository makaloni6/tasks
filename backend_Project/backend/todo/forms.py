from django import forms

class TodoForm(forms.Form):
    task_name = forms.CharField(label='タスク名')
    description = forms.CharField(label='説明')
    date = forms.DateTimeField(label='締切')
    estimated_time = forms.DateTimeField(label='予想作業時間')


# class SessionForm(forms.Form):
#     session = forms.CharField(label='session', required=False, \
#                               widget = forms.TextInput(attrs={'class':'form-control'}))
