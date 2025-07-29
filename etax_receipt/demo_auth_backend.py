from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

class DemoBackend(BaseBackend):
    """
    Authenticate against a hardcoded demo account for UI testing without a database.
    """
    def authenticate(self, request, username=None, password=None, **kwargs):
        if username == 'demo' and password == 'demo1234':
            UserModel = get_user_model()
            user = UserModel(username='demo', email='demo@example.com', is_staff=True, is_superuser=True)
            user.set_password('demo1234')
            user.id = 1
            user._state.adding = False
            return user
        return None

    def get_user(self, user_id):
        if user_id == 1:
            UserModel = get_user_model()
            user = UserModel(username='demo', email='demo@example.com', is_staff=True, is_superuser=True)
            user.set_password('demo1234')
            user.id = 1
            user._state.adding = False
            return user
        return None
