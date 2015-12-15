from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from friendship.models import Friend


class Todo(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)
    due_date = models.DateTimeField(
        blank=True, null=True)
    completed_date = models.DateTimeField(
        blank=True, null=True)
    shared_user = models.ManyToManyField(
        User,
        related_name="shared_users",
        blank=True,
        null=True
    )
    completed = models.BooleanField(default=False)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def complete(self):
        self.completed = True
        self.completed_date = timezone.now()
        self.save()

    def incomplete(self):
        self.completed = False
        self.completed_date = None
        self.save()

    def author_has_friends(self):
        # returns true is author has friends, else false
        return Friend.objects.friends(self.author) != []

    def __str__(self):
        return self.title


# update such that tasks belog to todo's. tasks are what need to be completed in a to do.
class Task(models.Model):
    todo = models.ForeignKey(Todo)
    completed = models.BooleanField(default=False)
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title
