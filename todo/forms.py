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
            # gets a list of all a user's friends
            friends = Friend.objects.filter(from_user=user)
            # converts friend objects to list of friends' usernames
            friend_users = map(lambda x: x.to_user.username, friends)
            # gets a list of user objects - the users who are friends with the original user
            friend_users_queryset = User.objects.filter(username__in=friend_users)
            # sets the shared_user field to only display a user's friends
            self.fields['shared_user'].queryset = friend_users_queryset
