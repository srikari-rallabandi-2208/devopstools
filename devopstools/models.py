from django.db import models


class TopResult(models.Model):
    cpu_data = models.TextField()
    memory_data = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.created_at)


class ProcessResult(models.Model):
    pid = models.IntegerField()
    ppid = models.IntegerField()
    user = models.CharField(max_length=100)
    cpu = models.FloatField()
    memory = models.FloatField()
    command = models.CharField(max_length=255)

    def __str__(self):
        return str(self.pid)


class JavaProcess(models.Model):
    pid = models.IntegerField()
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=100)
    cmdline = models.TextField()

    def __str__(self):
        return str(self.pid)
