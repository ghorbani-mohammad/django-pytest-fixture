from django.test import TestCase
from django.contrib.auth.models import Group

class MyTest(TestCase):
    fixtures = ["group.json"]
    
    def test_should_create_group(self):
        group = Group.objects.get(pk=1)
        self.assertEqual(group.name, "appusers")
