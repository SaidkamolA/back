from django.db import models
from users.models import User

class Gul(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='guls')
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s gul: {self.title}"

    class Meta:
        verbose_name = 'Gul'
        verbose_name_plural = 'Guls' 