from django.contrib.auth import get_user_model
from django.db import models


class Task(models.Model):
    is_done = models.BooleanField(default=False)
    details = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    owner = models.ForeignKey(get_user_model(), on_delete=models.DO_NOTHING)



