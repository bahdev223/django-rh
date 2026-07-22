# Architecture django-rh

Même structure que django-ventes et django-achats.

```
django_rh/
├── contracts/        # Interfaces pour autres packages
├── domain/           # Logique métier pure
├── models/           # Django ORM
├── services/         # Services applicatifs
├── selectors/        # Lecture
├── queries/          # Analytiques
├── api/              # REST API
├── serializers/      # DRF
├── permissions/      # Permissions
├── admin/            # Django Admin
├── signals/          # Événements
├── tasks/            # Tâches async
├── audit/            # Audit
├── tests/            # Tests
└── utils/            # Utilitaires
```
