import pytest
from django.contrib.auth.models import User

@pytest.fixture
def user_A(db) -> User:
    return User.objects.create_user("A")

def test_should_create_user_with_username(db) -> None:
    user = User.objects.create_user("Haki")
    assert user.username == "Haki"

def test_should_check_password(db, user_A) -> None:
    user_A.set_password("secret")
    assert user_A.check_password("secret") is True

def test_should_not_check_unusable_password(db, user_A) -> None:
    user_A.set_password("secret")
    user_A.set_unusable_password()
    assert user_A.check_password("secret") is False