# django-rh

Moteur de gestion des ressources humaines pour Django — Écosystème ERP francophone.

## Fonctionnalités

- 👤 Gestion des employés (matricule, identité, coordonnées)
- 🏢 Départements
- 💼 Postes
- 📄 Contrats (CDI, CDD, Stage, Consultant)
- 🔄 Cycle de vie : Recruté → Actif → Suspendu → Terminé
- 📜 Historique complet des modifications
- 🔍 Audit trail
- 🔔 Système d'événements
- 🔒 Permissions granulaires
- 📊 API REST complète
- ⚙️ Configuration via settings Django

## Installation

```bash
pip install django-rh
```

## Configuration

```python
INSTALLED_APPS = [
    ...
    "django_rh",
]

RH = {
    "AUTO_NUMBERING": True,
    "ENABLE_HISTORY": True,
    "ENABLE_AUDIT": True,
    "DEFAULT_CONTRACT_TYPE": "CDI",
}
```

## Utilisation

```python
from django_rh.services import EmployeeService

svc = EmployeeService()
emp = svc.create(first_name="Jean", last_name="Dupont", contract_type="CDI")
svc.hire(emp.id)
svc.suspend(emp.id, reason="Suspension")
svc.terminate(emp.id, reason="Démission")
```

## Licence MIT
