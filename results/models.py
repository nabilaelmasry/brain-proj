from django.db import models
from django.contrib.auth.models import User

class Results(models.Model):
    result_user = models.ForeignKey(User, on_delete=models.CASCADE)
    result = models.IntegerField(default=0)
    image = models.ImageField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.result_user)
