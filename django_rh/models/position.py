from django.db import models
from django.utils.translation import gettext_lazy as _


class Position(models.Model):
    code = models.CharField(max_length=20, unique=True, verbose_name="Code")
    title = models.CharField(max_length=255, verbose_name="Intitulé")
    description = models.TextField(blank=True, verbose_name="Description")
    department = models.ForeignKey(
        "django_rh.Department", null=True, blank=True, on_delete=models.SET_NULL,
        verbose_name="Département",
    )

    class Meta:
        verbose_name = "Poste"
        verbose_name_plural = "Postes"
        ordering = ["title"]

    def __str__(self):
        return f"{self.code} - {self.title}"
