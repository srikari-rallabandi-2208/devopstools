from django.db import models

class TopResult(models.Model):
    cpu_data = models.TextField()
    memory_data = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.created_at)
