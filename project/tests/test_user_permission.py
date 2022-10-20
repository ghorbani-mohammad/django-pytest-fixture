import pytest
from django.contrib.auth.models import User, Group, Permission

@pytest.fixture
def user_A(db) -> Group:
    group = Group.objects.create(name="app_user")
    change_user_permissions = Permission.objects.filter(
        codename__in=["change_user", "view_user"],
    )
    group.permissions.add(*change_user_permissions)
    user = User.objects.create_user("A")
    user.groups.add(group)
    return user

def test_should_create_user(user_A) -> None:
    assert user_A.username == "A"

def test_user_is_in_app_user_group(user_A) -> None:
    assert user_A.groups.filter(name="app_user").exists()
