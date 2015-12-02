from django import forms
from .models import Todo
from datetimewidget.widgets import DateTimeWidget


class TodoForm(forms.ModelForm):

    class Meta:
        model = Todo
        fields = (
            'title',
            'text',
            'due_date',
            'shared_user',
            'completed',
        )
        widgets = {
            'title' : forms.TextInput(attrs = {'placeholder': 'Title'}),
            'text' : forms.Textarea(attrs = {'placeholder': 'Detailed description', 'rows': 4}),
            'due_date': DateTimeWidget(attrs={'id':"yourdatetimeid", 'placeholder': "Due Date"}, usel10n = True, bootstrap_version=3),
            'shared_user': forms.SelectMultiple()
        }
