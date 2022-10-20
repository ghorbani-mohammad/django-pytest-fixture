from django.contrib.auth.models import User

def test_should_create_user_with_username(db) -> None:
    user = User.objects.create_user("Haki")
    assert user.username == "Haki"
