import pytest
from typing import List, Optional
from django.contrib.auth.models import User, Group, Permission


@pytest.fixture
def app_user_group(db) -> Group:
    group = Group.objects.create(name="app_user")
    change_user_permissions = Permission.objects.filter(
        codename__in=["change_user", "view_user"],
    )
    group.permissions.add(*change_user_permissions)
    return group

def create_app_user(
    username: str,
    password: Optional[str] = None,
    first_name: Optional[str] = "first name",
    last_name: Optional[str] = "last name",
    email: Optional[str] = "foo@bar.com",
    is_staff: str = False,
    is_superuser: str = False,
    is_active: str = True,
    groups: List[Group] = [],
) -> User:
    user = User.objects.create_user(
        username=username,
        password=password,
        first_name=first_name,
        last_name=last_name,
        email=email,
        is_staff=is_staff,
        is_superuser=is_superuser,
        is_active=is_active,
    )
    user.groups.add(*groups)
    return user

@pytest.fixture
def user_A(db, app_user_group: Group) -> User:
    return create_app_user(username="A", groups=[app_user_group])

@pytest.fixture
def user_B(db, app_user_group: Group) -> User:
    return create_app_user(username="B", groups=[app_user_group])

def test_should_create_user(user_A: User, app_user_group: Group) -> None:
    assert user_A.username == "A"
    assert user_A.email == "foo@bar.com"
    assert user_A.groups.filter(pk=app_user_group.pk).exists()

def test_should_create_two_users(user_A: User, user_B: User) -> None:
    assert user_A.pk != user_B.pk
