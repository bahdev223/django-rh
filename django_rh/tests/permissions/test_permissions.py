import pytest
from django.contrib.auth.models import User, Permission


class TestRHPermissions:
    def test_has_rh_create_perm(self, db):
        user = User.objects.create_user(username="test", password="test")
        perm = Permission.objects.get(codename="rh_create")
        user.user_permissions.add(perm)
        assert user.has_perm("django_rh.rh_create") is True
