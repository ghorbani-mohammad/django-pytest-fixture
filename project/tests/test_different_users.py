import pytest
from django.contrib.auth.models import User, Group, Permission

@pytest.fixture
def app_user_group(db) -> Group:
    group = Group.objects.create(name="app_user")
    change_user_permissions = Permission.objects.filter(
        codename__in=["change_user", "view_user"],
    )
    group.permissions.add(*change_user_permissions)
    return group

@pytest.fixture
def user_A(db, app_user_group: Group) -> User:
    user = User.objects.create_user("A")
    user.groups.add(app_user_group)
    return user

@pytest.fixture
def user_B(db, app_user_group: Group) -> User:
    user = User.objects.create_user("B")
    user.groups.add(app_user_group)
    return user

def test_should_create_two_users(user_A: User, user_B: User) -> None:
    assert user_A.pk != user_B.pk
