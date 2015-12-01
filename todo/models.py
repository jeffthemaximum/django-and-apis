from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Todo(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)
    due_date = models.DateTimeField(
        blank=True, null=True)
    shared_user = models.ManyToManyField(User, related_name="shared_users")
    completed = models.BooleanField(default=False)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
