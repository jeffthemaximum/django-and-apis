from django import forms
from .models import Todo
from friendship.models import Friend
from datetimewidget.widgets import DateTimeWidget
from django.contrib.auth.models import User


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
            'title': forms.TextInput(attrs={'placeholder': 'Title'}),
            'text': forms.Textarea(attrs={'placeholder': 'Detailed description', 'rows': 4}),
            'due_date': DateTimeWidget(attrs={'id': "yourdatetimeid", 'placeholder': "Due Date"}, usel10n=True, bootstrap_version=3),
            'shared_user': forms.SelectMultiple()
        }


    def __init__(self, user=None, **kwargs):
        super(TodoForm, self).__init__(**kwargs)
        if user:
            friends = Friend.objects.filter(from_user=user)
            friend_users = map(lambda x: x.to_user.username, friends)
            friend_users_queryset = User.objects.filter(username__in=friend_users)
            self.fields['shared_user'].queryset = friend_users_queryset
