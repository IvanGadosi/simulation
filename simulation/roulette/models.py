from django.db import models
from datetime import datetime, timedelta
from django.db.models.signals import post_delete
from django.dispatch.dispatcher import receiver
from django.core.validators import MaxValueValidator, MinValueValidator


class Graph(models.Model):
    graph_id=models.AutoField(primary_key=True)
    date_created=models.DateTimeField(default=datetime.now, editable=False)
    graph=models.ImageField(upload_to="files/", blank=True, null=True)

    turns=models.PositiveIntegerField(validators=[MinValueValidator(100), MaxValueValidator(10000)])
    money=models.PositiveIntegerField(validators=[MaxValueValidator(100000)])
    bet=models.PositiveIntegerField(validators=[MaxValueValidator(10000)])

    class Meta:
        verbose_name_plural = "graphs"

    def __str__(self):
        return str(self.graph_id)


@receiver(post_delete, sender=Graph)
def media_delete(sender, instance, **kwargs):
    instance.graph.delete(False)