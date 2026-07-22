from django.db import models
from django.utils.translation import gettext_lazy as _


class Department(models.Model):
    code = models.CharField(max_length=20, unique=True, verbose_name="Code")
    name = models.CharField(max_length=255, verbose_name="Nom")
    description = models.TextField(blank=True, verbose_name="Description")
    manager = models.ForeignKey(
        "django_rh.Employee", null=True, blank=True, on_delete=models.SET_NULL,
        related_name="managed_departments", verbose_name="Responsable",
    )

    class Meta:
        verbose_name = "Département"
        verbose_name_plural = "Départements"
        ordering = ["name"]

    def __str__(self):
        return f"{self.code} - {self.name}"
